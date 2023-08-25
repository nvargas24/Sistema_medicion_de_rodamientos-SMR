/**
 * @file main.c
 * @author Fernando Galassi
 * @brief This file contains the main script for the SMR sensor
 * @version 0.1
 * @date 2022-10-13
 *
 * @copyright  SMR Copyright (c) 2022
 *
 */

/* Includes */
#include <stdio.h>
#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "esp_wifi.h"
#include "esp_system.h"
#include "nvs_flash.h"
#include "esp_event.h"
#include "esp_netif.h"
#include "protocol_examples_common.h"

#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/semphr.h"
#include "freertos/queue.h"

#include "lwip/sockets.h"
#include "lwip/dns.h"
#include "lwip/netdb.h"

#include "esp_log.h"
#include "mqtt_client.h"

#include "driver/gpio.h"
#include "driver/i2c.h"
#include "driver/spi_master.h"
#include "driver/adc.h"
#include "esp_adc_cal.h"

#include "main.h"

#include "Drivers/mlx90614.h"
#include "Drivers/mpu6050.h"
#include "Drivers/mcp3008.h"
#include "Drivers/fft.h"
#include "Drivers/ds3231.h"

/* Function prototypes */
static esp_err_t smr_configure_gpios(void);
static esp_err_t smr_adc_init(void);
static esp_err_t smr_i2c_master_init(void);
static esp_err_t smr_spi_init(void);
static void smr_log_error_if_nonzero(const char *message, int error_code);
static void smr_mqtt_event_handler(void *handler_args, esp_event_base_t base, int32_t event_id, void *event_data);
static esp_err_t smr_mqtt_init(void);
static smr_errorCtrl_t smr_init_peripherals(void);
static smr_errorCtrl_t smr_measure_sensors(void);
static smr_errorCtrl_t smr_adc_read(uint32_t *batteryLevel);
static smr_errorCtrl_t smr_publish_measures(void);
static void smr_blink_led(smr_blink_led_t period);
static void smr_led_indicate(smr_blink_led_t type, unsigned int rep);
static void smr_error_reg(smr_errorCtrl_t errorCtrl, char *retString);
static esp_err_t smr_save_run_time(void);
static esp_err_t smr_save_last_error(uint8_t lastError);
static esp_err_t smr_print_nvs_saved(void);

float searchFreq(float freq_s, int tol, float *mag_fft, float *freq_fft);
esp_err_t rfft_calcule(int16_t *meas_mcp, float *mag_fft, float *freq_fft);

/* Global Variables */
esp_mqtt_client_handle_t client;
esp_adc_cal_characteristics_t *adc_chars;
static const adc_channel_t vBatLvl = ADC_CHANNEL_6;

uint8_t stageNum = 0;

float Ta;
float To;
float Td;
float accel[3];
float accel_offset[3];
float accel_axial = 0.0;
float accel_radial = 0.0;
bool flag_mode_cal_accel = 1;
uint32_t batteryLevel;
float tempThreshold;
float axialThreshold;
float radialThreshold;
bool axialAlarm = false;
bool radialAlarm = false;
bool alarmTemp = false;
bool run = false;
char timeStamp[40];

char aux[200];

/* Variables para FFT*/
float frecBPFI;
float frecBPFO;
float frecBSF;
float frecFTF;
bool presBPFO = false;
bool presBPFI = false;
bool presFTF = false;
bool presBSF = false;
float magBPFO = 0.0;
float magBPFI = 0.0;
float magFTF = 0.0;
float magBSF = 0.0;

float snr_dynamic = 0.0;
float critical_mag = 0.0;

#ifdef ROD_ANT
static const char *TAG = "SMR ROD ANTERIOR";
#endif

#ifdef ROD_POS
static const char *TAG = "SMR ROD POSTERIOR";
#endif

/**
 * @brief Main function
 *
 */
void app_main(void)
{
    smr_errorCtrl_t errorCtrl;
    char errorString[100];
    int i;

    errorCtrl = smr_init_peripherals();
    if (errorCtrl != SMR_OK)
    {
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_ULTRA_SLOW, errorCtrl);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
            ESP_LOGI(TAG, "Restarting in 3 seconds....");
        #endif
        vTaskDelay(3000 / portTICK_PERIOD_MS);
        /* Nuestra rutina de manejo de errores de momento es indicarlo mediante LED y reiniciar */
        smr_save_last_error((uint8_t) errorCtrl);
        smr_save_run_time();
        esp_restart();
    }
    else
    {
        smr_print_nvs_saved();

        #ifdef SET_RTC
            uint8_t time[] = {0x00, 0x02, 0x22, 0x07, 0x22, 0x04, 0x23, 0x44}; /* 0 SSMMHH WD DDMMAA */
            esp_err_t ret;

            ret = DS3231_SetTime(time);
            if(ret != ESP_OK)
            {
                errorCtrl = SMR_DS3231_SETING_ERROR;
                smr_error_reg(errorCtrl, errorString);

                for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
                {
                    smr_led_indicate(SMR_BLINK_LED_ULTRA_SLOW, errorCtrl);
                    /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                    vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
                }

                #ifdef DEBUG
                    ESP_LOGI(TAG, "%s", errorString);
                    ESP_LOGI(TAG, "Restarting in 3 seconds....");
                #endif
                vTaskDelay(3000 / portTICK_PERIOD_MS);
                /* Nuestra rutina de manejo de errores de momento es indicarlo mediante LED y reiniciar */
                smr_save_last_error((uint8_t) errorCtrl);
                smr_save_run_time();
                esp_restart();
            }
        #endif
    }

    while (1)
    {
        if (run)
        {
            errorCtrl = smr_measure_sensors();
            if (errorCtrl != SMR_OK)
            {
                smr_error_reg(errorCtrl, errorString);

                for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
                {
                    smr_led_indicate(SMR_BLINK_LED_ULTRA_SLOW, errorCtrl);
                    /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                    vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
                }

                #ifdef DEBUG
                    ESP_LOGI(TAG, "%s", errorString);
                    ESP_LOGI(TAG, "Restarting in 3 seconds....");
                #endif
                vTaskDelay(3000 / portTICK_PERIOD_MS);

                /* Nuestra rutina de manejo de errores de momento es indicarlo mediante LED y reiniciar */
                smr_save_last_error((uint8_t) errorCtrl);
                smr_save_run_time();
                esp_restart();
            }

            errorCtrl = smr_publish_measures();
            if (errorCtrl != SMR_OK)
            {
                smr_error_reg(errorCtrl, errorString);

                for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
                {
                    smr_led_indicate(SMR_BLINK_LED_ULTRA_SLOW, errorCtrl);
                    /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                    vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
                }

                #ifdef DEBUG
                    ESP_LOGI(TAG, "%s", errorString);
                    ESP_LOGI(TAG, "Restarting in 3 seconds....");
                #endif
                vTaskDelay(3000 / portTICK_PERIOD_MS);

                /* Nuestra rutina de manejo de errores de momento es indicarlo mediante LED y reiniciar */
                smr_save_last_error((uint8_t) errorCtrl);
                smr_save_run_time();
            }
            /* Blocking delay */
            vTaskDelay(SMR_TIME_BTW_MEASURES / portTICK_PERIOD_MS);
        }
    }
}

