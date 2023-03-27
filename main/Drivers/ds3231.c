
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

esp_err_t ds3231_set_time()
{
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
    esp_err_t ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);
    if (ret != ESP_OK) {
        printf("Error setting time\n");
    }
    else {
        printf("Time set successfully\n");
    }

    int seconds = bcd2dec(buffer[1]);
    int minutes = bcd2dec(buffer[2]);
    int hours = bcd2dec(buffer[3]);
    int day = buffer[4];
    int date = bcd2dec(buffer[5]);
    int month = bcd2dec(buffer[6]);
    int year = bcd2dec(buffer[7]) + 2000;

    
    printf("----------------------------------\n");
    printf("FECHA Y HORA POR DEFECTO\n");
    printf("Horario: %02d:%02d:%02d\n", hours, minutes, seconds);
    printf("Fecha: %02d/%02d/%02d\n", date, month, year);
    printf("----------------------------------\n");

    return ESP_OK;
}

esp_err_t ds3231_get_time(uint8_t *time)
{
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();

    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, DS3231_ADDR << 1 | I2C_MASTER_WRITE, true);
    i2c_master_write_byte(cmd, DS3231_REG_TIME, true);
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, DS3231_ADDR << 1 | I2C_MASTER_READ, true);
    i2c_master_read(cmd, time, 7, I2C_MASTER_LAST_NACK);
    i2c_master_stop(cmd);
    esp_err_t ret = i2c_master_cmd_begin(I2C_MASTER_NUM, cmd, 1000 / portTICK_PERIOD_MS);
    i2c_cmd_link_delete(cmd);
    if (ret != ESP_OK) {
        printf("Error reading from DS3231: %d\n", ret);
    }

    return ESP_OK;
}




