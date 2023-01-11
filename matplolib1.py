import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


plt.rcParams['toolbar'] = 'None'

# 1. Linspace
N = 600
# Sample spacing
tmax = 3/4
T = tmax / N # =1.0 / 800.0
x1 = np.linspace(0.0, N*T, N)
y1 = np.sin(50.0 * 2.0*np.pi*x1) + 0.5*np.sin(80.0 * 2.0*np.pi*x1)
yf1 = scipy.fftpack.fft(y1)
xf1 = np.linspace(0.0, 1.0/(2.0*T), N//2)

fig, ax = plt.subplots()
# Plotting only the left part of the spectrum to not show aliasing
ax.plot(xf1, 2.0/N * np.abs(yf1[:N//2]), label='fftpack tutorial')
plt.legend()
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Amplitud[dB]")
plt.grid()
plt.show()