/**
 * @brief This function is used to configurate de ADC Channel 1
 *
 */
esp_err_t smr_adc_init(void)
{
    esp_adc_cal_characterize(ADC_UNIT_1, ADC_ATTEN_DB_0, ADC_WIDTH_BIT_12, 0, &adc_chars);
    ESP_ERROR_CHECK(adc1_config_width(ADC_WIDTH_BIT_12));
    ESP_ERROR_CHECK(adc1_config_channel_atten(vBatLvl, ADC_ATTEN_DB_0));

    return ESP_OK;
}

/**
 * @brief This function is used to initialize the I2C driver
 *
 * @return esp_err_t  0 -> No error
 */
esp_err_t smr_i2c_master_init(void)
{
    int i2c_master_port = I2C_MASTER_NUM;

    i2c_config_t conf =
        {
            .mode = I2C_MODE_MASTER,
            .sda_io_num = I2C_MASTER_SDA_IO,
            .scl_io_num = I2C_MASTER_SCL_IO,
            .sda_pullup_en = GPIO_PULLUP_ENABLE,
            .scl_pullup_en = GPIO_PULLUP_ENABLE,
            .master.clk_speed = I2C_MASTER_FREQ_HZ,
        };

    i2c_param_config(i2c_master_port, &conf);

    return i2c_driver_install(i2c_master_port, conf.mode, I2C_MASTER_RX_BUF_DISABLE, I2C_MASTER_TX_BUF_DISABLE, 0);
}

/**
 * @brief SPI initialization
 *
 * @return esp_err_t    0 -> No error
 */
static esp_err_t smr_spi_init(void)
{
    esp_err_t ret;

    gpio_reset_pin(SPI_CS_PIN);
    gpio_set_direction(SPI_CS_PIN, GPIO_MODE_OUTPUT);
    gpio_set_level(SPI_CS_PIN, 1);

    spi_bus_config_t buscfg = {
        .miso_io_num = SPI_MISO_PIN,
        .mosi_io_num = SPI_MOSI_PIN,
        .sclk_io_num = SPI_CLK_PIN,
        .quadwp_io_num = -1,
        .quadhd_io_num = -1,
    };

    ret = spi_bus_initialize(SPI3_HOST, &buscfg, SPI_DMA_DISABLED);
    assert(ret == ESP_OK);

    return ret;
}

/**
 * @brief This function is used to log all the errors
 *
 * @param message  String that indicates the error
 * @param error_code Error code number
 */
static void smr_log_error_if_nonzero(const char *message, int error_code)
{
    if (error_code != 0)
    {
        ESP_LOGE(TAG, "Last error %s: 0x%x", message, error_code);
    }
}

/**
 * @brief Event handler registered to receive MQTT events
 *
 *  This function is called by the MQTT client event loop.
 *
 * @param handler_args user data registered to the event.
 * @param base Event base for the handler(always MQTT Base in this example).
 * @param event_id The id for the received event.
 * @param event_data The data for the event, esp_mqtt_event_handle_t.
 */
