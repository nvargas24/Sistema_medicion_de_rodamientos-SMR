import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Crear los datos iniciales
x_initial = [1, 2, 3, 4, 5]
y_initial = [3, 8, 5, 12, 6]

# Crear una figura y un eje
fig, ax = plt.subplots()

# Ajustar los límites de los ejes
ax.set_xlim(0, 6)
ax.set_ylim(0, 60)

# Crear la línea inicial
line, = ax.plot(x_initial, y_initial)

# Definir el número de pasos para la transición
num_steps = 50
num_int = 1
y_final = [50, 40, 30, 55, 20]

# Función de actualización para la animación
def update(frame, y_final):
    y_interp = np.linspace(y_initial, y_final, num_steps)
    line.set_ydata(y_interp[frame])
    return line,

# Crear la animación
animation = FuncAnimation(fig, update, frames=num_steps, fargs=(y_final,),interval=num_int, blit=True, repeat=False)
# en fargs se agrega ','al final final para que lo tome como tupla
# Mostrar la animación
plt.show()
