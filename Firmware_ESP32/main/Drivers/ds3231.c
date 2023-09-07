
/**
 * @file ds3231.c
 * @author Nahuel Vargas
 * @brief This file contains functions and methods to control DS3231
 * @version 0.1
 * @date 2023-3-23
 * 
 * @copyright SMR Copyright (c) 2022
 * 
 */

#include <stdio.h>
#include <stddef.h>

#include "esp_system.h"
#include "esp_log.h"
#include "driver/i2c.h"
#include "time.h"

#include "ds3231.h"
#include "main.h"

static uint8_t bcd2dec(uint8_t val)
{
    return (val >> 4) * 10 + (val & 0x0F);
}

static uint8_t dec2bcd(uint8_t val)
{
    return ((val/10) << 4) + (val %10);
}

esp_err_t DS3231_SetTime(uint8_t *buffer)
{
    esp_err_t ret;
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();  

    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, DS3231_ADDR << 1 | I2C_MASTER_WRITE, true);
    i2c_master_write(cmd, buffer, sizeof(buffer), true);
    i2c_master_stop(cmd);

    ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);

    return ret;
}

esp_err_t DS3231_GetTime(uint8_t *time)
{
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    esp_err_t ret;

    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, DS3231_ADDR << 1 | I2C_MASTER_WRITE, true);
    i2c_master_write_byte(cmd, DS3231_REG_TIME, true);
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, DS3231_ADDR << 1 | I2C_MASTER_READ, true);
    i2c_master_read(cmd, time, 7, I2C_MASTER_LAST_NACK);
    i2c_master_stop(cmd);
    
    ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);
    
    return ret;
}

int days_in_month[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int is_leap_year(int year)
{
    return (year%4 == 0 && (year%100 != 0 || year%400 == 0));
}


uint8_t hexToDecimal(uint8_t hexValue)
{   
    uint8_t decimalValue = ((hexValue >>4)*10) + (hexValue & 0x0F);
    return decimalValue;
}

esp_err_t DS3231_GetTimeStamp(char *timestamp)
{
    esp_err_t ret;
    uint8_t time[7];
    int timestamp_segs = 0;
    

    ret = DS3231_GetTime(&time);
    if(ret == ESP_OK)
    {
        
        int total_days = 0;

        for(int year=2000; year<hexToDecimal(time[6]) + 1900; year++)
        {
            total_days += is_leap_year(year) ? 366:365;
        }

        for(int month = 0; month <hexToDecimal(time[5])-1; month++)
        {
            total_days += days_in_month[month];
            if(month ==1 && is_leap_year(hexToDecimal(time[6])+ 1900))
            {
                total_days++;
            }
        }
        total_days += hexToDecimal(time[4])-1;

        timestamp_segs = total_days * 86400 + hexToDecimal(time[2])*3600 + hexToDecimal(time[1])*60 + hexToDecimal(time[0]);
        timestamp_segs =hexToDecimal(time[2])*3600 + hexToDecimal(time[1])*60 + hexToDecimal(time[0]);
        
        sprintf(timestamp, "%06d", timestamp_segs);
    }

    //printf("timeStamp: %d\n", timestamp_segs);
    //printf("timeStamp: %s\n", timestamp);

    return ret;
}