static void smr_mqtt_event_handler(void *handler_args, esp_event_base_t base, int32_t event_id, void *event_data)
{
    // ESP_LOGD(TAG, "Event dispatched from event loop base=%s, event_id=%d", base, event_id);
    esp_mqtt_event_handle_t event = event_data;
    esp_mqtt_client_handle_t client = event->client;
    int msg_id;
    switch ((esp_mqtt_event_id_t)event_id)
    {
    case MQTT_EVENT_CONNECTED:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_CONNECTED");
#endif
        msg_id = esp_mqtt_client_publish(client, "/topic/qos1", "data_3", 0, 1, 0);
#ifdef DEBUG
        ESP_LOGI(TAG, "Sent publish successful, msg_id=%d", msg_id);
#endif

        msg_id = esp_mqtt_client_subscribe(client, "/topic/qos0", 0);
        msg_id = esp_mqtt_client_subscribe(client, "smr/start", 2);
        msg_id = esp_mqtt_client_subscribe(client, "smr/stop", 2);
        msg_id = esp_mqtt_client_subscribe(client, "tempThreshold", 2);
        msg_id = esp_mqtt_client_subscribe(client, "axialThreshold", 2);
        msg_id = esp_mqtt_client_subscribe(client, "radialThreshold", 2);

#ifdef ROD_ANT
        msg_id = esp_mqtt_client_subscribe(client, "rodAnt/frecBPFI", 2);
        msg_id = esp_mqtt_client_subscribe(client, "rodAnt/frecBPFO", 2);
        msg_id = esp_mqtt_client_subscribe(client, "rodAnt/frecBSF", 2);
        msg_id = esp_mqtt_client_subscribe(client, "rodAnt/frecFTF", 2);
#endif

#ifdef ROD_POS
        msg_id = esp_mqtt_client_subscribe(client, "rodPos/frecBPFI", 2);
        msg_id = esp_mqtt_client_subscribe(client, "rodPos/frecBPFO", 2);
        msg_id = esp_mqtt_client_subscribe(client, "rodPos/frecBSF", 2);
        msg_id = esp_mqtt_client_subscribe(client, "rodPos/frecFTF", 2);
#endif

#ifdef DEBUG
        ESP_LOGI(TAG, "Sent subscribe successful, msg_id=%d", msg_id);
#endif
        msg_id = esp_mqtt_client_subscribe(client, "/topic/qos1", 1);
#ifdef DEBUG
        ESP_LOGI(TAG, "Sent subscribe successful, msg_id=%d", msg_id);
#endif

        // msg_id = esp_mqtt_client_unsubscribe(client, "/topic/qos1");
#ifdef DEBUG
        ESP_LOGI(TAG, "Sent unsubscribe successful, msg_id=%d", msg_id);
#endif
        break;
    case MQTT_EVENT_DISCONNECTED:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_DISCONNECTED");
#endif
        break;

    case MQTT_EVENT_SUBSCRIBED:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_SUBSCRIBED, msg_id=%d", event->msg_id);
#endif
        msg_id = esp_mqtt_client_publish(client, "/topic/qos0", "data", 0, 0, 0);
#ifdef DEBUG
        ESP_LOGI(TAG, "Sent publish successful, msg_id=%d", msg_id);
#endif
        break;
    case MQTT_EVENT_UNSUBSCRIBED:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_UNSUBSCRIBED, msg_id=%d", event->msg_id);
#endif
        break;
    case MQTT_EVENT_PUBLISHED:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_PUBLISHED, msg_id=%d", event->msg_id);
#endif
        break;
    case MQTT_EVENT_DATA:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_DATA");
        printf("TOPIC=%.*s\r\n", event->topic_len, event->topic);
        printf("DATA=%.*s\r\n", event->data_len, event->data);
#endif
        sprintf(aux, "%.*s", event->topic_len, event->topic);
        if (strcmp(aux, "smr/start") == 0)
        {
            run = true;
            stageNum++;
        }
        else if (strcmp(aux, "smr/stop") == 0)
        {
            run = false;
        }
        else if (strcmp(aux, "alarmas/temperatura") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            tempThreshold = strtof(aux, NULL);
        }
        else if (strcmp(aux, "alarmas/acelAxial") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            axialThreshold = strtof(aux, NULL);
        }
        else if (strcmp(aux, "alarmas/acelRadial") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            radialThreshold = strtof(aux, NULL);
        }

#ifdef ROD_ANT
        else if (strcmp(aux, "rodAnt/frecBPFI") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFI = strtof(aux, NULL);
        }
        else if (strcmp(aux, "rodAnt/frecBPFO") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFO = strtof(aux, NULL);
        }
        else if (strcmp(aux, "rodAnt/frecBSF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBSF = strtof(aux, NULL);
        }
        else if (strcmp(aux, "rodAnt/frecFTF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecFTF = strtof(aux, NULL);
        }
#endif

#ifdef ROD_POS
        else if (strcmp(aux, "rodPos/frecBPFI") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFI = strtof(aux, NULL);
        }
        else if (strcmp(aux, "rodPos/frecBPFO") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFO = strtof(aux, NULL);
        }
        else if (strcmp(aux, "rodPos/frecBSF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBSF = strtof(aux, NULL);
        }
        else if (strcmp(aux, "rodPos/frecFTF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecFTF = strtof(aux, NULL);
        }
#endif
        break;
    case MQTT_EVENT_ERROR:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_ERROR");
#endif
        if (event->error_handle->error_type == MQTT_ERROR_TYPE_TCP_TRANSPORT)
        {
            smr_log_error_if_nonzero("reported from esp-tls", event->error_handle->esp_tls_last_esp_err);
            smr_log_error_if_nonzero("reported from tls stack", event->error_handle->esp_tls_stack_err);
            smr_log_error_if_nonzero("captured as transport's socket errno", event->error_handle->esp_transport_sock_errno);
#ifdef DEBUG
            ESP_LOGI(TAG, "Last errno string (%s)", strerror(event->error_handle->esp_transport_sock_errno));
#endif
        }
        break;
    default:
#ifdef DEBUG
        ESP_LOGI(TAG, "Other event id:%d", event->event_id);
#endif
        break;
    }
}

/**
 * @brief This function is used to initializate the MQTT client
 *
 * @return esp_err_t  0 -> No error
 */
static esp_err_t smr_mqtt_init(void)
{
    esp_err_t ret;

    esp_mqtt_client_config_t mqtt_cfg =
        {
            .broker.address.hostname = "192.168.86.203",
            .broker.address.transport = MQTT_TRANSPORT_OVER_TCP,
            .broker.address.port = 1883,
        };
    client = esp_mqtt_client_init(&mqtt_cfg);
    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, smr_mqtt_event_handler, NULL);
    ret = esp_mqtt_client_start(client);
    return ret;
}


/**
 * @brief This function is used to perform sensor's measurement
 *
 */
smr_errorCtrl_t smr_measure_sensors(void)
{
    smr_errorCtrl_t errorCtrl;
    esp_err_t ret;
    char errorString[100];
    uint8_t i;

    /* Timestamp generation */
    ret = DS3231_GetTimeStamp(timeStamp);
    if (ret != ESP_OK)
    {
        errorCtrl = SMR_DS3231_GETTING_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_DS3231_GETTING_ERROR - 7));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    /* Calibracion MPU6050*/
    if(flag_mode_cal_accel == 1)
    {
        printf("MODO CALIBRACION\n");
        printf("Colocar sensor quieto\n");

        bzero(accel_offset, sizeof(accel_offset));

        for(int i=0; i<SAMPLES_ACCEL_CAL; i++)
        {
            ret = MPU6050_ReadAccelerometer(accel, 3);
            if (ret != ESP_OK)
            {
                errorCtrl = SMR_MPU6050_READ_ERROR;
                smr_error_reg(errorCtrl, errorString);

                for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
                {
                    smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MPU6050_READ_ERROR - 7));
                    /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                    vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
                }

                #ifdef DEBUG
                    ESP_LOGI(TAG, "%s", errorString);
                #endif

                return errorCtrl;
            }
            else
            {
                accel_offset[0] += accel[0];
                accel_offset[1] += accel[1];
                accel_offset[2] += accel[2];
            }
        }

        for(int i=0; i<3; i++)
        {
            accel_offset[i]/=SAMPLES_ACCEL_CAL;
        }

        flag_mode_cal_accel = 0;
        bzero(accel, sizeof(accel));                
    }

    #ifdef DEBUG
        printf("accel offset x: %f\n", accel_offset[0]);
        printf("accel offset y: %f\n", accel_offset[1]);
        printf("accel offset z: %f\n", accel_offset[2]);
    #endif

    /* ---- AGREGAR DEBUG_SHAKER ----*/
    #ifdef DEBUG_CAL_SHAKER
        printf("x\ty\tz\n");
        while(1)
        {
            /* Acceleration measures */
            /* Considero ahora que la aceleración en X es la axial y radial en Y */
            ret = MPU6050_ReadAccelerometer(accel, 3);
            if (ret != ESP_OK)
            {
                errorCtrl = SMR_MPU6050_READ_ERROR;
                smr_error_reg(errorCtrl, errorString);

                for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
                {
                    smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MPU6050_READ_ERROR - 7));
                    /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                    vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
                }

                #ifdef DEBUG
                    ESP_LOGI(TAG, "%s", errorString);
                #endif

                return errorCtrl;
            }
            else
            {
                #ifdef DEBUG
                    printf("%.3f\t%.3f\t%.3f\n",accel[0]-accel_offset[0], accel[1]-accel_offset[1], accel[2]-accel_offset[2]);
                #endif
            }
        }
    #endif

    /* Acceleration measures */
    ret = MPU6050_ReadAccelerometer(accel, 3);
    if (ret != ESP_OK)
    {
        errorCtrl = SMR_MPU6050_READ_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MPU6050_READ_ERROR - 7));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    else
    {
        #ifdef DEBUG
            ESP_LOGI(TAG, "AccelX = %f", accel[0]);
            ESP_LOGI(TAG, "AccelY = %f", accel[1]);
            ESP_LOGI(TAG, "AccelZ = %f", accel[2]);
        #endif

        /* Conversion de G a mm/s2*/
        for(int i=0; i<3; i++)
        {
            accel[i] = (accel[i] / MPU6050_AccelSens_2) * 9.81 * UNIT_ACCEL_MM_S2;
        }
        
        /* Calculo de aceleracion radial y axial*/
        // Fijarse segun colacion de PCB para accel_axial
        //accel_axial = accel[2];
        //accel_radial = sqrt(pow(accel[0], 2)+pow(accel[1], 2));

        /* Considero ahora que la aceleración en X es la axial y radial en Y */
        accel_axial = accel[0];
        accel_radial = accel[1];

        /* Hay alarma axial? */
        if (accel_axial >= axialThreshold)
        {
            axialAlarm = true;
            #ifdef DEBUG
                ESP_LOGI(TAG, "AXIAL ALARM");
            #endif
        }
        else
        {
            axialAlarm = false;
        }

        /* Hay alarma radial? */
        if (accel_radial >= radialThreshold)
        {
            radialAlarm = true;
            #ifdef DEBUG
                ESP_LOGI(TAG, "RADIAL ALARM");
            #endif
        }
        else
        {
            radialAlarm = false;
        }
    }

    /* ---- AGREGAR CALIBRACION TEMPERATURA SERIAL ----*/

    /* Temperature measures */
    ret = MLX90614_GetTa(&Ta);
    if (ret != ESP_OK)
    {
        errorCtrl = SMR_MLX3096_READ_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MLX3096_READ_ERROR - 7));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    else
    {
        ret = MLX90614_GetTo(&To);

        if (ret != ESP_OK)
        {
            errorCtrl = SMR_MLX3096_READ_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MLX3096_READ_ERROR - 7));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        else
        {
            #ifdef DEBUG
                ESP_LOGI(TAG, "Temperatura Ambiente = %f", Ta);
                ESP_LOGI(TAG, "Temperatura Objetivo = %f", To);
            #endif

            Td = To - Ta;

            /* Hay alarma de temperatura? */
            if (Td > tempThreshold)
            {
                alarmTemp = true;
                #ifdef DEBUG
                    ESP_LOGI(TAG, "ALARMA TEMPERATURA. Td = %f", Td);
                #endif
            }
            else
            {
                alarmTemp = false;
            }
        }
    }

    // COMENTADO PARA USAR SIN BATERIA - PRUEBAS DE CALIBRACION POR SERIAL
    /* Battery level measurement
    errorCtrl = smr_adc_read(&batteryLevel);

    if (errorCtrl != SMR_OK)
    {
        errorCtrl = SMR_ADC_READ_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_ADC_READ_ERROR - 7));
            // Blocking wait for SMR_TIME_BTW_LED_IND ms
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }
    else
    {
        if (batteryLevel <= SMR_LOW_BATTERY_MV)
        {
            #ifdef DEBUG
                ESP_LOGI(TAG, "BATERIA BAJA ---- %lu", batteryLevel);
            #endif
        }
    }

    */

    /* Medicion  de MCP3008 */
    int16_t meas_mcp[ADC_SAMPLES];
    float data_adc2temp[ADC_SAMPLES];
    int16_t data_adc2fft[ADC_SAMPLES];

    bzero(meas_mcp, sizeof(meas_mcp));
    bzero(data_adc2temp, sizeof(data_adc2temp));
    bzero(data_adc2fft, sizeof(data_adc2fft));

    for(int k = 0; k < ADC_SAMPLES; k++)
    {
        ret = MCP3008_ReadChannel(0, &meas_mcp[k]);

        if(ret != ESP_OK)
        {
            errorCtrl = SMR_MCP3008_READ_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MCP3008_READ_ERROR - 7));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;

        }
        else
        {
            if(meas_mcp[k] <= ADC_SAMPLES && meas_mcp[k] >= 0){
                #ifdef DEBUG_MCP
                    ESP_LOGI(TAG, "LECTURA DE MCP --- %u", meas_mcp[k]);
                #endif
            }
            else
            {
                #ifdef DEBUG_MCP
                    ESP_LOGI(TAG, "LECTURA DE MCP NO VALIDA ---");
                #endif
            }
        }
    }

    vTaskDelay(pdMS_TO_TICKS(10));    

    /*Lecturas validas de MCP*/
    #ifdef DEBUG_MCP
        printf("LECTURA DE ADC\n");
        for(int k=0; k<ADC_SAMPLES; k++)
        {
            printf("%u\n", meas_mcp[k]);
        }
    #endif

    /* Creo variable para data a lectura en volt y fft */
    for(int k=0; k<ADC_SAMPLES; k++)
    {   
        data_adc2temp[k]=(5.0/ADC_SAMPLES)*(float)meas_mcp[k];
        data_adc2fft[k] = meas_mcp[k];
    }
    
    /* Factor de calibracion temporal*/
    for(int k=0; k<ADC_SAMPLES; k++)
    { 
        data_adc2temp[k]=data_adc2temp[k]*(1.115);
    }

    vTaskDelay(pdMS_TO_TICKS(10));    


    /* FFT measures */
    float mag_fft[FFT_SAMPLES];
    float freq_fft[FFT_SAMPLES];

    bzero(mag_fft, sizeof(mag_fft));
    bzero(freq_fft, sizeof(freq_fft));

    ret=rfft_calcule(data_adc2fft, mag_fft, freq_fft);

    /*FC PARA FFT*/
    // Pasaje a dBV de continua
    mag_fft[0] = 20*log10(mag_fft[0]/ADC_SAMPLES);

    // Pasaje a dBV del espectro
    for (int k = 1; k < FFT_SAMPLES; k++)
    {
        mag_fft[k] = 20*log10((mag_fft[k]/ADC_SAMPLES)*2.2);
    }
    vTaskDelay(pdMS_TO_TICKS(10));

    #ifdef DEBUG_FFT
        printf("Magnitud\tFrecuencia\n");
        for (int k = 0; k < FFT_SAMPLES; k++){
            printf("%.5f\t%.2f\n", mag_fft[k], freq_fft[k]);
        }
    #endif

    /* Calculo de SNR */
    snr_dynamic = obtener_snr(mag_fft); // en dBV - se calcula percentil 50 (mediana)
    
    // LIMITE PARA CONSIDERAR VALOR DE MAGNITUD VALIDO 
    critical_mag = snr_dynamic + 20*log10(TOL_SNR);

    /* ---- AGREGAR CALCULO DE DOMINANTE (SE IGNORA DC) ----*/

    magBPFO = searchFreq(frecBPFO, 5, mag_fft, freq_fft);
    magBPFI = searchFreq(frecBPFI, 5, mag_fft, freq_fft);
    magFTF = searchFreq(frecFTF, 5, mag_fft, freq_fft);
    magBSF = searchFreq(frecBSF, 5, mag_fft, freq_fft);

    #ifdef DEBUG
        ESP_LOGI(TAG, "Magnitud de BPFO (%.2fHz)= %.2fdBV", frecBPFO, magBPFO);
        ESP_LOGI(TAG, "Magnitud de BPFI (%.2fHz) = %.2fdBV", frecBPFI, magBPFI);
        ESP_LOGI(TAG, "Magnitud de FTF (%.2fHz) = %.2fdBV", frecFTF, magFTF);
        ESP_LOGI(TAG, "Magnitud de BSF (%.2fHz) = %.2fdBV", frecBSF, magBSF);
    #endif

    if (magBPFO > snr_dynamic)
    {
        presBPFO = true;
    }
    else
    {
        presBPFO = false;
    }

    if (magBPFI > snr_dynamic)
    {
        presBPFI = true;
    }
    else
    {
        presBPFI = false;
    }

    if (magFTF > snr_dynamic)
    {
        presFTF = true;
    }
    else
    {
        presFTF = false;
    }

    if (magBSF > snr_dynamic)
    {
        presBSF = true;
    }
    else
    {
        presBSF = false;
    }

    return SMR_OK;
}

