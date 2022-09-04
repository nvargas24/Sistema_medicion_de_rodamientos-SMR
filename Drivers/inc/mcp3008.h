/**
 * @file mcp3008.h
 * @author Team SMR
 * @authors Galassi, Fernando
 * @authors Moran, Nicolas
 * @authors	Pilato, Bruno
 * @authors	Vargas, Nahuel
 *
 * @brief 
 * @version 0.1
 * @date 2022-08-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */
 
/********************************* Heaters *************************************/
#include "driver/gpio.h"
#include "driver/spi_master.h"

/************************** Macros y definiciones ******************************/
#define CS_PIN 5
#define CLK_PIN 18
#define MISO_PIN 19
#define MOSI_PIN 23

/******************** Definiciones de funciones externas **********************/
void mcpInit(void);
int16_t mcpRead(int16_t channel);