/**
 * @file mpu6050.c
 * @author Fernando Galassi 
 * @brief This files contains functions and methods to work with MPU6050 accel/gyro module
 * @version 0.1
 * @date 2022-09-03
 * 
 * @copyright  SMR Copyright (c) 2022
 * 
 */

#include <stdio.h>
#include <stddef.h>

#include "driver/i2c.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_log.h"    

#include "mpu6050.h"

/* Global variables */
uint8_t buffer[6];

static float accel[3];
static int16_t RawAccel[3];
static int16_t RawGyro[3];
static int16_t RawTemp;

MPU6050_Accelerometer_t AccelerometerSensitivity;
MPU6050_Gyroscope_t GyroscopeSensitivity;

/* Private Function prototypes */
static esp_err_t MPU6050_RegisterRead(uint8_t, uint8_t *, size_t);
static esp_err_t MPU6050_RegisterWriteByte(uint8_t, uint8_t);
static esp_err_t MPU6050_SetAccelerometer(uint8_t);
static esp_err_t MPU6050_SetGyroscope(uint8_t);
static esp_err_t MPU6050_EnableInts(bool);
static esp_err_t MPU6050_SetIntPin(void);
static esp_err_t MPU6050_SetDataRate(uint8_t);
static esp_err_t MPU6050_SetMotionDetectParams(uint8_t duration, uint8_t threshold);
static esp_err_t MPU6050_EnableTempSensor(bool en);
static esp_err_t MPU6050_PwrMgmt1(uint8_t);
static esp_err_t MPU6050_Config(uint8_t);
static esp_err_t MPU6050_GyroConfig(uint8_t);
static esp_err_t MPU6050_AccelConfig(uint8_t);
static esp_err_t MPU6050_SignalPathReset(void);
static void MPU6050_ParseAccel(void);
static void MPU6050_ParseGyro(float *);
static void MPU6050_ParseTemp(float *);
static esp_err_t MPU6050_WhoAmI(void);


/**
 * @brief This function performs a read sequence from MPU6050 device
 * 
 * @param reg_addr      Register to read
 * @param data          Communitacion buffer
 * @param len           Buffer size    
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_RegisterRead(uint8_t reg_addr, uint8_t *data, size_t len)
{
    return i2c_master_write_read_device(I2C_MASTER_NUM, MPU6050_I2C_ADDR, &reg_addr, 1, data, len, I2C_MASTER_TIMEOUT_MS / 10);
}

/**
 * @brief This function performs a write sequence into MPU6050 device.
 * 
 * @param reg_addr      Register to write
 * @param data          Communication buffer
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_RegisterWriteByte(uint8_t reg_addr, uint8_t data)
{
    int ret;
    uint8_t write_buf[2] = {reg_addr, data};

    ret = i2c_master_write_to_device(I2C_MASTER_NUM, MPU6050_I2C_ADDR, write_buf, sizeof(write_buf), I2C_MASTER_TIMEOUT_MS / 10);

    return ret;
}

/**
 * @brief This function is used to query MPU6050's I2C address as a "is alive?" test.
 * 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_WhoAmI(void)
{
    int ret;

    ret = MPU6050_RegisterRead(MPU6050_WHO_AM_I, buffer, 1);

    return ret;
}

/**
 * @brief This function sets the Accelerometer range
 * 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_SetAccelerometer(uint8_t param)
{
    int ret;
    uint8_t data;

    ret = MPU6050_RegisterRead(MPU6050_ACCEL_CONFIG, buffer, 1);
    if(!ret)
    {
        data = (buffer[0] & 0xE7) | (uint8_t)param << 3;
        ret = MPU6050_RegisterWriteByte(MPU6050_ACCEL_CONFIG, data);
        return ret;
    }
    else
    {
        return ret;
    }
}

/**
 * @brief This function sets the Gyroscope sensitivity
 * 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_SetGyroscope(uint8_t param)
{
    int ret;
    uint8_t data;

    ret = MPU6050_RegisterRead(MPU6050_GYRO_CONFIG, buffer, 1);
    if(!ret)
    {
        data = (buffer[0] & 0xE7) | (uint8_t)param<< 3;
        ret = MPU6050_RegisterWriteByte(MPU6050_GYRO_CONFIG, data);
        return ret;
    }
    else
    {
        return ret;
    }
}

/**
 * @brief This function enables/disables interruptions
 * 
 * @param en            Used as a flag for enable/disable
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_EnableInts(bool en)
{
    int ret;
    uint8_t data;

    if(en)
    {
        ret = MPU6050_RegisterRead(MPU6050_INT_ENABLE, buffer, 1);
        if(!ret)
        {
            data = 0x40; /* Only motion detect */
            ret = MPU6050_RegisterWriteByte(MPU6050_INT_ENABLE, data);
            
            return ret;
        }
        else
        {
            return ret;
        }
    }
    else
    {
        data = 0x00;
        ret = MPU6050_RegisterWriteByte(MPU6050_INT_ENABLE, data);
        
        return ret;
    }
}

