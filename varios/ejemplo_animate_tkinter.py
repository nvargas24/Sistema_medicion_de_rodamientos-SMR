import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *
 
root = tkinter.Tk()
root.wm_title("Graficador")
ta=root.geometry("1000x700")
 
style.use('fivethirtyeight')
 
fig = Figure()
ax1 = fig.add_subplot(111)
 
canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
 

def animate(i):
    x = np.arange(0, 10, .01)#.01
    try:
        solo=eval("np.sin(x)")
        ax1.clear()
        ax1.plot(x,solo)
    except:
        ax1.plot()

    ani.event_source.stop() #DETIENE ANIMACIÓN
 
def represent(): pass
    
ani = animation.FuncAnimation(fig, animate, interval=500)
 
plt.show()
 
et = tkinter.Entry(master=root,width=60)
et.config(bg="gray87", justify="left")
 
button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=tkinter.BOTTOM)
 
et.pack(side=tkinter.BOTTOM)
ets=tkinter.Entry(master=root,width=20)
ets.config(bg="gray87")
ets.pack(side=tkinter.RIGHT)
 
tkinter.mainloop()