/**
 * @brief This function is used to publish MQTT messages
 *
 */
smr_errorCtrl_t smr_publish_measures(void)
{
    char payload[100];
    char errorString[100];
    int ret;
    int i;
    smr_errorCtrl_t errorCtrl;

    #ifdef DEBUG_CAL_FFT
        /* Envio por MQTT datos de FFT y MCP*/
        char msg_mcp[ADC_SAMPLES*8];
        char msg_fft[FFT_SAMPLES*8];
        char msg_mag_mcp[64];
        char msg_freq_mcp[64];
        char msg_snr[64];

        int offset_mcp = 0;
        int offset_fft = 0;

        bzero(msg_mcp, sizeof(msg_mcp));
        bzero(msg_fft, sizeof(msg_fft));
        bzero(msg_mag_mcp, sizeof(msg_mag_mcp));
        bzero(msg_freq_mcp, sizeof(msg_freq_mcp));
        bzero(msg_snr, sizeof(msg_snr));
    #endif

#ifdef ROD_ANT

    ret = esp_mqtt_client_publish(client, "rodAnt/timeStamp", timeStamp, strlen(timeStamp), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", stageNum);
    ret = esp_mqtt_client_publish(client, "rodAnt/stageNum", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%lu", batteryLevel);
    ret = esp_mqtt_client_publish(client, "rodAnt/bateria", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", Ta);
    ret = esp_mqtt_client_publish(client, "rodAnt/tempAmb", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", To);
    ret = esp_mqtt_client_publish(client, "rodAnt/tempObj", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", accel[0]);
    ret = esp_mqtt_client_publish(client, "rodAnt/acelAxial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", accel[1]);
    ret = esp_mqtt_client_publish(client, "rodAnt/acelRadial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presBPFO);
    ret = esp_mqtt_client_publish(client, "rodAnt/presBPFO", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presBPFI);
    ret = esp_mqtt_client_publish(client, "rodAnt/presBPFI", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presBSF);
    ret = esp_mqtt_client_publish(client, "rodAnt/presBSF", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presFTF);
    ret = esp_mqtt_client_publish(client, "rodAnt/presFTF", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", alarmTemp);
    ret = esp_mqtt_client_publish(client, "rodAnt/alarmTemp", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", axialAlarm);
    ret = esp_mqtt_client_publish(client, "rodAnt/alarmAcelAxial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", radialAlarm);
    ret = esp_mqtt_client_publish(client, "rodAnt/alarmAcelRadial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    #ifdef DEBUG_CAL_FFT
        // Creo unico string para enviar lecturas de mcp
        for(int i =0; i<ADC_SAMPLES; i++)
        {
            offset_mcp += snprintf(msg_mcp+offset_mcp, sizeof(msg_mcp)-offset_mcp, "%.2f", data_adc2temp[i]);
            if(i!=(ADC_SAMPLES-1))
            {
                offset_mcp += snprintf(msg_mcp+offset_mcp, sizeof(msg_mcp)-offset_mcp, ",");
            }
        }

        // Creo unico string para enviar valores calculados de fft
        for(int i =0; i<FFT_SAMPLES; i++)
        {
            offset_fft += snprintf(msg_fft+offset_fft, sizeof(msg_fft)-offset_fft, "%.0f", mag_fft[i]);
            if(i!=(FFT_SAMPLES-1))
            {
                offset_fft += snprintf(msg_fft+offset_fft, sizeof(msg_fft)-offset_fft, ",");
            }
        }

        // Creo strings para enviar magnitud y frecuencia por mqtt
        snprintf(msg_mag_mcp, sizeof(msg_mag_mcp), "%.0f", mag_mcp);
        snprintf(msg_freq_mcp, sizeof(msg_freq_mcp), "%.0f", freq_mcp);
        snprintf(msg_snr, sizeof(msg_snr), "%.0f", snr_dynamic);

        ret = esp_mqtt_client_publish(client, "rodAnt/mcp", msg_mcp, strlen(msg_mcp), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodAnt/fft", msg_fft, strlen(msg_fft), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodAnt/mcpMag", msg_mag_mcp, strlen(msg_mag_mcp), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodAnt/mcpFreq", msg_freq_mcp, strlen(msg_freq_mcp), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodAnt/snr", msg_snr, strlen(msg_snr), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }
    #endif

    return SMR_OK;
#endif
#ifdef ROD_POS

    ret = esp_mqtt_client_publish(client, "rodPos/timeStamp", timeStamp, strlen(timeStamp), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", stageNum);
    ret = esp_mqtt_client_publish(client, "rodPos/stageNum", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", batteryLevel);
    ret = esp_mqtt_client_publish(client, "rodPos/bateria", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", Ta);
    ret = esp_mqtt_client_publish(client, "rodPos/tempAmb", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", To);
    ret = esp_mqtt_client_publish(client, "rodPos/tempObj", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", accel[0]);
    ret = esp_mqtt_client_publish(client, "rodPos/acelAxial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%f", accel[1]);
    ret = esp_mqtt_client_publish(client, "rodPos/acelRadial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presBPFO);
    ret = esp_mqtt_client_publish(client, "rodPos/presBPFO", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presBPFI);
    ret = esp_mqtt_client_publish(client, "rodPos/presBPFI", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presBSF);
    ret = esp_mqtt_client_publish(client, "rodPos/presBSF", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", presFTF);
    ret = esp_mqtt_client_publish(client, "rodPos/presFTF", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", alarmTemp);
    ret = esp_mqtt_client_publish(client, "rodPos/alarmTemp", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", axialAlarm);
    ret = esp_mqtt_client_publish(client, "rodPos/alarmAcelAxial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    sprintf(payload, "%d", radialAlarm);
    ret = esp_mqtt_client_publish(client, "rodPos/alarmAcelRadial", payload, strlen(payload), 0, false);
    if (ret < 0)
    {
        errorCtrl = SMR_MQTT_PUBLISH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

        #ifdef DEBUG
            ESP_LOGI(TAG, "%s", errorString);
        #endif

        return errorCtrl;
    }

    #ifdef DEBUG_CAL_FFT
        // Creo unico string para enviar lecturas de mcp
        for(int i =0; i<ADC_SAMPLES; i++)
        {
            offset_mcp += snprintf(msg_mcp+offset_mcp, sizeof(msg_mcp)-offset_mcp, "%.2f", data_adc2temp[i]);
            if(i!=(ADC_SAMPLES-1))
            {
                offset_mcp += snprintf(msg_mcp+offset_mcp, sizeof(msg_mcp)-offset_mcp, ",");
            }
        }

        // Creo unico string para enviar valores calculados de fft
        for(int i =0; i<FFT_SAMPLES; i++)
        {
            offset_fft += snprintf(msg_fft+offset_fft, sizeof(msg_fft)-offset_fft, "%.0f", mag_fft[i]);
            if(i!=(FFT_SAMPLES-1))
            {
                offset_fft += snprintf(msg_fft+offset_fft, sizeof(msg_fft)-offset_fft, ",");
            }
        }

        // Creo strings para enviar magnitud y frecuencia por mqtt
        snprintf(msg_mag_mcp, sizeof(msg_mag_mcp), "%.0f", mag_mcp);
        snprintf(msg_freq_mcp, sizeof(msg_freq_mcp), "%.0f", freq_mcp);
        snprintf(msg_snr, sizeof(msg_snr), "%.0f", snr_dynamic);

        ret = esp_mqtt_client_publish(client, "rodPos/mcp", msg_mcp, strlen(msg_mcp), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodPos/fft", msg_fft, strlen(msg_fft), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodPos/mcpMag", msg_mag_mcp, strlen(msg_mag_mcp), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodPos/mcpFreq", msg_freq_mcp, strlen(msg_freq_mcp), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }

        ret = esp_mqtt_client_publish(client, "rodPos/snr", msg_snr, strlen(msg_snr), 0, 0);
        if (ret < 0)
        {
            errorCtrl = SMR_MQTT_PUBLISH_ERROR;
            smr_error_reg(errorCtrl, errorString);

            for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
            {
                smr_led_indicate(SMR_BLINK_LED_FAST, (SMR_MQTT_PUBLISH_ERROR - 15));
                /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
                vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
            }

            #ifdef DEBUG
                ESP_LOGI(TAG, "%s", errorString);
            #endif

            return errorCtrl;
        }
    #endif

    return SMR_OK;
#endif
#ifdef DEBUG
    ESP_LOGI(TAG, "Publish done!");
#endif
}

/**
 * @brief This function is used to configure all the GPIOs
 *
 */
esp_err_t smr_configure_gpios(void)
{
    int ret;
    gpio_reset_pin(WIFI_STATE_LED);
    ret = gpio_set_direction(WIFI_STATE_LED, GPIO_MODE_OUTPUT);
    gpio_reset_pin(ERROR_STATE_LED);
    ret = gpio_set_direction(ERROR_STATE_LED, GPIO_MODE_OUTPUT);
    gpio_reset_pin(RTC_RST_PIN);
    ret = gpio_set_direction(RTC_RST_PIN, GPIO_MODE_OUTPUT);

    return ret;
}

/**
 * @brief This function is used to initialize all the peripherals
 *
 * @return smr_errorCtrl_t 0 -> No error
 */
smr_errorCtrl_t smr_init_peripherals(void)
{
    esp_err_t res;
    smr_errorCtrl_t errorCtrl;
    uint8_t i;
    char errorString[100];

#ifdef DEBUG
    ESP_LOGI(TAG, "Starting....");
    ESP_LOGI(TAG, "Firmware version: %s", SMR_FIRMWARE_VERSION);
#endif

    res = smr_configure_gpios();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_GPIO_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "GPIO init successfully");
#endif
    }

    res = nvs_flash_init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_NVS_FLASH_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_NVS_FLASH_ERROR);

            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "NVS flash init successfully");
#endif
    }

    res = esp_netif_init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_NETIF_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_NETIF_INIT_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "NETIF init successfully");
#endif
    }

    res = esp_event_loop_create_default();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_EVENT_LOOP_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_EVENT_LOOP_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "EVENT LOOP init successfully");
#endif
    }

    res = example_connect();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_WIFI_CONN_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_WIFI_CONN_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
        gpio_set_level(WIFI_STATE_LED, HIGH);
#ifdef DEBUG
        ESP_LOGI(TAG, "WIFI successfully connected");
#endif
    }

    res = smr_i2c_master_init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_I2C_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_I2C_INIT_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "I2C init successfully");
#endif
    }

    res = smr_spi_init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_SPI_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_SPI_INIT_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "SPI init successfully");
#endif
    }

    res = smr_adc_init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_ADC_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_NORMAL, SMR_ADC_INIT_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "ADC init successfully");
#endif
    }

    res = MCP3008_Init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_MCP3008_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MCP3008_INIT_ERROR - 7));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "MCP3008 init successfully");
#endif
    }

    res = MPU6050_Init(MPU6050_DataRate_400Hz, MPU6050_Accelerometer_2G, MPU6050_GyroSens_250);
    if (res != ESP_OK)
    {
        errorCtrl = SMR_MPU6050_INIT_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, (SMR_MPU6050_INIT_ERROR - 7));
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "MPU6050 init successfully");
#endif
    }

    res = smr_mqtt_init();
    if (res != ESP_OK)
    {
        errorCtrl = SMR_MQTT_CONN_ERROR;
        smr_error_reg(errorCtrl, errorString);

        for (i = 0; i < SMR_LED_INDICATE_TIMES; i++)
        {
            smr_led_indicate(SMR_BLINK_LED_SLOW, SMR_MQTT_CONN_ERROR);
            /* Blocking wait for SMR_TIME_BTW_LED_IND ms*/
            vTaskDelay(SMR_TIME_BTW_LED_IND / portTICK_PERIOD_MS);
        }

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif

        return errorCtrl;
    }
    else
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT successfully connected");
#endif
    }

    return SMR_OK;
}