/**
 * @brief This function sets the INT PIN
 * 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_SetIntPin(void)
{
    int ret;
    uint8_t data = 0x20; /* Low level . Push-Pull */

    ret = MPU6050_RegisterWriteByte(MPU6050_INT_PIN_CFG, data);
    
    return ret;
}

/**
 * @brief This function sets de data rate
 * 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_SetDataRate(uint8_t dataRate)
{
    int ret;
    
    ret = MPU6050_RegisterWriteByte(MPU6050_SMPLRT_DIV, dataRate);

    return ret;
}

/**
 * @brief This function sets the duration and threshold for motion detect
 * 
 * @param duration      Duration to set
 * @param threshold     Threshold to set
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_SetMotionDetectParams(uint8_t duration, uint8_t threshold)
{
    int ret;

    ret = MPU6050_RegisterWriteByte(MPU6050_MOT_DUR, duration);
    if(!ret)
    {
        ret = MPU6050_RegisterWriteByte(MPU6050_MOT_THR, threshold);
        
        return ret;
    }
    else
    {
        return ret;
    }
}

/**
 * @brief This function is used to read the Interrupt status register
 * 
 * @return esp_err_t    0 -> No error
 */
esp_err_t MPU6050_ReadInterrupts(void)
{
    int ret;

    ret = MPU6050_RegisterRead(MPU6050_INT_STATUS, buffer, 1);

    return ret;
}

/**
 * @brief This function enables/disables the temperature sensor
 * 
 * @param en            Used as a flag for enable/disable
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_EnableTempSensor(bool en)
{
    int ret;
    uint8_t data;

    if(en)
    {
        ret = MPU6050_RegisterRead(MPU6050_PWR_MGMT_1, buffer, 1);
        if(!ret)
        {
            data = (buffer[0] & 0xF7) | 0x08 << 3 ;
            ret = MPU6050_RegisterWriteByte(MPU6050_PWR_MGMT_1, data);

            return ret;
        }
        else
        {
            return ret;
        }
    }
    else
    {
        ret = MPU6050_RegisterRead(MPU6050_PWR_MGMT_1, buffer, 1);
        if(!ret)
        {
            data = (buffer[0] & 0xF7) | 0x00 << 3 ;
            ret = MPU6050_RegisterWriteByte(MPU6050_PWR_MGMT_1, data);

            return ret;
        }
        else
        {
            return ret;
        }
    }
}

/**
 * @brief This function is used to get accelerometer measures
 * 
 * @return esp_err_t    0 -> No error
 */
