import serial
from time import sleep

ser=serial.Serial('COM3', 115200, timeout=1, write_timeout=1)

while True:
    sleep(0.2)
    dato=ser.readline()
    dato=dato.decode('utf-8') #se interpresta como caracteres segun la unicode

    print(dato)
    print(dato.find("{"))
    print(dato.find("}"))

    if dato.find("}")>=0 and dato.find("{")==0:
        print("Encontrado")
        print(dato[1:dato.find("}")])
    else:
        print("No encotrado")

    print("-"*30)