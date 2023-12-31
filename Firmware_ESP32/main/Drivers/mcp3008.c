/**
 * @file mcp3008.c
 * @author 
 * @brief 
 * @version 0.2
 * @date 2023-3-13
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
#include "main.h"

/* Global Variables */
static const char *TAG = "SMR Sensors";
spi_device_handle_t spi3;

esp_err_t MCP3008_Init(void)
{
    esp_err_t ret;

    spi_device_interface_config_t devcfg = 
    {
        .clock_speed_hz = SPI_MASTER_FREQ_20M , // config lectura de ADC si >20MHz
        .mode = 0,
        .spics_io_num = SPI_CS_PIN,
        .queue_size = 1,
        .flags = SPI_DEVICE_NO_DUMMY ,
    };

    return spi_bus_add_device(SPI3_HOST, &devcfg, &spi3);   
}


/**
 * @brief 
 * 
 * @param channel 
 * @return int16_t 
 */
esp_err_t MCP3008_ReadChannel(int16_t channel, int16_t *meas_mcp)
{
    esp_err_t ret;
    unsigned char rbuf[3];
    unsigned char wbuf[3];

    spi_transaction_t SPITransaction;    

    if (channel > MAX_CHANNEL) {
		ESP_LOGE(TAG, "Illegal channel %d", channel);
		return 0;
	}

    memset(wbuf, 0, sizeof(rbuf));
    memset(rbuf, 0, sizeof(rbuf));
    memset(&SPITransaction, 0, sizeof(spi_transaction_t));
    
    wbuf[0] = 0x60 | channel << 2;

    SPITransaction.length = 24;
    SPITransaction.tx_buffer = wbuf;
    SPITransaction.rx_buffer = rbuf;

    // Se captura error si no hay comunicacion con el MCP3008
    ret = spi_device_transmit( spi3, &SPITransaction );

    //val = (rbuf[1]<<2) + (rbuf[2]>>6); 
    *meas_mcp = (rbuf[1]<<3) + (rbuf[2]>>5); // Solo para frecuencia de CLK=20MHz.

    return ret;
}


