import time
import tkinter as tk

timer_running = False
start_time = 0
times_list = []

# Función para guardar el valor del temporizador en un archivo de texto
def save_time(time):
    with open("timer.txt", "w") as f:
        f.write(str(time))

# Función para leer el valor del temporizador guardado en el archivo de texto
def read_time():
    try:
        with open("timer.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

# Función que se ejecuta cuando se hace clic en el botón
def button_click():
    global timer_running, start_time
    
    if not timer_running:
        # Iniciar un nuevo temporizador
        timer_running = True
        start_time = time.time()
        label.config(text="Temporizador iniciado.")
        button.config(text="Restablecer")
    else:
        # Detener el temporizador y guardar el valor actual
        timer_running = False
        elapsed_time = time.time() - start_time
        label.config(text="Temporizador detenido. Tiempo transcurrido: " + time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
        button.config(text="Iniciar")
        save_time(elapsed_time)
        times_list.append(time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
    
    # Actualizar la etiqueta del tiempo transcurrido
    label_time.config(text="Tiempo transcurrido: 00:00:00")

# Función para actualizar el tiempo transcurrido cada segundo
def update_time():
    global timer_running, start_time
    if timer_running:
        # Mostrar el tiempo transcurrido desde que se inició el temporizador actual
        elapsed_time = time.time() - start_time
        label_time.config(text="Tiempo transcurrido: " + time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
    # Actualizar la etiqueta cada 1000 milisegundos (1 segundo)
    label_time.after(1000, update_time)

# Crear la ventana principal
window = tk.Tk()
window.title("Temporizador")

# Crear la etiqueta para mostrar el estado del temporizador
label = tk.Label(window, text="Presione el botón para iniciar el temporizador.")
label.pack(pady=10)

# Crear la etiqueta para mostrar el tiempo transcurrido
label_time = tk.Label(window, text="Tiempo transcurrido: 00:00:00")
label_time.pack()

# Crear el botón para iniciar o restablecer el temporizador
button = tk.Button(window, text="Iniciar", command=button_click)
button.pack(pady=10)

# Leer el valor del temporizador guardado en el archivo de texto
elapsed_time = read_time()

# Si hay un valor guardado, mostrarlo en la etiqueta del tiempo transcurrido
if elapsed_time > 0:
    label_time.config(text="Tiempo transcurrido: " + time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))
    times_list.append(time.strftime('%H:%M:%S', time.gmtime(elapsed_time)))

# Actualizar el tiempo transcurrido cada segundo
update_time()

# Ejecutar la ventana principal
window.mainloop()

# Imprimir la lista de tiem
