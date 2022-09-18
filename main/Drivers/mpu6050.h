/**
 * @file mpu6050.h
 * @author Fernando Galassi
 * @brief Header file for mpu6050.c
 * @version 0.1
 * @date 2022-09-03
 * 
 * @copyright SMR Copyright (c) 2022
 * 
 */

#ifndef _MPU6050_H_
#define _MPU6050_H_

/* Libraries include*/
#include <stdio.h>
#include <stddef.h>

/* Registers Defines */
#define MPU6050_I2C_ADDR        0x68

#define MPU6050_AUX_VDDIO       0x00
#define MPU6050_YG_OFFS_TC      0x01
#define MPU6050_ZG_OFFS_TC      0x02
#define MPU6050_X_FINE_GAIN     0x03
#define MPU6050_Y_FINE_GAIN     0x04
#define MPU6050_Z_FINE_GAIN     0x05
#define MPU6050_XA_OFFS_H       0x06
#define MPU6050_XA_OFFS_L_TC    0x07
#define MPU6050_YA_OFFS_H       0x08
#define MPU6050_YA_OFFS_L_TC    0x09
#define MPU6050_ZA_OFFS_H       0x0A
#define MPU6050_ZA_OFFS_L_TC    0x0B

#define MPU6050_XG_OFFS_USRH        0x13
#define MPU6050_XG_OFFS_USRL        0x14
#define MPU6050_YG_OFFS_USRH        0x15
#define MPU6050_YG_OFFS_USRL        0x16
#define MPU6050_ZG_OFFS_USRH        0x17
#define MPU6050_ZG_OFFS_USRL        0x18
#define MPU6050_SMPLRT_DIV          0x19
#define MPU6050_CONFIG              0x1A
#define MPU6050_GYRO_CONFIG         0x1B
#define MPU6050_ACCEL_CONFIG        0x1C
#define MPU6050_FF_THR              0x1D
#define MPU6050_FF_DUR              0x1E
#define MPU6050_MOT_THR             0x1F
#define MPU6050_MOT_DUR             0x20
#define MPU6050_ZRMOT_THR           0x21
#define MPU6050_ZRMOT_DUR           0x22
#define MPU6050_FIFO_EN             0x23
#define MPU6050_MOT_DETECT_STATUS   0x61
#define MPU6050_MOT_DETECT_CTRL     0x69

#define MPU6050_INT_PIN_CFG     0x37
#define MPU6050_INT_ENABLE      0x38
#define MPU6050_DMP_INT_STATUS  0x39
#define MPU6050_INT_STATUS      0x3A

#define MPU6050_ACCEL_XOUT_H    0x3B
#define MPU6050_ACCEL_XOUT_L    0x3C
#define MPU6050_ACCEL_YOUT_H    0x3D
#define MPU6050_ACCEL_YOUT_L    0x3E
#define MPU6050_ACCEL_ZOUT_H    0x3F
#define MPU6050_ACCEL_ZOUT_L    0x40

#define MPU6050_TEMP_OUT_H      0x41
#define MPU6050_TEMP_OUT_L      0x42

#define MPU6050_GYRO_XOUT_H     0x43
#define MPU6050_GYRO_XOUT_L     0x44
#define MPU6050_GYRO_YOUT_H     0x45
#define MPU6050_GYRO_YOUT_L     0x46
#define MPU6050_GYRO_ZOUT_H     0x47
#define MPU6050_GYRO_ZOUT_L     0x48

#define MPU6050_SIG_PATH_RST	0x68
#define MPU6050_USR_CTRL        0x6A
#define MPU6050_PWR_MGMT_1      0x6B
#define MPU6050_PWR_MGMT_2      0x6C
#define MPU6050_BANK_SEL        0x6D
#define MPU6050_MEM_START_ADDR  0x6E
#define MPU6050_MEM_R_W         0x6F
#define MPU6050_DMP_CFG_1       0x70
#define MPU6050_DMP_CFG_2       0x71
#define MPU6050_FIFO_COUNTH     0x72
#define MPU6050_FIFO_COUNTL     0x73
#define MPU6050_FIFO_R_W        0x74
#define MPU6050_WHO_AM_I        0x75

/* Usefull defines */
#define MPU6050_DataRate_8KHz   0   /*!< Sample rate set to 8 kHz */
#define MPU6050_DataRate_4KHz   1   /*!< Sample rate set to 4 kHz */
#define MPU6050_DataRate_2KHz   3   /*!< Sample rate set to 2 kHz */
#define MPU6050_DataRate_1KHz   7   /*!< Sample rate set to 1 kHz */
#define MPU6050_DataRate_500Hz  15  /*!< Sample rate set to 500 Hz */
#define MPU6050_DataRate_250Hz  31  /*!< Sample rate set to 250 Hz */
#define MPU6050_DataRate_125Hz  63  /*!< Sample rate set to 125 Hz */
#define MPU6050_DataRate_100Hz  79  /*!< Sample rate set to 100 Hz */

/* Gyro sensitivities in degrees/s */
#define MPU6050_GyroSens_250		((float) 131)
#define MPU6050_GyroSens_500		((float) 65.5)
#define MPU6050_GyroSens_1000		((float) 32.8)
#define MPU6050_GyroSens_2000		((float) 16.4)

/* Accel sensitivities in g/s */
#define MPU6050_AccelSens_2			((float) 16384)
#define MPU6050_AccelSens_4			((float) 8192)
#define MPU6050_AccelSens_8			((float) 4096)
#define MPU6050_AccelSens_16		((float) 2048)

/* Public Function prototypes */
esp_err_t MPU6050_ReadInterrupts(void);
esp_err_t MPU6050_ReadAccelerometer(void);
esp_err_t MPU6050_ReadGyroscope(void);
esp_err_t MPU6050_ReadTemperature(void);
esp_err_t MPU6050_Init(uint8_t dataRate, uint8_t accelRange, uint8_t gyroSens);
esp_err_t MPU6050_ReadMotionStatus(void);

/* Typedef */
typedef enum MPU6050_Accelerometer_e
{
    MPU6050_Accelerometer_2G = 0x00,
	MPU6050_Accelerometer_4G = 0x01,
	MPU6050_Accelerometer_8G = 0x02,
	MPU6050_Accelerometer_16G = 0x03
} MPU6050_Accelerometer_t;

typedef enum MPU6050_Gyroscope_e 
{
	MPU6050_Gyroscope_250s = 0x00, 
	MPU6050_Gyroscope_500s = 0x01, 
	MPU6050_Gyroscope_1000s = 0x02,
	MPU6050_Gyroscope_2000s = 0x03 
} MPU6050_Gyroscope_t;

#endif