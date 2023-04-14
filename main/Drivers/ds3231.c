
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

esp_err_t DS3231_GetTimeStamp(char *timestamp)
{
    esp_err_t ret;
    uint8_t time[7];

    ret = DS3231_GetTime(&time);
    if(ret == ESP_OK)
    {
        /* AA_MM_DD_HH_MM_SS */
        sprintf(timestamp, "%d%d%d_%d%d%d", time[7], time[6], time[5], time[3], time[2],time[1]);
    }

    return ret;
}




