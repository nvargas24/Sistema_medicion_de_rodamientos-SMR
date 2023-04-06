/**
 * @file ds3231.h
 * @author Nahuel Vargas
 * @brief  Header file for DS3231.c
 * @version 0.1
 * @date 2023-3-23
 * 
 * @copyright SMR Copyright (c) 2022
 * 
 */

#ifndef _DS3231_H_
#define _DS3231_H_

/* Libraries include*/
#include <stdio.h>
#include <stddef.h>
#include "esp_system.h"

/* Registers Defines */
#define DS3231_ADDR                 0x68 /*!< slave address for DS3231 sensor */
#define DS3231_REG_TIME             0x00 /*!< register address for time */

#define DS3231_CONTROL_REGISTER			0x0E
#define DS3231_STATUS_REGISTER			0x0F
#define DS3231_AGING_OFFSET_REGISTER	0x10
#define DS3231_TEMP_MSB_REGISTER		0x11
#define DS3231_TEMP_LSB_REGISTER		0x12

/* Data Registers */
#define DS3231_SECONDS_REGISTER		0x00	/* Range 0-59 */
#define DS3231_MINUTES_RGISTER		0x01	/* Range 0-59 */
#define DS3231_HOURS_REGISTER		0x02	/* Range 0-23 */
#define DS3231_DAY_REGISTER			0x03	/* Range 1-7 */
#define DS3231_DATE_REGISTER		0x04	/* Range 1-31 */
#define DS3231_MONTH_REGISTER		0x05	/* Range 1-12 */
#define DS3231_YEAR_REGISTER		0x06	/* Range 0-99 */

/* Usefull defines */
#define ACK_CHECK_EN        0x01    
#define ACK_CHECK_DIS       0x00    
#define ACK_VAL             0x00    
#define NACK_VAL            0x01    
#define I2C_MASTER_NUM      I2C_NUM_0

/* Public Function prototypes */
esp_err_t DS3231_SetTime();
esp_err_t DS3231_GetTime(uint8_t *time);
esp_err_t DS3231_GetTimeStamp(char *timestamp);

/* Private Function Prototypes */

/* Typedef */

#endif

