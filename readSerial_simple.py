import serial
import json
from time import sleep
x=[]
y=[]

ser=serial.Serial('COM3', 115200, timeout=1, write_timeout=1)
print("Se habilita lectura de puerto COM3")
sleep(0.2)

while True:
    dato=ser.readline()
    dato=dato.decode("utf-8", errors="replace") #se interpreta como caracteres segun unicode
    sleep(0.01)
    if (dato.find("}")>=0 and dato.find("{")==0):
        data_serial = dato[0:dato.find("}")+1]
        json_data = json.loads(data_serial)


        if json_data["Type"]=="Freq":
            x.insert(json_data["Index"], json_data["Value"])
        elif json_data["Type"]=="Amp":
            y.insert(json_data["Index"], json_data["Value"])
    
        if json_data["Index"]==511:
            print("-"*20)
            print("Termino carga de datos nuevos")

    print("-"*40)
    print(len(x))
    """
    print("Frecuencia:")
    for i in range(len(x)):
        print(x[i])
    
    print("Amplitudes:")
    for i in range(len(y)):
        print(y[i])
    """