esp_err_t MPU6050_ReadAccelerometer(float *a)
{
    int ret;
    int i;
    
    ret = MPU6050_RegisterRead(MPU6050_ACCEL_XOUT_H, buffer, 6);

    if(!ret)
    {
        for(i = 0; i < 3; i++)
        {
            int j = 2 * i;
            RawAccel[i] = (int16_t)(buffer[j]);
            RawAccel[i] = RawAccel[i] << 8 ;
            RawAccel[i] = RawAccel[i] | buffer[j+1];
        }
        
        MPU6050_ParseAccel();
        
        for(i = 0; i < 3; i++)
            a[i] = accel[i];

        return ret;
    }
    else
    {
        return ret;
    }
}

/**
 * @brief This function is used to get gyroscope measures
 * 
 * @return esp_err_t    0 -> No error
 */
esp_err_t MPU6050_ReadGyroscope(float *gyro)
{
    int ret;
    int i;

    ret = MPU6050_RegisterRead(MPU6050_GYRO_XOUT_H, buffer, 6);
    if(!ret)
    {
        for(i = 0; i < 3; i++)
        {
            int j = 2 * i;
            RawGyro[i] = (int16_t)(buffer[j]);
            RawGyro[i] = RawGyro[i] << 8;
            RawGyro[i] = RawGyro[i] | buffer[j];
        }

        switch(AccelerometerSensitivity)
        {
            case MPU6050_Accelerometer_2G:
                for(i = 0; i < 3; i++)
                    (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_2);
                break;
            case MPU6050_Accelerometer_4G:
                for(i = 0; i < 3; i++)
                    (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_4);
                break;
            case MPU6050_Accelerometer_8G:
                for(i = 0; i < 3; i++)
                    (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_8);
                break;
            case MPU6050_Accelerometer_16G:
                for(i = 0; i < 3; i++)
                    (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_16);
                break;
        }

        return ret;
    }
    else
    {
        return ret;
    }
}

/**
 * @brief This function is used to get temperature measures
 * 
 * @return esp_err_t    0 -> No error
 */
esp_err_t MPU6050_ReadTemperature(float *temp)
{
    int ret;

    ret = MPU6050_RegisterRead(MPU6050_TEMP_OUT_H, buffer, 2);
    if(!ret)
    {
        RawTemp = (int16_t)(buffer[0] << 8 | buffer[1]);

        MPU6050_ParseTemp(&temp);

        return ret;
    }
    else
    {
        return ret;
    }
}

/**
 * @brief This function is used to enable/disable Gyroscope
 * 
 * @param en            Used as a flag forn disables/enable
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MPU6050_DisableGyro(bool en)
{
    int ret;
    uint8_t data;

    if(en)
    {
        ret = MPU6050_RegisterRead(MPU6050_PWR_MGMT_2, buffer, 1);
        if(!ret)
        {
            data = (buffer[0] & 0xF8) | 0x07; 
            ret = MPU6050_RegisterWriteByte(MPU6050_PWR_MGMT_2, data);
            
            return ret;
        }
        else
        {
            return ret;
        }
    }
    else
    {
        data = (buffer[0] & 0xF8) | 0x00;
        ret = MPU6050_RegisterWriteByte(MPU6050_PWR_MGMT_2, data);
        
        return ret;
    }
}

/**
 * @brief This function is used for wake up the device
 * 
 * @return esp_err_t    0 -> No error 
 */
static esp_err_t MPU6050_PwrMgmt1(uint8_t data)
{
    int ret;

    ret = MPU6050_RegisterWriteByte(MPU6050_PWR_MGMT_1, data);

    return ret;
}

/**
 * @brief This function is used to reset the signal path
 * 
 * @return esp_err_t 
 */
static esp_err_t MPU6050_SignalPathReset(void)
{
    int ret;

    ret = MPU6050_RegisterWriteByte(MPU6050_SIG_PATH_RST, 0x07);

    return ret;
}

/**
 * @brief Todavía no se 
 * 
 * @return esp_err_t 
 */
static esp_err_t MPU6050_Config(uint8_t data)
{
    int ret = MPU6050_RegisterWriteByte(MPU6050_CONFIG, data);

    return ret;
}

