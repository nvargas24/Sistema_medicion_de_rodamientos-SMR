import serial
import json
from time import sleep
x=[]
y=[]
json_data={}

ser=serial.Serial('COM3', 115200, timeout=1, write_timeout=1)
print("Se habilita lectura de puerto COM3")


while True:
    sleep(0.01)
    dato=ser.readline()
    dato=dato.decode("utf-8", errors="ignore")

    if (dato.find("}")>=0 and dato.find("{")==0):
        data_serial = dato[0:dato.find("}")+1]
        json_data = json.loads(data_serial)
    print(json_data.keys())
    #if json_data["Type"]=="Freq":
        #x.insert(json_data["Index"], json_data["Value"])
        #elif json_data["Type"]=="Amp":
        #    y.insert(json_data["Index"], json_data["Value"])
    """
    if json_data["Index"]==511:
        print("-"*20)
        print("Termino carga de datos nuevos")
        break
    """
print("-"*40)
print(len(x))

print("Frecuencia:")
for i in range(len(x)):
    print(x[i])

"""
print("Amplitudes:")
for i in range(len(y)):
    print(y[i])
"""

ser.close()