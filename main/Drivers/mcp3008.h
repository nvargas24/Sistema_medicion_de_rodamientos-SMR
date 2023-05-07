/**
 * @file mcp3008.h
 * 
 * @author Team SMR
 * @authors Galassi, Fernando
 * @authors Moran, Nicolas
 * @authors	Pilato, Bruno
 * @authors	Vargas, Nahuel
 *
 * @brief Header file for mcp3008.c
 * @version 0.1
 * @date 2022-08-30
 * 
 * @copyright SMR Copyright (c) 2022
 * 
 */
 

#ifndef __MCP3008_H__
#define __MCP3008_H__

#include <stdio.h>
#include <stddef.h>
#include "esp_system.h"

#define MAX_CHANNEL 8


esp_err_t MCP3008_ReadChannel(int16_t channel, int16_t *meas_mcp);
esp_err_t MCP3008_Init(void);

#endif // __FFT_H__