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
#include "mpu6050.h"

/* Global variables */
uint8_t **ptr_buffer;
uint8_t buffer[6];

int16_t accel[3];
int16_t gyro[3];
int16_t temp;

MPU6050_Accelerometer_t AccelerometerSensitivity;
MPU6050_Gyroscope_t GyroscopeSensitivity;

/**
 * @brief This funtion is used to share the placeholder for the I2C transactions.
 *        
 * @param buff  Communication buffer
 */
void MPU6050_GetBuffer(uint8_t **buff)
{
    *buff = buffer;
}

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
    return i2c_master_write_read_device(I2C_MASTER_NUM, MPU6050_I2C_ADDR, &reg_addr, 1, data, len, I2C_MASTER_TIMEOUT_MS / portTICK_RATE_MS);
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

    ret = i2c_master_write_to_device(I2C_MASTER_NUM, MPU6050_I2C_ADDR, write_buf, sizeof(write_buf), I2C_MASTER_TIMEOUT_MS / portTICK_RATE_MS);

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
static esp_err_t MPU6050_SetAccelerometer(void)
{
    int ret;
    uint8_t data;

    ret = MPU6050_RegisterRead(MPU6050_ACCEL_CONFIG, buffer, 1);
    if(!ret)
    {
        data = (buffer[0] & 0xE7) | (uint8_t)AccelerometerSensitivity << 3;
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
static esp_err_t MPU6050_SetGyroscope(void)
{
    int ret;
    uint8_t data;

    ret = MPU6050_RegisterRead(MPU6050_GYRO_CONFIG, buffer, 1);
    if(!ret)
    {
        data = (buffer[0] & 0xE7) | (uint8_t)GyroscopeSensitivity << 3;
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
    uint8_t data = 0x80; /* Low level . Push-Pull */

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
esp_err_t MPU6050_ReadAccelerometer(void)
{
    int ret;
    int i;

    ret = MPU6050_RegisterRead(MPU6050_ACCEL_XOUT_H, buffer, 6);
    if(!ret)
    {
        for(i = 0; i < 3; i++)
            accel[i] = (int16_t)(buffer[i] << 8 | buffer[i+1]);

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
esp_err_t MPU6050_ReadGyroscope(void)
{
    int ret;
    int i;

    ret = MPU6050_RegisterRead(MPU6050_GYRO_XOUT_H, buffer, 6);
    if(!ret)
    {
        for(i = 0; i < 3; i++)
            gyro[i] = (int16_t)(buffer[i] << 8 | buffer[i+1]);

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
esp_err_t MPU6050_ReadTemperature(void)
{
    int ret;

    ret = MPU6050_RegisterRead(MPU6050_TEMP_OUT_H, buffer, 2);
    if(!ret)
    {
        temp = (int16_t)(buffer[0] << 8 | buffer[1]);

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
static esp_err_t MPU6050_WakeUp(void)
{
    int ret;

    ret = MPU6050_RegisterWriteByte(MPU6050_PWR_MGMT_1, 0x00);

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
   if(ret)
   {
        return ret;
   }
   else
   {
        /* Wake-up device */
        ret = MPU6050_WakeUp();
        if(ret)
        {
            return ret;
        }
        else
        {
            /* Set sample rate */
            ret = MPU6050_SetDataRate(dataRate);
            if(ret)
            {
                return ret;
            }
            else
            {
                /* Set Accelerometer sensitivity */
                ret = MPU6050_SetAccelerometer();
                if(ret)
                {
                    return ret;
                }
                else
                {
                    /* Set Gyro Sensitivity */
                    ret = MPU6050_SetGyroscope();

                    return ret;
                }
            }
        }
   }
}
