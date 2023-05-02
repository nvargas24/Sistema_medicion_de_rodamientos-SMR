
class Option():    
    # --- Metodos que accede al hacer click --#
    def url_op(self, select_combobox):
        self.op_select = select_combobox.comboBox_seleccion.currentText()
        print("Se verifica option elegida")
        print("Opening elegido %s" %self.op_select)

    def input_user(self, parent):
        self.parent = parent
        self.name = self.parent.ui.usuario.text()
        self.contra = self.parent.ui.contrasenia.text()

        print("Usuario: %s" %self.name)
        print("Contraseña: %s"%self.contra)
        
        if self.name == "lab" and self.contra == "elect":
            # Abro ventana principal una vez verificado el usuario
            self.parent.parent.window_main.show()
        else:
            print("Usuario Incorrecto")
            self.parent.ui.usuario.clear()
            self.parent.ui.contrasenia.clear()

