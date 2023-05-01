# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(567, 235)
        LoginWindow.setStyleSheet(u"/*QApplication::setStyle(\"fusion\");*/\n"
"\n"
"background-color: #EAEAEA;\n"
"")
        self.verticalLayoutWidget = QWidget(LoginWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 40, 471, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(41)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_usuario = QLabel(self.verticalLayoutWidget)
        self.label_usuario.setObjectName(u"label_usuario")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_usuario.sizePolicy().hasHeightForWidth())
        self.label_usuario.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_usuario.setFont(font)

        self.horizontalLayout.addWidget(self.label_usuario)

        self.usuario = QLineEdit(self.verticalLayoutWidget)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setStyleSheet(u"QLineEdit {\n"
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
        self.usuario.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.usuario)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_contra = QLabel(self.verticalLayoutWidget)
        self.label_contra.setObjectName(u"label_contra")
        sizePolicy.setHeightForWidth(self.label_contra.sizePolicy().hasHeightForWidth())
        self.label_contra.setSizePolicy(sizePolicy)
        self.label_contra.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_contra)

        self.contrasenia = QLineEdit(self.verticalLayoutWidget)
        self.contrasenia.setObjectName(u"contrasenia")
        self.contrasenia.setStyleSheet(u"QLineEdit {\n"
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
        self.contrasenia.setEchoMode(QLineEdit.Password)
        self.contrasenia.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.contrasenia)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(50, 20, 50, 5)
        self.btn_aceptar = QPushButton(self.verticalLayoutWidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_aceptar.sizePolicy().hasHeightForWidth())
        self.btn_aceptar.setSizePolicy(sizePolicy1)
        self.btn_aceptar.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_aceptar)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_salir = QPushButton(self.verticalLayoutWidget)
        self.btn_salir.setObjectName(u"btn_salir")
        sizePolicy1.setHeightForWidth(self.btn_salir.sizePolicy().hasHeightForWidth())
        self.btn_salir.setSizePolicy(sizePolicy1)
        self.btn_salir.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.btn_salir)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Form", None))
        self.label_usuario.setText(QCoreApplication.translate("LoginWindow", u"Usuario:", None))
        self.usuario.setInputMask("")
        self.usuario.setText("")
        self.usuario.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Ingrese nombre de usuario en minuscula", None))
        self.label_contra.setText(QCoreApplication.translate("LoginWindow", u"Contrase\u00f1a:", None))
        self.contrasenia.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Ingrese contrase\u00f1a en minuscula", None))
        self.btn_aceptar.setText(QCoreApplication.translate("LoginWindow", u"Ingresar", None))
        self.btn_salir.setText(QCoreApplication.translate("LoginWindow", u"Salir", None))
    # retranslateUi

