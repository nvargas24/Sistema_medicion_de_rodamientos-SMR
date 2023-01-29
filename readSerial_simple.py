import serial
import json
from time import sleep

ser=serial.Serial('COM3', 115200, timeout=1, write_timeout=1)

while True:
    try:
        dato=ser.readline()
        dato=dato.decode('utf-8') #se interpresta como caracteres segun la unicode

        if (dato.find("}")>=0 and dato.find("{")==0):
            data_serial = dato[0:dato.find("}")+1]
            json_data = json.loads(data_serial)
            print(json_data["Type"])
            print(json_data["Index"])
            print(json_data["Value"])
    except:
        print("Cerrar puerto")
        ser.close()
        break