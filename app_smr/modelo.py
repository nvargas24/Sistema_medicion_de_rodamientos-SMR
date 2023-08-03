# No es el metodo mas apropiado, deberia usarse un observador para los cambios realizados
from PySide2.QtGui import *

class Option():    
    # --- Metodos que accede al hacer click --#
    def select(self, window):
        self.op_select = window.ui.comboBox_seleccion.currentText()
        print("Se verifica option elegida")
        print("Opening elegido %s" %self.op_select)

        if self.op_select == "Demon Slayer":
            window.ui.image.setPixmap(QPixmap("demon_slayer.jpeg"))
            window.ui.image.setScaledContents(True)
        if self.op_select == "Chainsaw Man":
            window.ui.image.setPixmap(QPixmap("chainsawman.jpeg"))
            window.ui.image.setScaledContents(True)
        if self.op_select == "Los Caballeros del Zodiaco":
            window.ui.image.setPixmap(QPixmap("caballeros_zodiaco.jpeg"))
            window.ui.image.setScaledContents(True)
        if self.op_select == "Nier Automata":
            window.ui.image.setPixmap(QPixmap("nier_automata.jpeg"))
            window.ui.image.setScaledContents(True)
        if self.op_select == "luz":
            window.ui.image.setPixmap(QPixmap("luz.png"))
            window.ui.image.setScaledContents(True)            

    def url_op(self, window): pass

    def input_user(self, parent):
        self.parent = parent # Accedo a atributos de clase WindowLogin
        # Obtengo valores ingresador a los QLine
        self.name = self.parent.ui.usuario.text()
        self.contra = self.parent.ui.contrasenia.text()

        print("Usuario: %s" %self.name)
        print("Contraseña: %s"%self.contra)
        
        if self.name == "lab" and self.contra == "elect":
            # Abro ventana principal una vez verificado el usuario
            self.parent.windows.window_main.show() # Accedo a atributos de clase controlador, especificamente al objeto window_main
            self.parent.close()
        else:
            print("Usuario y contraseña incorrecta")
            # Al no ser correcto los datos ingresados limpio los QLine
            self.parent.ui.usuario.clear()
            self.parent.ui.contrasenia.clear()

