
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

static uint8_t bcd2dec(uint8_t val)
{
    return (val >> 4) * 10 + (val & 0x0F);
}

static uint8_t dec2bcd(uint8_t val)
{
    return ((val/10) << 4) + (val %10);
}

esp_err_t DS3231_SetTime()
{
    esp_err_t ret;
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    uint8_t buffer[8];
    buffer[0] = 0x00; // Starting register address for time

    // Set default time and date values
    buffer[1] = 0x00; // Segundos
    buffer[2] = 0x02; // Minutos
    buffer[3] = 0x22; // Horas (24hs)
    buffer[4] = 0x07; // Dia de la semana
    buffer[5] = 0x26; // Dia
    buffer[6] = 0x03; // Mes
    buffer[7] = 0x23; // Anio(20YY)

    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, DS3231_ADDR << 1 | I2C_MASTER_WRITE, true);
    i2c_master_write(cmd, buffer, sizeof(buffer), true);
    i2c_master_stop(cmd);

    ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);

    int seconds = bcd2dec(buffer[1]);
    int minutes = bcd2dec(buffer[2]);
    int hours = bcd2dec(buffer[3]);
    int day = buffer[4];
    int date = bcd2dec(buffer[5]);
    int month = bcd2dec(buffer[6]);
    int year = bcd2dec(buffer[7]) + 2000;

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




