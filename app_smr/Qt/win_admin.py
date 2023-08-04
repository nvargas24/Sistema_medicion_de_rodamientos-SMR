# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_admin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(588, 532)
        self.verticalLayoutWidget = QWidget(AdminWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 40, 491, 454))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_29 = QLabel(self.verticalLayoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_29)

        self.cbox_modelo_rod_ant = QComboBox(self.verticalLayoutWidget)
        self.cbox_modelo_rod_ant.setObjectName(u"cbox_modelo_rod_ant")
        self.cbox_modelo_rod_ant.setFont(font)
        self.cbox_modelo_rod_ant.setFocusPolicy(Qt.ClickFocus)
        self.cbox_modelo_rod_ant.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.cbox_modelo_rod_ant)

        self.horizontalLayout_19.setStretch(0, 4)
        self.horizontalLayout_19.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_28 = QLabel(self.verticalLayoutWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_28)

        self.cbox_modelo_rod_pos = QComboBox(self.verticalLayoutWidget)
        self.cbox_modelo_rod_pos.setObjectName(u"cbox_modelo_rod_pos")
        self.cbox_modelo_rod_pos.setFont(font)
        self.cbox_modelo_rod_pos.setFocusPolicy(Qt.ClickFocus)
        self.cbox_modelo_rod_pos.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.cbox_modelo_rod_pos)

        self.horizontalLayout_18.setStretch(0, 4)
        self.horizontalLayout_18.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.sbox_temp_max = QSpinBox(self.verticalLayoutWidget)
        self.sbox_temp_max.setObjectName(u"sbox_temp_max")
        self.sbox_temp_max.setFocusPolicy(Qt.ClickFocus)
        self.sbox_temp_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_temp_max.setMinimum(0)
        self.sbox_temp_max.setMaximum(100)
        self.sbox_temp_max.setValue(0)

        self.horizontalLayout.addWidget(self.sbox_temp_max)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.sbox_temp_min = QSpinBox(self.verticalLayoutWidget)
        self.sbox_temp_min.setObjectName(u"sbox_temp_min")
        self.sbox_temp_min.setFocusPolicy(Qt.ClickFocus)
        self.sbox_temp_min.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_temp_min.setMinimum(-50)
        self.sbox_temp_min.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.sbox_temp_min)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sbox_axial_max = QSpinBox(self.verticalLayoutWidget)
        self.sbox_axial_max.setObjectName(u"sbox_axial_max")
        self.sbox_axial_max.setFocusPolicy(Qt.ClickFocus)
        self.sbox_axial_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.sbox_axial_max)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.sbox_radial_max = QSpinBox(self.verticalLayoutWidget)
        self.sbox_radial_max.setObjectName(u"sbox_radial_max")
        self.sbox_radial_max.setFocusPolicy(Qt.ClickFocus)
        self.sbox_radial_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.sbox_radial_max)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 10, -1, 10)
        self.btn_guardar = QPushButton(self.verticalLayoutWidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_guardar.sizePolicy().hasHeightForWidth())
        self.btn_guardar.setSizePolicy(sizePolicy)
        self.btn_guardar.setFocusPolicy(Qt.NoFocus)
        self.btn_guardar.setStyleSheet(u"QPushButton {\n"
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
        self.btn_guardar.setCheckable(False)
        self.btn_guardar.setAutoRepeat(False)
        self.btn_guardar.setAutoDefault(False)
        self.btn_guardar.setFlat(False)

        self.horizontalLayout_16.addWidget(self.btn_guardar)

        self.btn_reset = QPushButton(self.verticalLayoutWidget)
        self.btn_reset.setObjectName(u"btn_reset")
        sizePolicy.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy)
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

        self.horizontalLayout_16.addWidget(self.btn_reset)

        self.btn_edit_rod = QPushButton(self.verticalLayoutWidget)
        self.btn_edit_rod.setObjectName(u"btn_edit_rod")
        sizePolicy.setHeightForWidth(self.btn_edit_rod.sizePolicy().hasHeightForWidth())
        self.btn_edit_rod.setSizePolicy(sizePolicy)
        self.btn_edit_rod.setFocusPolicy(Qt.NoFocus)
        self.btn_edit_rod.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.btn_edit_rod)


        self.verticalLayout.addLayout(self.horizontalLayout_16)


        self.retranslateUi(AdminWindow)

        self.btn_guardar.setDefault(False)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("AdminWindow", u"SMR-Menu Administrador", None))
        self.label_29.setText(QCoreApplication.translate("AdminWindow", u"Modelo en rod. anterior:", None))
        self.label_28.setText(QCoreApplication.translate("AdminWindow", u"Modelo en rod. posterior:", None))
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u"Temperatura m\u00e1x.(\u00b0C):", None))
        self.label_3.setText(QCoreApplication.translate("AdminWindow", u"Temperatura min.(\u00b0C):", None))
        self.label_4.setText(QCoreApplication.translate("AdminWindow", u"Vib. axial m\u00e1x.(mm/s2):", None))
        self.label_5.setText(QCoreApplication.translate("AdminWindow", u"Vib. radial m\u00e1x.(mm/s2):", None))
        self.btn_guardar.setText(QCoreApplication.translate("AdminWindow", u"Guardar \n"
" configuracion", None))
        self.btn_reset.setText(QCoreApplication.translate("AdminWindow", u"Default", None))
        self.btn_edit_rod.setText(QCoreApplication.translate("AdminWindow", u"Editar \n"
"rodamientos", None))
    # retranslateUi

