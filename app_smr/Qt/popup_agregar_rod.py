# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_agregar_rod.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewRodWindow(object):
    def setupUi(self, NewRodWindow):
        if not NewRodWindow.objectName():
            NewRodWindow.setObjectName(u"NewRodWindow")
        NewRodWindow.resize(338, 188)
        self.verticalLayoutWidget = QWidget(NewRodWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 281, 149))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.input_model_rod = QLineEdit(self.verticalLayoutWidget)
        self.input_model_rod.setObjectName(u"input_model_rod")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_model_rod.sizePolicy().hasHeightForWidth())
        self.input_model_rod.setSizePolicy(sizePolicy1)
        font2 = QFont()
        self.input_model_rod.setFont(font2)
        self.input_model_rod.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout.addWidget(self.input_model_rod)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_aceptar = QPushButton(self.verticalLayoutWidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_aceptar.setFont(font3)
        self.btn_aceptar.setFocusPolicy(Qt.NoFocus)
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

        self.horizontalLayout_2.addWidget(self.btn_aceptar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 8)

        self.retranslateUi(NewRodWindow)

        QMetaObject.connectSlotsByName(NewRodWindow)
    # setupUi

    def retranslateUi(self, NewRodWindow):
        NewRodWindow.setWindowTitle(QCoreApplication.translate("NewRodWindow", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NewRodWindow", u"Nuevo rodamiento", None))
        self.label_2.setText(QCoreApplication.translate("NewRodWindow", u"Modelo:", None))
        self.input_model_rod.setPlaceholderText(QCoreApplication.translate("NewRodWindow", u"Ingrese nombre de nuevo modelo", None))
        self.btn_aceptar.setText(QCoreApplication.translate("NewRodWindow", u"Aceptar", None))
    # retranslateUi