/**
 * @brief This function is used to get an ADC read.
 *
 * @param batteryLevel Placeholder for the ADC measure.
 * @return smr_errorCtrl  0 -> Not error.
 */
smr_errorCtrl_t smr_adc_read(uint32_t *batteryLevel)
{
    uint32_t result;
    smr_errorCtrl_t errorCtrl;
    char errorString[100];

    result = esp_adc_cal_raw_to_voltage(adc1_get_raw(vBatLvl), &adc_chars);

    if ((result < SMR_LOW_BATTERY_MV) || (result > SMR_HIGH_BATTERY_MV))
    {
        errorCtrl = SMR_ADC_READ_ERROR;
        smr_error_reg(errorCtrl, errorString);

#ifdef DEBUG
        ESP_LOGI(TAG, "%s", errorString);
#endif
    }

    else
    {
        *(batteryLevel) = result;

        errorCtrl = SMR_OK;

#ifdef DEBUG
        ESP_LOGI(TAG, "ADC Reading sucessfully");
#endif
    }

    return errorCtrl;
}

/**
 * @brief This function returns a time period in milliseconds corresponding to the value of the enumeration smr_blink_led_t passed as an argument.
 * 
 * @param period  Blinking period.
 */
void smr_blink_led(smr_blink_led_t period)
{
    uint32_t speed = 0;

    switch (period)
    {
        case SMR_BLINK_LED_ULTRA_SLOW:
            speed = 2000;
            break;

        case SMR_BLINK_LED_SLOW:
            speed = 1000;
            break;

        case SMR_BLINK_LED_NORMAL:
            speed = SMR_TIME_BTW_LED_IND;
            break;

        case SMR_BLINK_LED_FAST:
            speed = 250;
            break;
        case SMR_BLINK_LED_ULTRA_FAST:
            speed = 125;
            break;
    }

    gpio_set_level(ERROR_STATE_LED, HIGH);
    vTaskDelay(speed / portTICK_PERIOD_MS);
    gpio_set_level(ERROR_STATE_LED, LOW);
}

