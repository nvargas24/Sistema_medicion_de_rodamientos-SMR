
#ifndef _MLX90614_H_
#define _MLX90614_H_
#include "esp_system.h"

#define MLX90614_ADDRESS    0x5A

#define WRITE_BIT           I2C_MASTER_WRITE  /*!< I2C master write */
#define READ_BIT            I2C_MASTER_READ    /*!< I2C master read */

#define ACK_CHECK_EN        0x01    /*!< I2C master will check ack from slave*/
#define ACK_CHECK_DIS       0x00    /*!< I2C master will not check ack from slave */
#define ACK_VAL             0x00    /*!< I2C ack value */
#define NACK_VAL            0x01    /*!< I2C nack value */




/* Public Functions Prototypes  */
esp_err_t MLX90614_GetTa(float *ta);
esp_err_t MLX90614_GetTo(float *to);
esp_err_t MLX90614_GetTo2(float *to2);


#endif