/**
 * @brief This function is used to congif the gyro
 * 
 * @return esp_err_t 
 */
static esp_err_t MPU6050_GyroConfig(uint8_t data)
{
    int ret;

    ret = MPU6050_RegisterWriteByte(MPU6050_GYRO_CONFIG, data);

    return ret;
}

static esp_err_t MPU6050_AccelConfig(uint8_t data)
{
    int ret;

    ret = MPU6050_RegisterWriteByte(MPU6050_ACCEL_CONFIG, data);

    return ret;
}

/**
 * @brief This function is used to initialize the MPU6050 device
 * 
 * @param dataRate      Data rate for accel
 * @param accelRange    Full scale for accel
 * @param gyroSens      Gyro sensitivity
 * @return esp_err_t    0 -> No error
 */
esp_err_t MPU6050_Init(uint8_t dataRate, uint8_t accelRange, uint8_t gyroSens)
{
    int ret;
    AccelerometerSensitivity = accelRange;
    GyroscopeSensitivity = gyroSens;

    ret = MPU6050_WhoAmI();
    ret = MPU6050_EnableInts(false);
    ret = MPU6050_PwrMgmt1(0x01);
    ret = MPU6050_SetDataRate(0x00);
    ret = MPU6050_Config(0x00);
    ret = MPU6050_GyroConfig(0x08);
    ret = MPU6050_AccelConfig(0x01);
    ret = MPU6050_SetIntPin();
    ret = MPU6050_SetMotionDetectParams(1, 47);
    ret = MPU6050_RegisterWriteByte(MPU6050_MOT_DETECT_CTRL, 0x11);
    ret = MPU6050_EnableInts(true);
    return ret;   
}

/**
 * @brief This function is used to get human readable accelerometer results
 * 
 */
static void MPU6050_ParseAccel(void)
{
    int i;

    switch(AccelerometerSensitivity)
    {
        case MPU6050_Accelerometer_2G:
            for(i = 0; i < 3; i++)
                (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_2);
            break;
        case MPU6050_Accelerometer_4G:
            for(i = 0; i < 3; i++)
                (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_4);
            break;
        case MPU6050_Accelerometer_8G:
            for(i = 0; i < 3; i++)
                (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_8);
            break;
        case MPU6050_Accelerometer_16G:
            for(i = 0; i < 3; i++)
                (accel[i]) = (float)((float)RawAccel[i] / MPU6050_AccelSens_16);
            break;
    }
}

/**
 * @brief This funtion is used to get human readable gyroscope results
 * 
 */
static void MPU6050_ParseGyro(float *gyro)
{
    int i;

    switch(GyroscopeSensitivity)
    {
        case MPU6050_Gyroscope_250s:
            for(i = 0; i < 3; i++)
                (gyro[i]) = (float)((float)RawGyro[i] / MPU6050_GyroSens_250);
            break;
        case MPU6050_Gyroscope_500s:
            for(i = 0; i < 3; i++)
                (gyro[i]) = (float)((float)RawGyro[i] / MPU6050_GyroSens_500);
            break;
        case MPU6050_Gyroscope_1000s:
            for(i = 0; i < 3; i++)
                (gyro[i]) = (float)((float)RawGyro[i] / MPU6050_GyroSens_1000);
            break;
        case MPU6050_Gyroscope_2000s:
            for(i = 0; i < 3; i++)
                (gyro[i]) = (float)((float)RawGyro[i] / MPU6050_GyroSens_2000);
            break;
    }
}

/**
 * @brief This function is used to get human readable temperature results
 * 
 */
static void MPU6050_ParseTemp(float *temp)
{
    *(temp) = (float)((RawTemp / 340.0) +36.53);
}

esp_err_t MPU6050_ReadMotionStatus(void)
{
    int ret;

    ret = MPU6050_RegisterRead(MPU6050_INT_STATUS, buffer, 1);

    return ret;
}