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
 


#define MAX_CHANNEL 8


int16_t MCP3008_ReadChannel(int16_t channel);