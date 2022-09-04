#include <stdio.h>
#include <string.h>
#include "esp_log.h"
#include "esp_err.h"
#include "driver/gpio.h"
#include "driver/spi_master.h"
#include "mcp3008.h"

#define MAX_CHANNEL 8

spi_device_handle_t spi2;
static const char* tag = "MyModule";
esp_err_t ret;

static void spi_init(void);
void mcpInit(void);

//static const char* tag = "MyModule";


static void spi_init(){
  

    spi_bus_config_t buscfg ={
        .miso_io_num = MISO_PIN,
        .mosi_io_num = MOSI_PIN,
        .sclk_io_num = CLK_PIN,
        .quadwp_io_num = -1,
        .quadhd_io_num = -1,
        //.max_transfer_sz = 32,
    };

    ret = spi_bus_initialize(SPI2_HOST, &buscfg, SPI_DMA_CH_AUTO);
    ESP_LOGD(tag, "spi_bus_initialize=%d",ret);
    assert(ret == ESP_OK);

    spi_device_interface_config_t devcfg={
        .clock_speed_hz = SPI_MASTER_FREQ_11M ,
        .mode = 0,
        .spics_io_num = CS_PIN,
        .queue_size = 1,
        .flags = SPI_DEVICE_NO_DUMMY ,
        //.flags = SPI_DEVICE_HALFDUPLEX,
        //.pre_cb = NULL,
        //.post_cb = NULL,
    };

    ESP_ERROR_CHECK(spi_bus_add_device(SPI2_HOST, &devcfg, &spi2));

    ret = spi_bus_add_device(SPI2_HOST, &devcfg, &spi2);
	ESP_LOGD(tag, "spi_bus_add_device=%d",ret);
	assert(ret==ESP_OK);

}

void mcpInit(void)
{
    //esp_err_t ret;
    ESP_LOGI(tag, "GPIO_CS = %d", CS_PIN);
    ESP_LOGI(tag, "GPIO_MOSI = %d", MOSI_PIN);
    ESP_LOGI(tag, "GPIO_MISO = %d", MISO_PIN);
    ESP_LOGI(tag, "GPIO_CLK = %d", CLK_PIN);

    gpio_reset_pin(CS_PIN);
    gpio_set_direction(CS_PIN, GPIO_MODE_OUTPUT);
    gpio_set_level(CS_PIN, 1);

    spi_init();
}

int16_t mcpRead(int16_t channel)
{
    char rbuf[3];
    char wbuf[3];
    int16_t val = 0;

    if (channel > MAX_CHANNEL) {
		ESP_LOGE(tag, "Illegal channel %d", channel);
		return 0;
	}

    memset(wbuf, 0, sizeof(rbuf));
    memset(rbuf, 0, sizeof(rbuf));

    wbuf[0] = 0x60 | channel << 2;

    ESP_LOGD(tag, "wbuf=0x%02X 0x%02X", wbuf[0], wbuf[1]);
    spi_transaction_t SPITransaction;
    
    memset(&SPITransaction, 0, sizeof(spi_transaction_t));
    SPITransaction.length = 3*8;
    SPITransaction.tx_buffer = wbuf;
    SPITransaction.rx_buffer = rbuf;

    ret = spi_device_transmit( spi2, &SPITransaction );

	assert(ret==ESP_OK); 
	ESP_LOGD(tag, "rbuf[0]=%02X rbuf[1]=%02X rbuf[2]=%02X", rbuf[0], rbuf[1], rbuf[2]);
    
    val = (rbuf[1]<<2) + (rbuf[2]>>6);
    //val = (rbuf[1]&3 << 8)+ rbuf[2];

    ESP_LOGD(tag, "val= %02x", val);
    return val;
}

