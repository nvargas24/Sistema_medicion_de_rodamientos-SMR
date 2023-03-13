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

/* Defines */
#define DEBUG
#define ROD_ANT
//#define ROD_POS

#define HIGH 1
#define LOW  0

#define LOW_BATTERY 3000
#define SLEEP       6000


#define WIFI_STATE_LED  GPIO_NUM_2
#define BATT_STATE_LED  GPIO_NUM_4
#define RTC_RST_PIN     GPIO_NUM_12


/* Function prototypes */
esp_err_t adc_init(void);
esp_err_t i2c_master_init(void);
static esp_err_t spi_init(void);
static void log_error_if_nonzero(const char *message, int error_code);
static void mqtt_event_handler(void *handler_args, esp_event_base_t base, int32_t event_id, void *event_data);
static esp_err_t mqtt_init(void);
void measure_sensors(void);
esp_err_t configure_gpios(void);
void init_peripherals(void);
void adc_read(int *batteryLevel);
void publish_measures(void);


/* Global Variables */
esp_mqtt_client_handle_t client;
spi_device_handle_t spi3;
esp_adc_cal_characteristics_t *adc_chars;
static const adc_channel_t  vBatLvl = ADC_CHANNEL_6;

float Ta;
float To;
float Td;
float accel[3];
float frecBPFI;
float frecBPFO;
float frecBSF;
float frecFTF;
int batteryLevel;
float tempThreshold;
float axialThreshold;
float radialThreshold;
bool axialAlarm = false;
bool radialAlarm = false;
bool alarmTemp = false;
bool presBPFO = false;
bool presBPFI = false;
bool presFTF = false;
bool presBSF = false;
bool run = false;

char aux[200];

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

    init_peripherals();

    while(1)
    {
#ifdef DEBUG
        ESP_LOGI(TAG, "run = %d", run);
        vTaskDelay(pdMS_TO_TICKS(SLEEP*3));
        gpio_set_level(WIFI_STATE_LED, 0);
#endif
        if(run)
        {
            //measure_sensors();
            //publish_measures(); 
            gpio_set_level(WIFI_STATE_LED, HIGH);
            /*
            vTaskDelay(pdMS_TO_TICKS(SLEEP));
            ESP_LOGI(TAG, "BFPI: %f", frecBPFI);
            vTaskDelay(pdMS_TO_TICKS(3));
            */
            ESP_LOGI(TAG, "BFP0: %f", frecBPFO);
            
            /*
            vTaskDelay(pdMS_TO_TICKS(3));
            ESP_LOGI(TAG, "BSF: %f", frecBSF);
            vTaskDelay(pdMS_TO_TICKS(3));
            ESP_LOGI(TAG, "FTF: %f", frecFTF);
            */
            gpio_set_level(WIFI_STATE_LED, LOW);
            vTaskDelay(pdMS_TO_TICKS(SLEEP));
        }
    }
    
}

/**
 * @brief This function is used to configurate de ADC Channel 1
 * 
 */
esp_err_t adc_init(void)
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
esp_err_t i2c_master_init(void)
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
static esp_err_t spi_init(void)
{
    esp_err_t ret;

    gpio_reset_pin(SPI_CS_PIN);
    gpio_set_direction(SPI_CS_PIN, GPIO_MODE_OUTPUT);
    gpio_set_level(SPI_CS_PIN, 1);

    spi_bus_config_t buscfg =
    {
    .miso_io_num = SPI_MISO_PIN,
    .mosi_io_num = SPI_MOSI_PIN,
    .sclk_io_num = SPI_CLK_PIN,
    .quadwp_io_num = -1,
    .quadhd_io_num = -1,
    };

    ret = spi_bus_initialize(SPI3_HOST, &buscfg, SPI_DMA_CH_AUTO);
    assert(ret == ESP_OK);

    spi_device_interface_config_t devcfg = 
    {
        .clock_speed_hz = SPI_MASTER_FREQ_11M ,
        .mode = 0,
        .spics_io_num = SPI_CS_PIN,
        .queue_size = 1,
        .flags = SPI_DEVICE_NO_DUMMY ,
    };

    ESP_ERROR_CHECK(spi_bus_add_device(SPI3_HOST, &devcfg, &spi3));

    ret = spi_bus_add_device(SPI3_HOST, &devcfg, &spi3);
	
    return ret;
}

/**
 * @brief This function is used to log all the errors
 * 
 * @param message  String that indicates the error
 * @param error_code Error code number 
 */
