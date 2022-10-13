
/**
 * @file mlx90614.c
 * @author Fernando Galassi
 * @brief This file contains functions and methods to control MLX90614
 * @version 0.1
 * @date 2022-10-13
 * 
 * @copyright SMR Copyright (c) 2022
 * 
 */

#include <stdio.h>
#include <stddef.h>
#include <math.h>

#include "esp_system.h"
#include "esp_log.h"
#include "driver/i2c.h"

#include "mlx90614.h"

/* Global Variables */
static const char *TAG = "SMR Sensors";

/* Private functions Prototypes */
static esp_err_t MLX90614_SendCommand(uint8_t command);
static esp_err_t MLX90614_DumpEE(uint16_t *eeData);
static esp_err_t MLX90614_Write(uint8_t writeAddress, uint16_t data);
static esp_err_t MLX90614_Read(uint8_t reg_addr, uint16_t *data);
static uint8_t Calculate_PEC (uint8_t initPEC, uint8_t newData);


/**
 * @brief This function is used to send commands to th MLX60914 sensor
 * 
 * @param command       The command to be send 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MLX90614_SendCommand(uint8_t command)
{
    uint8_t chip_addr;
    uint8_t send_data[2]= {0,0};
    uint8_t pec;
    int ret;
    
    if(command != 0x60 && command != 0x61)
        return -5;
             
    chip_addr = (MLX90614_ADDRESS << 1);
    send_data[0] = command;
        
    pec = Calculate_PEC(0, chip_addr);
    pec = Calculate_PEC(pec, send_data[0]);
       
    send_data[1] = pec;
    
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, chip_addr | WRITE_BIT, ACK_CHECK_EN);
    
    for (int i = 0; i < 2; i++) 
        i2c_master_write_byte(cmd, send_data[i], ACK_CHECK_EN);
    
    i2c_master_stop(cmd);
    
    ret = i2c_master_cmd_begin(I2C_NUM_0, cmd, 100);

    i2c_cmd_link_delete(cmd);

    if (ret == ESP_OK)
    { 
        ESP_LOGI(TAG, "Write OK");
    }
    else if (ret == ESP_ERR_TIMEOUT)
    {
        ESP_LOGI(TAG, "Bus is busy");
        return ret;
    }
    else 
    {
        ESP_LOGW(TAG, "Write Failed");
        return ret;
    }
        
    return ret;
}    

/**
 * @brief This function is used to calculate the Packet Error Code
 * 
 * @param initPEC 
 * @param newData 
 * @return uint8_t The calculated PEC
 */
static uint8_t Calculate_PEC (uint8_t initPEC, uint8_t newData)
{
    uint8_t data;
    uint8_t bitCheck;

    data = initPEC ^ newData;
    
    for (int i = 0; i < 8; i++)
    {
        bitCheck = data & 0x80;
        data = data << 1;
        
        if (bitCheck != 0)
        {
            data = data ^ 0x07;
        }
        
    }

    return data;
}

/**
 * @brief This function is used to perfrom a write sequence to the MLX9014 sensor
 * 
 * @param writeAddress  Address to be write
 * @param data          Data to be write
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MLX90614_Write(uint8_t writeAddress, uint16_t data)
{
    uint8_t chip_addr;
    uint8_t send_data[4] = {0,0,0,0};
    static uint16_t dataCheck;
    uint8_t pec;
    esp_err_t ret;
    
    chip_addr = (MLX90614_ADDRESS << 1);
    send_data[0] = writeAddress;
    send_data[1] = data & 0x00FF;
    send_data[2] = data >> 8;
    
    pec = Calculate_PEC(0, chip_addr);
    pec = Calculate_PEC(pec, send_data[0]);
    pec = Calculate_PEC(pec, send_data[1]);
    pec = Calculate_PEC(pec, send_data[2]);
    
    send_data[3] = pec;

    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, chip_addr | WRITE_BIT, ACK_CHECK_EN);

    for (int i = 0; i < 3; i++) 
        i2c_master_write_byte(cmd, send_data[i], ACK_CHECK_EN);
    
    i2c_master_stop(cmd);

    ret = i2c_master_cmd_begin(I2C_NUM_0, cmd, 100);
    
    i2c_cmd_link_delete(cmd);
    
    if (ret == ESP_OK)
    {
        ESP_LOGI(TAG, "Write OK");
    }
    
    else if (ret == ESP_ERR_TIMEOUT)
    {
        ESP_LOGI(TAG, "Bus is busy");
        return ret;
    }
    
    else 
    {
        ESP_LOGI(TAG, "Write Failed");
        return ret;
    }
           
    
    ret = MLX90614_Read(writeAddress, &dataCheck);
    
    if ( dataCheck != data)
    {
        return -3;
    }    
    
    return ret;
}

/**
 * @brief This function is used to perform a read sequence to the MLX90614
 * 
 * @param reg_addr 
 * @param data 
 * @return esp_err_t 
 */
