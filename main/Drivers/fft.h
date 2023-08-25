/**
 * @file fft.h
 * 
 * @author Team SMR
 * @authors Galassi, Fernando
 * @authors Moran, Nicolas
 * @authors	Pilato, Bruno
 * @authors	Vargas, Nahuel
 *
 * @brief Header file for fft.c
 * @version 0.1
 * @date 2022-08-30
 * 
 * @copyright Copyright (c) 2022
 * 
 */
#ifndef __FFT_H__
#define __FFT_H__

/* Macros para FFT */
#define ADC_SAMPLES 1024
#define FFT_SAMPLES 512
#define RESOLUTION_F 37  // Hz
#define SWEEP_FFT 5
#define SNR -100
#define TOL_SNR 3

typedef enum
{
  FFT_REAL,
  FFT_COMPLEX
} fft_type_t;

typedef enum
{
  FFT_FORWARD,
  FFT_BACKWARD
} fft_direction_t;

#define FFT_OWN_INPUT_MEM 1
#define FFT_OWN_OUTPUT_MEM 2

typedef struct
{
  int size;  // FFT size
  float *input;  // pointer to input buffer
  float *output; // pointer to output buffer
  float *twiddle_factors;  // pointer to buffer holding twiddle factors
  fft_type_t type;   // real or complex
  fft_direction_t direction; // forward or backward
  unsigned int flags; // FFT flags
} fft_config_t;

fft_config_t *fft_init(int size, fft_type_t type, fft_direction_t direction, float *input, float *output);
void fft_destroy(fft_config_t *config);
void fft_execute(fft_config_t *config);
void fft(float *input, float *output, float *twiddle_factors, int n);
void ifft(float *input, float *output, float *twiddle_factors, int n);
void rfft(float *x, float *y, float *twiddle_factors, int n);
void irfft(float *x, float *y, float *twiddle_factors, int n);
void fft_primitive(float *x, float *y, int n, int stride, float *twiddle_factors, int tw_stride);
void split_radix_fft(float *x, float *y, int n, int stride, float *twiddle_factors, int tw_stride);
void ifft_primitive(float *input, float *output, int n, int stride, float *twiddle_factors, int tw_stride);
void fft8(float *input, int stride_in, float *output, int stride_out);
void fft4(float *input, int stride_in, float *output, int stride_out);

esp_err_t rfft_calcule(int16_t *meas_mcp, float *mag_fft, float *freq_fft);
float searchFreq(float freq_s, int tol, float *mag_fft, float*freq_fft);
float obtener_snr(float *mag_fft);

#endif // __FFT_H__
