# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_user_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_FormUserWindow(object):
    def setupUi(self, FormUserWindow):
        if not FormUserWindow.objectName():
            FormUserWindow.setObjectName(u"FormUserWindow")
        FormUserWindow.resize(431, 649)
        self.verticalLayoutWidget = QWidget(FormUserWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 371, 611))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.groupBox.setFont(font1)
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 331, 83))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.input_operario = QLineEdit(self.verticalLayoutWidget_2)
        self.input_operario.setObjectName(u"input_operario")
        self.input_operario.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.input_operario)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.input_legajo = QLineEdit(self.verticalLayoutWidget_2)
        self.input_legajo.setObjectName(u"input_legajo")
        self.input_legajo.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.input_legajo)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 20, 331, 83))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.input_formacion = QLineEdit(self.verticalLayoutWidget_4)
        self.input_formacion.setObjectName(u"input_formacion")
        self.input_formacion.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.input_formacion)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.input_coche = QLineEdit(self.verticalLayoutWidget_4)
        self.input_coche.setObjectName(u"input_coche")
        self.input_coche.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.input_coche)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font1)
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(20, 20, 331, 83))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.input_boguie = QLineEdit(self.verticalLayoutWidget_5)
        self.input_boguie.setObjectName(u"input_boguie")
        self.input_boguie.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.input_boguie)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_9)

        self.input_motor = QLineEdit(self.verticalLayoutWidget_5)
        self.input_motor.setObjectName(u"input_motor")
        self.input_motor.setStyleSheet(u"QLineEdit {\n"
"    background-color: #F7F7F7; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 17px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"QLineEdit:focus {\n"
"    border-color: #0078d7; /* Cambia el color del borde cuando se selecciona el QLineEdit */\n"
"    outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.input_motor)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font1)
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 20, 331, 83))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_10 = QLabel(self.verticalLayoutWidget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_10)

        self.cbox_fase_tierra = QComboBox(self.verticalLayoutWidget_6)
        self.cbox_fase_tierra.addItem("")
        self.cbox_fase_tierra.addItem("")
        self.cbox_fase_tierra.addItem("")
        self.cbox_fase_tierra.setObjectName(u"cbox_fase_tierra")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbox_fase_tierra.sizePolicy().hasHeightForWidth())
        self.cbox_fase_tierra.setSizePolicy(sizePolicy)
        self.cbox_fase_tierra.setFocusPolicy(Qt.NoFocus)
        self.cbox_fase_tierra.setDuplicatesEnabled(False)

        self.horizontalLayout_9.addWidget(self.cbox_fase_tierra)

        self.horizontalLayout_9.setStretch(0, 6)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(8)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.verticalLayoutWidget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_11)

        self.cbox_rod_tierra = QComboBox(self.verticalLayoutWidget_6)
        self.cbox_rod_tierra.addItem("")
        self.cbox_rod_tierra.addItem("")
        self.cbox_rod_tierra.setObjectName(u"cbox_rod_tierra")
        sizePolicy.setHeightForWidth(self.cbox_rod_tierra.sizePolicy().hasHeightForWidth())
        self.cbox_rod_tierra.setSizePolicy(sizePolicy)
        self.cbox_rod_tierra.setFocusPolicy(Qt.NoFocus)
        self.cbox_rod_tierra.setDuplicatesEnabled(False)

        self.horizontalLayout_10.addWidget(self.cbox_rod_tierra)

        self.horizontalLayout_10.setStretch(0, 6)
        self.horizontalLayout_10.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.btn_reset = QPushButton(self.verticalLayoutWidget)
        self.btn_reset.setObjectName(u"btn_reset")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_reset.setFont(font3)
        self.btn_reset.setFocusPolicy(Qt.NoFocus)
        self.btn_reset.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"	outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_reset)

        self.btn_ingresar = QPushButton(self.verticalLayoutWidget)
        self.btn_ingresar.setObjectName(u"btn_ingresar")
        sizePolicy1.setHeightForWidth(self.btn_ingresar.sizePolicy().hasHeightForWidth())
        self.btn_ingresar.setSizePolicy(sizePolicy1)
        self.btn_ingresar.setFont(font3)
        self.btn_ingresar.setFocusPolicy(Qt.NoFocus)
        self.btn_ingresar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
"    color: #444444; /* Color de texto */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    background-color: #88AEF1; /* Color celeste */\n"
"    border-color: #0078D7; /* Borde celeste */\n"
"    color: #FFFFFF; /* Color de texto blanco */\n"
"	outline: none; /* Elimina el contorno alrededor del QLineEdit al seleccionarlo */\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_ingresar)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 6)
        self.verticalLayout.setStretch(4, 6)
        self.verticalLayout.setStretch(5, 6)
        self.verticalLayout.setStretch(6, 4)

        self.retranslateUi(FormUserWindow)

        self.cbox_fase_tierra.setCurrentIndex(-1)
        self.cbox_rod_tierra.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(FormUserWindow)
    # setupUi

    def retranslateUi(self, FormUserWindow):
        FormUserWindow.setWindowTitle(QCoreApplication.translate("FormUserWindow", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("FormUserWindow", u"SMR - Menu de usuario", None))
        self.groupBox.setTitle(QCoreApplication.translate("FormUserWindow", u"Datos de usuario", None))
        self.label.setText(QCoreApplication.translate("FormUserWindow", u"Operario", None))
        self.input_operario.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Ingrese apellido", None))
        self.label_2.setText(QCoreApplication.translate("FormUserWindow", u"Legajo", None))
        self.input_legajo.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Ingrese solo numeros", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("FormUserWindow", u"Datos de formaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("FormUserWindow", u"Formaci\u00f3n", None))
        self.input_formacion.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Ingrese solo numeros", None))
        self.label_6.setText(QCoreApplication.translate("FormUserWindow", u"Coche", None))
        self.input_coche.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Ingrese solo numeros", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("FormUserWindow", u"Datos de motor", None))
        self.label_8.setText(QCoreApplication.translate("FormUserWindow", u"Boguie", None))
        self.input_boguie.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Ingrese modelo", None))
        self.label_9.setText(QCoreApplication.translate("FormUserWindow", u"Motor", None))
        self.input_motor.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Ingrese modelo", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("FormUserWindow", u"Megado", None))
        self.label_10.setText(QCoreApplication.translate("FormUserWindow", u"Fase a tierra", None))
        self.cbox_fase_tierra.setItemText(0, QCoreApplication.translate("FormUserWindow", u"U", None))
        self.cbox_fase_tierra.setItemText(1, QCoreApplication.translate("FormUserWindow", u"V", None))
        self.cbox_fase_tierra.setItemText(2, QCoreApplication.translate("FormUserWindow", u"W", None))

        self.cbox_fase_tierra.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Seleccione rodamiento", None))
        self.label_11.setText(QCoreApplication.translate("FormUserWindow", u"Rodamiento a tierra", None))
        self.cbox_rod_tierra.setItemText(0, QCoreApplication.translate("FormUserWindow", u"Anterior", None))
        self.cbox_rod_tierra.setItemText(1, QCoreApplication.translate("FormUserWindow", u"Posterior", None))

        self.cbox_rod_tierra.setPlaceholderText(QCoreApplication.translate("FormUserWindow", u"Seleccione rodamiento", None))
        self.btn_reset.setText(QCoreApplication.translate("FormUserWindow", u"Reset", None))
        self.btn_ingresar.setText(QCoreApplication.translate("FormUserWindow", u"Ingresar", None))
    # retranslateUi