/**
 * @brief This function is responsible for blinking the indicator LED a certain number of times defined by smr_errorCtrl_t at a speed specified by smr_blink_led_t.
 * 
 * @param type  Blinking period.
 * @param rep   Blinking times.
 */
void smr_led_indicate(smr_blink_led_t type, unsigned int rep)
{
    unsigned int i;

    for (i = 0; i < rep; i++)
        smr_blink_led(type);
}

/**
 * @brief This function returns a string indicating the error that occurred based on the value of smr_errorCtrl_t received.
 * 
 * @param errorCtrl  Error to be printed into string.
 * @param retString  String that contains the error info.
 */
void smr_error_reg(smr_errorCtrl_t errorCtrl, char *retString)
{
    char errorString[40];

    switch (errorCtrl)
    {
    case SMR_UNDEFINED_ERROR:
        sprintf(errorString, "SMR_UNDEFINED_ERROR");
        break;

    case SMR_OK:
        sprintf(errorString, "SMR_OK");
        break;

    case SMR_GPIO_INIT_ERROR:
        sprintf(errorString, "SMR_GPIO_INIT_ERROR");
        break;

    case SMR_NVS_FLASH_ERROR:
        sprintf(errorString, "SMR_NVS_FLASH_ERROR");
        break;

    case SMR_NETIF_INIT_ERROR:
        sprintf(errorString, "SMR_NETIF_INIT_ERROR");
        break;

    case SMR_EVENT_LOOP_ERROR:
        sprintf(errorString, "SMR_EVENT_LOOP_ERROR");
        break;

    case SMR_WIFI_CONN_ERROR:
        sprintf(errorString, "SMR_WIFI_CONN_ERROR");
        break;

    case SMR_I2C_INIT_ERROR:
        sprintf(errorString, "SMR_I2C_INIT_ERROR");
        break;

    case SMR_SPI_INIT_ERROR:
        sprintf(errorString, "SMR_SPI_INIT_ERROR");
        break;

    case SMR_ADC_INIT_ERROR:
        sprintf(errorString, "SMR_ADC_INIT_ERROR");
        break;

    case SMR_MQTT_CONN_ERROR:
        sprintf(errorString, "SMR_MQTT_CONN_ERROR");
        break;

    case SMR_MCP3008_INIT_ERROR:
        sprintf(errorString, "SMR_MCP3008_INIT_ERROR");
        break;

    case SMR_MPU6050_INIT_ERROR:
        sprintf(errorString, "SMR_MPU6050_INIT_ERROR");
        break;

    case SMR_ADC_READ_ERROR:
        sprintf(errorString, "SMR_ADC_READ_ERROR");
        break;

    case SMR_MPU6050_READ_ERROR:
        sprintf(errorString, "SMR_MPU6050_READ_ERROR");
        break;

    case SMR_MCP3008_READ_ERROR:
        sprintf(errorString, "SMR_MCP3008_READ_ERROR");
        break;

    case SMR_MLX3096_READ_ERROR:
        sprintf(errorString, "SMR_MLX3096_READ_ERROR");
        break;

    case SMR_MQTT_PUBLISH_ERROR:
        sprintf(errorString, "SMR_MQTT_PUBLISH_ERROR");
        break;

    case SMR_DS3231_GETTING_ERROR:
        sprintf(errorString, "SMR_DS3231_GETTING_ERROR");
        break;

    case SMR_DS3231_SETING_ERROR:
        sprintf(errorString, "SMR_DS3231_SETING_ERROR");
        break;
    }
    sprintf(retString, "An error of the type %s has occurred", errorString);
}

