#ifndef MAIN_H_
#define MAIN_H_


#define DEBUG
#define ROD_ANT
//#define ROD_POS

#define SMR_FIRMWARE_VERSION    "V1.0_R3.1"
#define SMR_LED_INDICATE_TIMES  3
#define SMR_TIME_BTW_MEASURES   6000
#define SMR_TIME_BTW_LED_IND    500

#define HIGH 1
#define LOW  0

#define WIFI_STATE_LED    GPIO_NUM_2
#define ERROR_STATE_LED   GPIO_NUM_4
#define RTC_RST_PIN       GPIO_NUM_12

/* Macros para FFT */
#define ADC_SAMPLES 1024
#define FFT_SAMPLES 512
#define RESOLUTION_F 37  // Hz
#define SWEEP_FFT 5
#define SNR -15


/*  I2C Defines */
#define I2C_MASTER_SCL_IO           22      /*!< GPIO number used for I2C master clock */
#define I2C_MASTER_SDA_IO           21      /*!< GPIO number used for I2C master data  */
#define I2C_MASTER_NUM              0                          /*!< I2C master i2c port number, the number of i2c peripheral interfaces available will depend on the chip */
#define I2C_MASTER_FREQ_HZ          100000                     /*!< I2C master clock frequency */
#define I2C_MASTER_TX_BUF_DISABLE   0                          /*!< I2C master doesn't need buffer */
#define I2C_MASTER_RX_BUF_DISABLE   0                          /*!< I2C master doesn't need buffer */
#define I2C_MASTER_TIMEOUT_MS       1000

/* SPI Defines */
#define SPI_CS_PIN      5
#define SPI_CLK_PIN     18
#define SPI_MISO_PIN    19
#define SPI_MOSI_PIN    23

/* Battery levels defines */
#define SMR_LOW_BATTERY_MV  2700
#define SMR_HIGH_BATTERY_MV 4300

typedef enum smr_errorCtrl_e
{
  SMR_UNDEFINED_ERROR,
  SMR_OK,
  SMR_GPIO_INIT_ERROR,
  SMR_NVS_FLASH_ERROR,
  SMR_NETIF_INIT_ERROR,
  SMR_EVENT_LOOP_ERROR,
  SMR_WIFI_CONN_ERROR,
  SMR_I2C_INIT_ERROR,
  SMR_SPI_INIT_ERROR,
  SMR_ADC_INIT_ERROR,
  SMR_MQTT_CONN_ERROR,
  SMR_MCP3008_INIT_ERROR,
  SMR_MPU6050_INIT_ERROR,
  SMR_ADC_READ_ERROR,
  SMR_MPU6050_READ_ERROR,
  SMR_MCP3008_READ_ERROR,
  SMR_MLX3096_READ_ERROR,
  SMR_MQTT_PUBLISH_ERROR,
}smr_errorCtrl_t;

typedef enum smr_blink_led_e
{
    SMR_BLINK_LED_ULTRA_FAST = 0,
    SMR_BLINK_LED_FAST,
    SMR_BLINK_LED_SLOW,
    SMR_BLINK_LED_NORMAL,
    SMR_BLINK_LED_ULTRA_SLOW
} smr_blink_led_t;


#endif