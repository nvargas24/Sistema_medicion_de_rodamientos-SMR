#include <stdio.h>
#include "esp_log.h"
#include "driver/i2c.h"



/* Defines */
#define I2C_MASTER_SCL_IO           22      /*!< GPIO number used for I2C master clock */
#define I2C_MASTER_SDA_IO           21      /*!< GPIO number used for I2C master data  */
#define I2C_MASTER_NUM              0                          /*!< I2C master i2c port number, the number of i2c peripheral interfaces available will depend on the chip */
#define I2C_MASTER_FREQ_HZ          400000                     /*!< I2C master clock frequency */
#define I2C_MASTER_TX_BUF_DISABLE   0                          /*!< I2C master doesn't need buffer */
#define I2C_MASTER_RX_BUF_DISABLE   0                          /*!< I2C master doesn't need buffer */
#define I2C_MASTER_TIMEOUT_MS       1000

/* Function prototypes */
//esp_err_t RegisterWriteByte(uint8_t reg_addr, uint8_t data);
//esp_err_t RegisterRead(uint8_t reg_addr, uint8_t *data, size_t len);

/* Global variables */
static const char *TAG = "MPU6050 Test";