static esp_err_t MLX90614_Read(uint8_t reg_addr, uint16_t *data)
{
    uint8_t chip_addr; 
    uint8_t data_addr;                          
    uint8_t pec;                               
    uint16_t *p;

    p = data;
    chip_addr = (MLX90614_ADDRESS << 1);
    data_addr = reg_addr;
    pec = chip_addr;
    uint8_t recived_data[3] = {0,0,0};

    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, chip_addr | WRITE_BIT, ACK_CHECK_EN);
    i2c_master_write_byte(cmd, data_addr, ACK_CHECK_EN);
    i2c_master_start(cmd);
    chip_addr = chip_addr | 0x01;
    i2c_master_write_byte(cmd, chip_addr | READ_BIT, ACK_CHECK_EN);
    i2c_master_read(cmd, recived_data, 2, ACK_VAL);
    i2c_master_read_byte(cmd, recived_data + 2, NACK_VAL);       
    i2c_master_stop(cmd);  
    esp_err_t ret = i2c_master_cmd_begin(I2C_NUM_0, cmd, 100);
    i2c_cmd_link_delete(cmd);
    if (ret == ESP_OK) {
        pec = Calculate_PEC(0, pec);
        pec = Calculate_PEC(pec, data_addr);
        pec = Calculate_PEC(pec, chip_addr);
        pec = Calculate_PEC(pec, recived_data[0]);
        pec = Calculate_PEC(pec, recived_data[1]);
    } else if (ret == ESP_ERR_TIMEOUT) {
        ESP_LOGW(TAG, "Bus is busy");
    } else {
        ESP_LOGW(TAG, "Read failed");
    }
    if (pec != recived_data[2])
    {
        return -2;
    }
        
    *p = (uint16_t)recived_data[1]*256 + (uint16_t)recived_data[0];
    return 0;   
}

/**
 * @brief This function is used to dump the EEPROM
 * 
 * @param eeData 
 * @return esp_err_t    0 -> No error
 */
static esp_err_t MLX90614_DumpEE(uint16_t *eeData)
{
     int error = 0;
     char address = 0x20;
     uint16_t *p = eeData;
     
     while (address < 0x40 && error == 0)
     {
        error = MLX90614_Read(address, p);
        address = address + 1;
        p = p + 1;
     }   
         
     return error;
}

/**
 * @brief This function is used to get the room temperature
 * 
 * @param ta            Placeholder for room temperature.
 * @return esp_err_t    0 -> No error.
 */
esp_err_t MLX90614_GetTa(float *ta)
{
    int error = 0;
    uint16_t data = 0;
    
    error = MLX90614_Read(0x06, &data);
    
    if (data > 0x7FFF)
    {
        return -4;
    }
        
    *ta = (float)data * 0.02f - 273.15;
        
    return error;
}    

/**
 * @brief This function is used to get the target's temperature
 * 
 * @param to            Placeholder for target's temperature
 * @return esp_err_t    0 -> No error.
 */
esp_err_t MLX90614_GetTo(float *to)
{
    int error = 0;
    uint16_t data = 0;
    
    error = MLX90614_Read(0x07, &data);
    
    if (data > 0x7FFF)
    {
        return -4;
    }
    
    if (error == 0)
    {
        *to = (float)data * 0.02f - 273.15;
    } 
    
    return error;
} 
