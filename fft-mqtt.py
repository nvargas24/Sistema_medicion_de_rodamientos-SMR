import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
import paho.mqtt.client as mqtt
import tkinter as tk

MUESTRAS_FFT = 512

x=[]
y=[]

def cerrar():
    root.quit()

def init_fft():
    client.publish("smr/start", 1)
    print("Inicia lectura de datos")

def finish_fft():
    client.publish("smr/stop", 1)
    plt.clf() # Limpiar gráfico anterior
    print("Finalizo conexion para recibir datos")

# Función que se llama cuando se recibe un mensaje MQTT
def on_message(client, userdata, msg):
    global x
    global y

    message = msg.payload.decode()
    values_str = message.split(",")
    y = [float(value) for value in values_str]
    print("Se actualiza datos de fft")
    plt.clf() # Limpiar gráfico anterior
    plt.plot(x, y)
    plt.title("Sweep FFT")
    plt.xlabel("Frecuencia[kHz]")
    plt.ylabel("Amplitud[dBV]")
    plt.xlim(-100, 19000) # Establecer límites del eje X
    plt.ylim(-40, 60) # Establecer límites del eje Y
    canvas.draw() # Actualizar gráfico

#completa array de float para resolucion de frecuencia de 37Hz
for i in range(MUESTRAS_FFT):
    x.append(37*i)

# Crear ventana de Tkinter
root = tk.Tk()
root.title("Test fft con MQTT")
root.geometry("500x400")
style.use("bmh")

# Crear lienzo para el gráfico
fig, ax = plt.subplots(figsize=(4, 3), dpi=70)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Establecer límites del eje X e Y
ax.set_xlim(-100, 19000)
ax.set_ylim(-40, 60)

plt.title("Sweep FFT")
plt.xlabel("Frecuencia[Hz]")
plt.ylabel("Amplitud[dBV]")

#crea botton e ventana principal
btn_cerrar=tk.Button(root, text="Cerrar", command=cerrar)
btn_finish = tk.Button(root, text="Finalizar conexion", command=finish_fft)
btn_init = tk.Button(root, text="Iniciar conexion", command=init_fft)

btn_cerrar.pack(side=tk.BOTTOM)
btn_finish.pack(side=tk.BOTTOM)
btn_init.pack(side=tk.BOTTOM)

# Conectar al servidor MQTT y suscribirse al tema "/mytopic"
client = mqtt.Client()
client.connect("192.168.1.110", 1883)
client.subscribe("rodAnt/fft")
client.on_message = on_message
client.loop_start()

# Iniciar bucle de eventos de Tkinter
root.mainloop()