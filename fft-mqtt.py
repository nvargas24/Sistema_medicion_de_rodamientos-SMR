import tkinter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style

MUESTRAS_FFT = 512
TIME_SWEEP = 100 #mseconds 

x1=[]
y1=[]

plt.rcParams['toolbar'] = 'None'

for i in range(MUESTRAS_FFT):
    x1.append(37*i)

for j in range(MUESTRAS_FFT):
    y1.append(-15)

root = tkinter.Tk()
root.wm_title("Grafica test")
ta=root.geometry("700x420")

style.use("bmh")

fig=Figure(dpi=60)
graph=fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

cont=0

def animate(i):
    global cont
    print("actualizar grafica")

    graph.clear() 
    graph.plot(x1, y1)

# animacion para actualizar datos de grafico
ani = animation.FuncAnimation(fig, animate, interval=TIME_SWEEP)
plt.show()

def cerrar():
    root.quit()

button=tkinter.Button(master=root, text="cerrar", command=cerrar)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()