static void log_error_if_nonzero(const char *message, int error_code)
{
    if (error_code != 0) {
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
static void mqtt_event_handler(void *handler_args, esp_event_base_t base, int32_t event_id, void *event_data)
{
    //ESP_LOGD(TAG, "Event dispatched from event loop base=%s, event_id=%d", base, event_id);
    esp_mqtt_event_handle_t event = event_data;
    esp_mqtt_client_handle_t client = event->client;
    int msg_id;
    switch ((esp_mqtt_event_id_t)event_id) {
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

        //msg_id = esp_mqtt_client_unsubscribe(client, "/topic/qos1");
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
        if(strcmp(aux, "smr/start") == 0)
        {
            run = true;
        }
        else if(strcmp(aux, "smr/stop") == 0)
        {
            run = false;
        }
        else if(strcmp(aux, "tempThreshold") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            tempThreshold = strtof(aux, NULL);
        }
        else if(strcmp(aux, "axialThreshold") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            axialThreshold = strtof(aux, NULL);
        }
        else if(strcmp(aux, "radialThreshold") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            radialThreshold = strtof(aux, NULL);
        }

#ifdef ROD_ANT
        else if(strcmp(aux, "rodAnt/frecBPFI") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFI = strtof(aux, NULL);
        }
        else if(strcmp(aux, "rodAnt/frecBPFO") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFO = strtof(aux, NULL);
        }
        else if(strcmp(aux, "rodAnt/frecBSF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBSF = strtof(aux, NULL);
        }
        else if(strcmp(aux, "rodAnt/frecFTF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecFTF = strtof(aux, NULL);
        }
#endif

#ifdef ROD_POS
        else if(strcmp(aux, "rodPos/frecBPFI") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFI = strtof(aux, NULL);
        }
        else if(strcmp(aux, "rodPos/frecBPFO") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBPFO = strtof(aux, NULL);
        }
        else if(strcmp(aux, "rodPos/frecBSF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecBSF = strtof(aux, NULL);
        }
        else if(strcmp(aux, "rodPos/frecFTF") == 0)
        {
            sprintf(aux, "%.*s", event->data_len, event->data);
            frecFTF = strtof(aux, NULL);
        }
#endif
        
//#endif
        break;
    case MQTT_EVENT_ERROR:
#ifdef DEBUG
        ESP_LOGI(TAG, "MQTT_EVENT_ERROR");
#endif
        if (event->error_handle->error_type == MQTT_ERROR_TYPE_TCP_TRANSPORT) {
            log_error_if_nonzero("reported from esp-tls", event->error_handle->esp_tls_last_esp_err);
            log_error_if_nonzero("reported from tls stack", event->error_handle->esp_tls_stack_err);
            log_error_if_nonzero("captured as transport's socket errno",  event->error_handle->esp_transport_sock_errno);
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
static esp_err_t mqtt_init(void)
{
    esp_err_t ret;
    
    esp_mqtt_client_config_t mqtt_cfg = 
    {
        .broker.address.hostname = "192.168.1.109",
    };
    client = esp_mqtt_client_init(&mqtt_cfg);
    esp_mqtt_client_register_event(client, ESP_EVENT_ANY_ID, mqtt_event_handler, NULL);
    ret = esp_mqtt_client_start(client);
    return ret;
}

/**
 * @brief This function is used to perform sensor's measurement
 * 
 */
void measure_sensors(void)
{
    /* Acceleration measures */
    /* Considero ahora que la aceleración en X es la axial y radial en Y */
    ESP_ERROR_CHECK(MPU6050_ReadAccelerometer(accel, 3));
#ifdef DEBUG
    ESP_LOGI(TAG, "AccelX = %f", accel[0]);
    ESP_LOGI(TAG, "AccelY = %f", accel[1]);
    ESP_LOGI(TAG, "AccelZ = %f", accel[2]);
#endif
    if(accel[0] >= axialThreshold)
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
    if(accel[1] >= radialThreshold)
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

    /* Temperature measures */
    ESP_ERROR_CHECK(MLX90614_GetTa(&Ta));
    ESP_ERROR_CHECK(MLX90614_GetTo(&To));
#ifdef DEBUG
    ESP_LOGI(TAG, "Temperatura Ambiente = %f", Ta);
    ESP_LOGI(TAG, "Temperatura Objetivo = %f", To);
#endif 
    Td = To - Ta;
    if(Td > tempThreshold)
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

    /* Battery level measurement */
    adc_read(&batteryLevel);
    if(batteryLevel <= LOW_BATTERY)
    {
        gpio_set_level(BATT_STATE_LED, HIGH);
#ifdef DEBUG
        ESP_LOGI(TAG, "BATERIA BAJA ---- %d", batteryLevel);
#endif
    }
    else
    {
        gpio_set_level(BATT_STATE_LED, LOW);
    }

    /* FFT measures */
    /* Ver lógica de mediciones y como comparar los resultados contra una base de ruido 
     * Disparar alarmas segun lo recibido por mqtt
     * #ifdef para posibles prints de info
    */
}

/**
 * @brief This function is used to publish MQTT messages
 * 
 */
void publish_measures(void)
{
    char payload[100];

#ifdef ROD_ANT
    sprintf(payload, "%d", batteryLevel);
    esp_mqtt_client_publish(client, "rodAnt/bateria", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", Ta);
    esp_mqtt_client_publish(client, "rodAnt/tempAmb", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", To);
    esp_mqtt_client_publish(client, "rodAnt/tempObj", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", accel[0]);
    esp_mqtt_client_publish(client, "rodAnt/acelAxial", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", accel[1]);
    esp_mqtt_client_publish(client, "rodAnt/acelRadial", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presBPFO);
    esp_mqtt_client_publish(client, "rodAnt/presBPFO", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presBPFI);
    esp_mqtt_client_publish(client, "rodAnt/presBPFI", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presBSF);
    esp_mqtt_client_publish(client, "rodAnt/presBSF", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presFTF);
    esp_mqtt_client_publish(client, "rodAnt/presFTF", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", alarmTemp);
    esp_mqtt_client_publish(client, "rodAnt/alarmTemp", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", axialAlarm);
    esp_mqtt_client_publish(client, "rodAnt/alarmAcelAxial", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", radialAlarm);
    esp_mqtt_client_publish(client, "rodAnt/alarmAcelRadial", payload, strlen(payload), 0, false);
#endif
#ifdef ROD_POS
    sprintf(payload, "%d", batteryLevel);
    esp_mqtt_client_publish(client, "rodPos/bateria", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", Ta);
    esp_mqtt_client_publish(client, "rodPos/tempAmb", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", To);
    esp_mqtt_client_publish(client, "rodPos/tempObj", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", accel[0]);
    esp_mqtt_client_publish(client, "rodPos/acelAxial", payload, strlen(payload), 0, false);
    sprintf(payload, "%f", accel[1]);
    esp_mqtt_client_publish(client, "rodPos/acelRadial", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presBPFO);
    esp_mqtt_client_publish(client, "rodPos/presBPFO", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presBPFI);
    esp_mqtt_client_publish(client, "rodPos/presBPFI", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presBSF);
    esp_mqtt_client_publish(client, "rodPos/presBSF", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", presFTF);
    esp_mqtt_client_publish(client, "rodPos/presFTF", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", alarmTemp);
    esp_mqtt_client_publish(client, "rodPos/alarmTemp", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", axialAlarm);
    esp_mqtt_client_publish(client, "rodPos/alarmAcelAxial", payload, strlen(payload), 0, false);
    sprintf(payload, "%d", radialAlarm);
    esp_mqtt_client_publish(client, "rodPos/alarmAcelRadial", payload, strlen(payload), 0, false);
#endif
#ifdef DEBUG 
    ESP_LOGI(TAG, "Publish done!");
#endif
}

/**
 * @brief This function is used to configure all the GPIOs
 * 
 */
esp_err_t configure_gpios(void)
{
    int ret;
    gpio_reset_pin(WIFI_STATE_LED);
    ret = gpio_set_direction(WIFI_STATE_LED, GPIO_MODE_OUTPUT);
    gpio_reset_pin(BATT_STATE_LED);
    ret =gpio_set_direction(BATT_STATE_LED, GPIO_MODE_OUTPUT);
    gpio_reset_pin(RTC_RST_PIN);
    ret = gpio_set_direction(RTC_RST_PIN, GPIO_MODE_OUTPUT);

    return ret;
}

/**
 * @brief This function is used to initialize all the peripherals
 * 
 */
void init_peripherals(void)
{
#ifdef DEBUG
    ESP_LOGI(TAG, "[APP] Startup..");
    //ESP_LOGI(TAG, "[APP] Free memory: %d bytes", esp_get_free_heap_size());
    ESP_LOGI(TAG, "[APP] IDF version: %s", esp_get_idf_version());
#endif
    ESP_ERROR_CHECK(nvs_flash_init());
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    ESP_ERROR_CHECK(configure_gpios());
#ifdef DEBUG
    ESP_LOGI(TAG, "GPIOs initialized successfully");
#endif
    ESP_ERROR_CHECK(example_connect());
    gpio_set_level(WIFI_STATE_LED, HIGH);
    ESP_ERROR_CHECK(i2c_master_init());
#ifdef DEBUG
    ESP_LOGI(TAG, "I2C initialized successfully");
#endif
    ESP_ERROR_CHECK(spi_init());
#ifdef DEBUG
    ESP_LOGI(TAG, "SPI initialized successfully");
#endif
    ESP_ERROR_CHECK(adc_init());
#ifdef DEBUG
    ESP_LOGI(TAG, "ADC initialized successfully");
#endif
    ESP_ERROR_CHECK(mqtt_init());


    //ESP_ERROR_CHECK(MPU6050_Init(MPU6050_DataRate_100Hz, MPU6050_Accelerometer_2G, MPU6050_GyroSens_250));
}

/**
 * @brief This function is used to get an ADC read.
 * 
 * @param batteryLevel Placeholder for the ADC measure.
 */
void adc_read(int *batteryLevel)
{
    //*(batteryLevel) = esp_adc_cal_raw_to_voltage(adc1_get_raw(vBatLvl), &adc_chars);
}