/**
 * @brief This function saves the new operating time value of the equipment in flash memory.
 * 
 * @return esp_err_t  0 -> No error.
 */
esp_err_t smr_save_run_time(void)
{
    nvs_handle_t nvs_handle;
    esp_err_t err;
    size_t required_size = 0; 

    err = nvs_open(STORAGE_NAMESPACE, NVS_READWRITE, &nvs_handle);
    if (err != ESP_OK) 
        return err;

    err = nvs_get_blob(nvs_handle, "run_time", NULL, &required_size);
    if (err != ESP_OK && err != ESP_ERR_NVS_NOT_FOUND) return err;


    uint32_t* run_time = malloc(required_size + sizeof(uint32_t));
    if (required_size > 0) 
    {
        err = nvs_get_blob(nvs_handle, "run_time", run_time, &required_size);
        if (err != ESP_OK) 
        {
            free(run_time);
            return err;
        }
    }

    required_size += sizeof(uint32_t);
    run_time[required_size / sizeof(uint32_t) - 1] = xTaskGetTickCount() * portTICK_PERIOD_MS;
    err = nvs_set_blob(nvs_handle, "run_time", run_time, required_size);
    free(run_time);

    if (err != ESP_OK) 
        return err;

    err = nvs_commit(nvs_handle);
    if (err != ESP_OK) return err;

    nvs_close(nvs_handle);
    return ESP_OK;
}

