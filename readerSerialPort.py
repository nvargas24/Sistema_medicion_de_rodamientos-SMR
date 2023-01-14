from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import *
from math import *
 
root = Tk()
root.wm_title("Graficador")
ta=root.geometry("1000x700")
 
style.use('fivethirtyeight')
 
fig = Figure()
ax1 = fig.add_subplot(111)
 
canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=root.TOP, fill=root.BOTH, expand=1)
 

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
 
et = root.Entry(master=root,width=60)
et.config(bg="gray87", justify="left")
 
button = root.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=root.BOTTOM)
 
et.pack(side=root.BOTTOM)
ets=root.Entry(master=root,width=20)
ets.config(bg="gray87")
ets.pack(side=root.RIGHT)

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4")
tree.column("#0", width=50, minwidth=50)
tree.column("col1", width=144, minwidth=144, anchor="center")
tree.column("col2", width=80, minwidth=80, anchor="center")
tree.heading("#0", text="ID")
tree.heading("col1", text="Frecuencia[Hz]")
tree.heading("col2", text="Amplitud[dBV]")

tree.grid(column=0, row=11, columnspan=6, padx=50, pady=40)

root.mainloop()