/**
 * @file mcp3008.c
 * @author 
 * @brief 
 * @version 0.1
 * @date 2022-10-13
 * 
 * @copyright 
 * 
 */
#include <stdio.h>
#include <string.h>

#include "esp_log.h"
#include "esp_err.h"
#include "driver/gpio.h"
#include "driver/spi_master.h"

#include "mcp3008.h"

/* Global Variables */
spi_device_handle_t spi2;
static const char *TAG = "SMR Sensors";


/**
 * @brief 
 * 
 * @param channel 
 * @return int16_t 
 */
int16_t MCP3008_ReadChannel(int16_t channel)
{
    int ret;
    char rbuf[3];
    char wbuf[3];
    int16_t val = 0;

    if (channel > MAX_CHANNEL) {
		ESP_LOGE(TAG, "Illegal channel %d", channel);
		return 0;
	}

    memset(wbuf, 0, sizeof(rbuf));
    memset(rbuf, 0, sizeof(rbuf));

    wbuf[0] = 0x60 | channel << 2;

    ESP_LOGD(TAG, "wbuf=0x%02X 0x%02X", wbuf[0], wbuf[1]);
    
    spi_transaction_t SPITransaction;
    
    memset(&SPITransaction, 0, sizeof(spi_transaction_t));
    SPITransaction.length = 3*8;
    SPITransaction.tx_buffer = wbuf;
    SPITransaction.rx_buffer = rbuf;

    ret = spi_device_transmit( spi2, &SPITransaction );

	assert(ret==ESP_OK); 
	ESP_LOGD(TAG, "rbuf[0]=%02X rbuf[1]=%02X rbuf[2]=%02X", rbuf[0], rbuf[1], rbuf[2]);
    
    val = (rbuf[1]<<2) + (rbuf[2]>>6);
    //val = (rbuf[1]&3 << 8)+ rbuf[2];

    ESP_LOGD(TAG, "val= %02x", val);
    return val;
}

