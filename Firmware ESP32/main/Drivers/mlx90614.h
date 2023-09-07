/**
 * @file mlx90614.h
 * @author Fernando Galassi
 * @brief  Header file for mlx90614.c
 * @version 0.1
 * @date 2022-10-13
 * 
 * @copyright SMR Copyright (c) 2022
 * 
 */

#ifndef _MLX90614_H_
#define _MLX90614_H_

#include "esp_system.h"

#define MLX90614_ADDRESS    0x5A

#define WRITE_BIT           I2C_MASTER_WRITE  
#define READ_BIT            I2C_MASTER_READ   

#define ACK_CHECK_EN        0x01    
#define ACK_CHECK_DIS       0x00    
#define ACK_VAL             0x00    
#define NACK_VAL            0x01    



/* Public Functions Prototypes  */
esp_err_t MLX90614_GetTa(float *ta);
esp_err_t MLX90614_GetTo(float *to);
esp_err_t MLX90614_GetTo2(float *to2);


#endif
