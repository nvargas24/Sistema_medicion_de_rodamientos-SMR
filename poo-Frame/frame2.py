from sys import exit 
from tkinter import * 
from frame1 import Hola 

root = Tk() 
root.geometry("500x300") 
parent = Frame(root, bg="red", bd=10, relief=SUNKEN, width=1000, height=100)
parent.pack(expand=YES, fill=X)
parent.pack_propagate(False) # para utilizar las dimensiones establecidas y no adaptarse a los widgets que tenga

Hola(parent).pack(side=RIGHT)
Button(parent, text='Agregado', command=exit).pack(side=LEFT)

root.mainloop() 