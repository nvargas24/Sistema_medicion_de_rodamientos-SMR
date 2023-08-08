# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_meas_corrientes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MeasCorrientesWindow(object):
    def setupUi(self, MeasCorrientesWindow):
        if not MeasCorrientesWindow.objectName():
            MeasCorrientesWindow.setObjectName(u"MeasCorrientesWindow")
        MeasCorrientesWindow.resize(400, 303)
        self.verticalLayoutWidget = QWidget(MeasCorrientesWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 321, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
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

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(40, -1, 40, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.input_fase_u = QLineEdit(self.verticalLayoutWidget)
        self.input_fase_u.setObjectName(u"input_fase_u")
        self.input_fase_u.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_14.addWidget(self.input_fase_u)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_5)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 6)
        self.horizontalLayout_14.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_6)

        self.input_fase_v = QLineEdit(self.verticalLayoutWidget)
        self.input_fase_v.setObjectName(u"input_fase_v")
        self.input_fase_v.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_15.addWidget(self.input_fase_v)

        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_15.addWidget(self.label_8)

        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 6)
        self.horizontalLayout_15.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.input_fase_w = QLineEdit(self.verticalLayoutWidget)
        self.input_fase_w.setObjectName(u"input_fase_w")
        self.input_fase_w.setStyleSheet(u"QLineEdit {\n"
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

        self.horizontalLayout_16.addWidget(self.input_fase_w)

        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_16.addWidget(self.label_10)

        self.horizontalLayout_16.setStretch(0, 2)
        self.horizontalLayout_16.setStretch(1, 6)
        self.horizontalLayout_16.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(90, -1, 90, -1)
        self.btn_aceptar = QPushButton(self.verticalLayoutWidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aceptar.sizePolicy().hasHeightForWidth())
        self.btn_aceptar.setSizePolicy(sizePolicy)
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

        self.horizontalLayout.addWidget(self.btn_aceptar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)

        self.retranslateUi(MeasCorrientesWindow)

        QMetaObject.connectSlotsByName(MeasCorrientesWindow)
    # setupUi

    def retranslateUi(self, MeasCorrientesWindow):
        MeasCorrientesWindow.setWindowTitle(QCoreApplication.translate("MeasCorrientesWindow", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("MeasCorrientesWindow", u"Corrientes medidas", None))
        self.label_4.setText(QCoreApplication.translate("MeasCorrientesWindow", u"Fase U:", None))
        self.input_fase_u.setPlaceholderText(QCoreApplication.translate("MeasCorrientesWindow", u"S\u00f3lo n\u00fameros", None))
        self.label_5.setText(QCoreApplication.translate("MeasCorrientesWindow", u"A", None))
        self.label_6.setText(QCoreApplication.translate("MeasCorrientesWindow", u"Fase V:", None))
        self.input_fase_v.setPlaceholderText(QCoreApplication.translate("MeasCorrientesWindow", u"S\u00f3lo n\u00fameros", None))
        self.label_8.setText(QCoreApplication.translate("MeasCorrientesWindow", u"A", None))
        self.label_9.setText(QCoreApplication.translate("MeasCorrientesWindow", u"Fase W:", None))
        self.input_fase_w.setPlaceholderText(QCoreApplication.translate("MeasCorrientesWindow", u"S\u00f3lo n\u00fameros", None))
        self.label_10.setText(QCoreApplication.translate("MeasCorrientesWindow", u"A", None))
        self.btn_aceptar.setText(QCoreApplication.translate("MeasCorrientesWindow", u"OK", None))
    # retranslateUi

