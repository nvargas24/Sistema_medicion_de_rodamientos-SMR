from tkinter import * 

class Hola(Frame): 
    def __init__(self, parent=None, **config):
        Frame.__init__(self, parent)
        self.pack() 
        self.data = 0 
        self.agregar_boton1(**config) 
        self.agregar_boton2() 

    def agregar_boton1(self, **config): 
        widget = Button(self, text='Botón 1!', command=self.valor_de_variable)
        widget.config(**config)
        widget.pack(side=LEFT)

    def agregar_boton2(self): 
        self.widget = Button(self, text='Boton', command=self.valor_de_variable)
        self.widget.pack(side=LEFT)

    def valor_de_variable(self):
        self.data += 1
        self.widget.configure(text=f'Boton({self.data})') #para mostrar valor de contador en boton
        #self.widget.configure(text="Cambie por hacer clic")
        print('Valor %s!' % self.data)

def valorfunc():
    print("soy un funcion independiente")

if __name__ == '__main__': 
    obj2=Hola()
    obj2.mainloop()
