import serial
from time import sleep

try:
    ser=serial.Serial('COM3', 115200)
    sleep(2)
    while True:
        dato=ser.readline()
        print(dato)
except:
    print("Error, saliendo")
    ser.close()
