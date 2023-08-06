# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_admin_rod.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_RodWindow(object):
    def setupUi(self, RodWindow):
        if not RodWindow.objectName():
            RodWindow.setObjectName(u"RodWindow")
        RodWindow.resize(723, 600)
        RodWindow.setFocusPolicy(Qt.ClickFocus)
        RodWindow.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.centralwidget = QWidget(RodWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 661, 551))
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

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_13)

        self.cbox_modelo_rod = QComboBox(self.verticalLayoutWidget)
        self.cbox_modelo_rod.setObjectName(u"cbox_modelo_rod")
        self.cbox_modelo_rod.setFont(font)
        self.cbox_modelo_rod.setFocusPolicy(Qt.ClickFocus)
        self.cbox_modelo_rod.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cbox_modelo_rod)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 50)
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_8.addWidget(self.label_14)

        self.rbtn_horario = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup = QButtonGroup(RodWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rbtn_horario)
        self.rbtn_horario.setObjectName(u"rbtn_horario")
        self.rbtn_horario.setFont(font)
        self.rbtn_horario.setChecked(True)

        self.verticalLayout_8.addWidget(self.rbtn_horario)

        self.rbtn_antihorario = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup.addButton(self.rbtn_antihorario)
        self.rbtn_antihorario.setObjectName(u"rbtn_antihorario")
        self.rbtn_antihorario.setFont(font)

        self.verticalLayout_8.addWidget(self.rbtn_antihorario)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout_9.addWidget(self.label_15)

        self.rbtn_v300 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_2 = QButtonGroup(RodWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.rbtn_v300)
        self.rbtn_v300.setObjectName(u"rbtn_v300")
        self.rbtn_v300.setFont(font)
        self.rbtn_v300.setChecked(True)
        self.rbtn_v300.setAutoRepeat(True)
        self.rbtn_v300.setAutoExclusive(True)

        self.verticalLayout_9.addWidget(self.rbtn_v300)

        self.rbtn_v1500 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_2.addButton(self.rbtn_v1500)
        self.rbtn_v1500.setObjectName(u"rbtn_v1500")
        self.rbtn_v1500.setFont(font)

        self.verticalLayout_9.addWidget(self.rbtn_v1500)

        self.rbtn_v1800 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_2.addButton(self.rbtn_v1800)
        self.rbtn_v1800.setObjectName(u"rbtn_v1800")
        self.rbtn_v1800.setFont(font)

        self.verticalLayout_9.addWidget(self.rbtn_v1800)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(40, 40, 571, 129))
        self.horizontalLayoutWidget_7.setFont(font)
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_16 = QLabel(self.horizontalLayoutWidget_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_16)

        self.sbox_bpfo = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_bpfo.setObjectName(u"sbox_bpfo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbox_bpfo.sizePolicy().hasHeightForWidth())
        self.sbox_bpfo.setSizePolicy(sizePolicy)
        self.sbox_bpfo.setFont(font)
        self.sbox_bpfo.setAutoFillBackground(False)
        self.sbox_bpfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_bpfo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_bpfo.setMaximum(19000)

        self.horizontalLayout_12.addWidget(self.sbox_bpfo)

        self.label_17 = QLabel(self.horizontalLayoutWidget_7)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setFont(font)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.horizontalLayout_12.setStretch(0, 4)
        self.horizontalLayout_12.setStretch(1, 8)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.horizontalLayoutWidget_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_18)

        self.sbox_bpfi = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_bpfi.setObjectName(u"sbox_bpfi")
        sizePolicy.setHeightForWidth(self.sbox_bpfi.sizePolicy().hasHeightForWidth())
        self.sbox_bpfi.setSizePolicy(sizePolicy)
        self.sbox_bpfi.setFont(font)
        self.sbox_bpfi.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_bpfi.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_bpfi.setMaximum(19000)

        self.horizontalLayout_13.addWidget(self.sbox_bpfi)

        self.label_19 = QLabel(self.horizontalLayoutWidget_7)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setFont(font)

        self.horizontalLayout_13.addWidget(self.label_19)

        self.horizontalLayout_13.setStretch(0, 4)
        self.horizontalLayout_13.setStretch(1, 8)
        self.horizontalLayout_13.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_20 = QLabel(self.horizontalLayoutWidget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_20)

        self.sbox_ftf = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_ftf.setObjectName(u"sbox_ftf")
        sizePolicy.setHeightForWidth(self.sbox_ftf.sizePolicy().hasHeightForWidth())
        self.sbox_ftf.setSizePolicy(sizePolicy)
        self.sbox_ftf.setFont(font)
        self.sbox_ftf.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_ftf.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_ftf.setMaximum(19000)

        self.horizontalLayout_14.addWidget(self.sbox_ftf)

        self.label_21 = QLabel(self.horizontalLayoutWidget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 8)
        self.horizontalLayout_14.setStretch(2, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.horizontalLayoutWidget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_22)

        self.sbox_bsf = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_bsf.setObjectName(u"sbox_bsf")
        sizePolicy.setHeightForWidth(self.sbox_bsf.sizePolicy().hasHeightForWidth())
        self.sbox_bsf.setSizePolicy(sizePolicy)
        self.sbox_bsf.setFont(font)
        self.sbox_bsf.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_bsf.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_bsf.setMaximum(19000)

        self.horizontalLayout_15.addWidget(self.sbox_bsf)

        self.label_23 = QLabel(self.horizontalLayoutWidget_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_23)

        self.horizontalLayout_15.setStretch(0, 4)
        self.horizontalLayout_15.setStretch(1, 8)
        self.horizontalLayout_15.setStretch(2, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_11.addLayout(self.verticalLayout_11)

        self.horizontalLayout_11.setStretch(0, 7)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 7)

        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 3)
        self.verticalLayout_7.setStretch(2, 6)

        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 10, -1, 10)
        self.btn_guardar = QPushButton(self.verticalLayoutWidget)
        self.btn_guardar.setObjectName(u"btn_guardar")
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

        self.btn_new_rod = QPushButton(self.verticalLayoutWidget)
        self.btn_new_rod.setObjectName(u"btn_new_rod")
        self.btn_new_rod.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.btn_new_rod)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        RodWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RodWindow)

        self.btn_guardar.setDefault(False)


        QMetaObject.connectSlotsByName(RodWindow)
    # setupUi

    def retranslateUi(self, RodWindow):
        RodWindow.setWindowTitle(QCoreApplication.translate("RodWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("RodWindow", u"SMR-Menu Administrador", None))
        self.label_13.setText(QCoreApplication.translate("RodWindow", u"Modelo de rodamiento:", None))
        self.label_14.setText(QCoreApplication.translate("RodWindow", u"Sentido de rotacion:", None))
        self.rbtn_horario.setText(QCoreApplication.translate("RodWindow", u"Horario", None))
        self.rbtn_antihorario.setText(QCoreApplication.translate("RodWindow", u"Antiorario", None))
        self.label_15.setText(QCoreApplication.translate("RodWindow", u"Velocidad de motor:", None))
        self.rbtn_v300.setText(QCoreApplication.translate("RodWindow", u"300 RPM", None))
        self.rbtn_v1500.setText(QCoreApplication.translate("RodWindow", u"1500 RPM", None))
        self.rbtn_v1800.setText(QCoreApplication.translate("RodWindow", u"1800 RPM", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("RodWindow", u"Frecuencias a detectar", None))
        self.label_16.setText(QCoreApplication.translate("RodWindow", u"BPFO:", None))
        self.label_17.setText(QCoreApplication.translate("RodWindow", u"Hz", None))
        self.label_18.setText(QCoreApplication.translate("RodWindow", u"BPFI:", None))
        self.label_19.setText(QCoreApplication.translate("RodWindow", u"Hz", None))
        self.label_20.setText(QCoreApplication.translate("RodWindow", u"FTF:", None))
        self.label_21.setText(QCoreApplication.translate("RodWindow", u"Hz", None))
        self.label_22.setText(QCoreApplication.translate("RodWindow", u"BSF:", None))
        self.label_23.setText(QCoreApplication.translate("RodWindow", u"Hz", None))
        self.btn_guardar.setText(QCoreApplication.translate("RodWindow", u"Guardar \n"
" configuracion", None))
        self.btn_reset.setText(QCoreApplication.translate("RodWindow", u"Restablecer \n"
"freuencias", None))
        self.btn_new_rod.setText(QCoreApplication.translate("RodWindow", u"Guardar\n"
" nuevo modelo", None))
    # retranslateUi

