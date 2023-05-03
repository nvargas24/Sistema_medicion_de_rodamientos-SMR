# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(475, 565)
        MainWindow.setStyleSheet(u"/*QApplication::setStyle(\"fusion\");*/\n"
"\n"
"background-color: #EAEAEA;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 431, 511))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_usuario = QLabel(self.verticalLayoutWidget)
        self.label_usuario.setObjectName(u"label_usuario")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
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

        self.horizontalLayout_6.addWidget(self.label_usuario)

        self.usuario = QLabel(self.verticalLayoutWidget)
        self.usuario.setObjectName(u"usuario")
        font1 = QFont()
        font1.setPointSize(16)
        self.usuario.setFont(font1)

        self.horizontalLayout_6.addWidget(self.usuario)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_seleccion = QLabel(self.verticalLayoutWidget)
        self.label_seleccion.setObjectName(u"label_seleccion")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_seleccion.sizePolicy().hasHeightForWidth())
        self.label_seleccion.setSizePolicy(sizePolicy1)
        self.label_seleccion.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_seleccion)

        self.comboBox_seleccion = QComboBox(self.verticalLayoutWidget)
        self.comboBox_seleccion.addItem("")
        self.comboBox_seleccion.addItem("")
        self.comboBox_seleccion.addItem("")
        self.comboBox_seleccion.addItem("")
        self.comboBox_seleccion.setObjectName(u"comboBox_seleccion")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_seleccion.sizePolicy().hasHeightForWidth())
        self.comboBox_seleccion.setSizePolicy(sizePolicy2)
        self.comboBox_seleccion.setFocusPolicy(Qt.ClickFocus)
        self.comboBox_seleccion.setStyleSheet(u"QComboBox {\n"
"    background-color: #F7F7F7;\n"
"    border: 2px solid #D9D9D9;\n"
"    border-radius: 17px;\n"
"    padding: 5px 10px;\n"
"    font-size: 14px;\n"
"    color: #444444;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border-color: #0078d7;\n"
"    outline: none;\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox_seleccion.setMaxVisibleItems(5)
        self.comboBox_seleccion.setMinimumContentsLength(0)
        self.comboBox_seleccion.setDuplicatesEnabled(False)

        self.horizontalLayout_3.addWidget(self.comboBox_seleccion)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 10, 391, 271))

        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_opening = QLabel(self.verticalLayoutWidget)
        self.label_opening.setObjectName(u"label_opening")
        sizePolicy.setHeightForWidth(self.label_opening.sizePolicy().hasHeightForWidth())
        self.label_opening.setSizePolicy(sizePolicy)
        self.label_opening.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_opening)

        self.nombre_op = QLabel(self.verticalLayoutWidget)
        self.nombre_op.setObjectName(u"nombre_op")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.nombre_op.setFont(font2)

        self.horizontalLayout_7.addWidget(self.nombre_op)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 20, 15, 10)
        self.btn_aceptar = QPushButton(self.verticalLayoutWidget)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_aceptar.sizePolicy().hasHeightForWidth())
        self.btn_aceptar.setSizePolicy(sizePolicy3)
        self.btn_aceptar.setSizeIncrement(QSize(0, 0))
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
        self.btn_aceptar.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.btn_aceptar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_menu = QPushButton(self.verticalLayoutWidget)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy3.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy3)
        self.btn_menu.setStyleSheet(u"QPushButton {\n"
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
        self.btn_menu.setAutoDefault(True)

        self.horizontalLayout_2.addWidget(self.btn_menu)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(4, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBox_seleccion.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.usuario.setText("")
        self.label_seleccion.setText(QCoreApplication.translate("MainWindow", u"Seleccione anime:", None))
        self.comboBox_seleccion.setItemText(0, QCoreApplication.translate("MainWindow", u"Chainsaw Man", None))
        self.comboBox_seleccion.setItemText(1, QCoreApplication.translate("MainWindow", u"Demon Slayer", None))
        self.comboBox_seleccion.setItemText(2, QCoreApplication.translate("MainWindow", u"Nier Automata", None))
        self.comboBox_seleccion.setItemText(3, QCoreApplication.translate("MainWindow", u"Los Caballeros de Zodiaco", None))

        self.comboBox_seleccion.setCurrentText(QCoreApplication.translate("MainWindow", u"Chainsaw Man", None))
        self.comboBox_seleccion.setPlaceholderText("")
        self.image.setText("")
        self.label_opening.setText(QCoreApplication.translate("MainWindow", u"Opening:", None))
        self.nombre_op.setText("")
        self.btn_aceptar.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Volver a menu", None))
    # retranslateUi

