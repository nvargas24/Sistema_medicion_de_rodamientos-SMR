# No es el metodo mas apropiado, deberia usarse un observador para los cambios realizados

class Option():    
    # --- Metodos que accede al hacer click --#
    def url_op(self, window):
        self.op_select = window.ui.comboBox_seleccion.currentText()
        print("Se verifica option elegida")
        print("Opening elegido %s" %self.op_select)
        # window.ui.image.setPixmap(window.grafico.QPixmap("Imagenes/demon_slayer.jpeg"))

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

