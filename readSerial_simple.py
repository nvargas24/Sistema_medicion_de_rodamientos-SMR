import serial
from time import sleep

try:
    ser=serial.Serial('COM3', 115200)
    #ser.setDTR(False)
    sleep(2)
    #ser.flushInput()
    #ser.setDTR(True)
    while True:
        dato=ser.readline()
        print(dato)
        ser.close()
    
except:
    print("Error, saliendo")

