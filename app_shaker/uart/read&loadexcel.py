import serial
import time
import pandas as pd

def found_letras(raw_data):
    alpha = "qwertyuiopasdfghjklñzxcvbnm"
    for letra in alpha:
        if letra in raw_data.lower():
            return True
    
    return False

ser = serial.Serial('COM3', 115200)
time.sleep(2)

data_columns = ["x", "y", "z"]
data = pd.DataFrame(columns = data_columns)

try:
    print("Inicia lectura")
    while True:
        raw_data = ser.readline().decode("utf-8", errors="ignore").strip()
        if raw_data and not found_letras(raw_data):
            x, y, z = map(float, raw_data.split('\t'))
            data.loc[len(data)] = [x, y, z]
        time.sleep(0.005)            
except KeyboardInterrupt:
    print("Finaliza lectura")
    ser.close()

print("Se guarda en archivo: test_cal_accel.xlsx")
data.to_excel("test_cal_accel.xlsx", index = False)


