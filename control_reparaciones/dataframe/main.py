# installar:
# pip install openpyxl
# tener en cuenta:
# se debe pasar ubicacion relativa de archivo (depende la ubicacion desde se ejecuta el programa - ver terminal)

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import os

import pandas as pd
import numpy as np

# Leer datos desde el archivo Excel (test.xlsx en la misma carpeta)
df = pd.read_excel('control_reparaciones\dataframe\data.xlsx')

# Mostrar los datos del archivo Excel por consola
print("Datos del archivo Excel:")
print(df)

# Calcular la suma de las columnas A y B y guardarla en una nueva columna 'Suma'
df['Suma'] = df['A'] + df['B']

# Crear un nuevo DataFrame solo con la columna de la suma
df_suma = df[['Suma']]

# Calcular el promedio de la columna 'Suma' usando numpy
promedio = np.mean(df_suma['Suma'])

# Mostrar el resultado del promedio en consola
print("\nResultado del promedio:")
print("Promedio:", promedio)