/**
 * @brief This function is responsible for storing the error code that caused the equipment to restart in flash memory.
 * 
 * @param lastError     Error code that caused restart.
 * @return esp_err_t    0 -> No error.
 */
esp_err_t smr_save_last_error(uint8_t lastError)
{
    nvs_handle_t nvs_handle;
    esp_err_t err;

    // Open
    err = nvs_open(STORAGE_NAMESPACE, NVS_READWRITE, &nvs_handle);
    if (err != ESP_OK) 
        return err;

    uint8_t last_saved_error = 0; 
    err = nvs_get_u8(nvs_handle, "restart_conter", &last_saved_error);
    if (err != ESP_OK && err != ESP_ERR_NVS_NOT_FOUND) 
        return err;

    last_saved_error = lastError;
    err = nvs_set_i32(nvs_handle, "restart_conter", last_saved_error);
    if (err != ESP_OK) 
        return err;

    err = nvs_commit(nvs_handle);
    if (err != ESP_OK) 
        return err;

    nvs_close(nvs_handle);
    return ESP_OK;
}

/**
 * @brief This function is used to print the information stored in flash memory.
 * 
 * @return esp_err_t    0 -> No error
 */
esp_err_t smr_print_nvs_saved(void)
{
    nvs_handle_t nvs_handle;
    esp_err_t err;
    char errorString[100];

    err = nvs_open(STORAGE_NAMESPACE, NVS_READWRITE, &nvs_handle);
    if (err != ESP_OK) 
        return err;

    uint8_t last_error = 0; 
    err = nvs_get_i32(nvs_handle, "restart_conter", &last_error);
    if (err != ESP_OK && err != ESP_ERR_NVS_NOT_FOUND) 
        return err;
    smr_error_reg((smr_errorCtrl_t) last_error, errorString);

#ifdef DEBUG
    ESP_LOGI(TAG, "The last error occured was: %s", errorString);
#endif


    size_t required_size = 0;

    err = nvs_get_blob(nvs_handle, "run_time", NULL, &required_size);
    if (err != ESP_OK && err != ESP_ERR_NVS_NOT_FOUND) 
        return err;

    if (required_size == 0) 
    {

#ifdef DEBUG
        ESP_LOGI(TAG, "Run time is: Nothing saved yet!");
#endif
    } 
    else 
    {
        uint32_t* run_time = malloc(required_size);
        err = nvs_get_blob(nvs_handle, "run_time", run_time, &required_size);
        if (err != ESP_OK) 
        {
            free(run_time);
            return err;
        }
        for (int i = 0; i < required_size / sizeof(uint32_t); i++) 
        {
#ifdef DEBUG
        ESP_LOGI(TAG, "%d: %lu", i + 1, run_time[i]);
#endif
        }
        free(run_time);
    }

    nvs_close(nvs_handle);
    return ESP_OK;
}