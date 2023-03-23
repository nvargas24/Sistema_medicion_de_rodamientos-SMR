
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

#include "ds3231.h"


static uint8_t dec2bcd()
{
    return ((val/10) << 4) + (val %10);
}

void ds3231_set_time(struct tm *time)
{
    uint8_t data[7];

    data[0] = dec2bcd(time->tm_sec);
    data[1] = dec2bcd(time->tm_min);
    data[2] = dec2bcd(time->tm_hour);
    data[3] = dec2bcd(time->tm_wday +1);
    data[4] = dec2bcd(time->tm_mday);
    data[5] = dec2bcd(time->tm_mon +1);
    data[6] = dec2bcd(time->tm_year -100);

    chip_addr = (DS3231_aDDRESS <<1);

    /*revisar*/
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, chip_addr | I2C_MASTER_WRITE, ACK_CHECK_EN);
    
    for (int i = 0; i < 2; i++) 
        i2c_master_write_byte(cmd, send_data[i], ACK_CHECK_EN);
    
    i2c_master_stop(cmd);
    
    ret = i2c_master_cmd_begin(I2C_NUM_0, cmd, 100);

    i2c_cmd_link_delete(cmd);

}






