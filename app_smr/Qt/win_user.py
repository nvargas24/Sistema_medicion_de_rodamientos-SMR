# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_user.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        if not UserWindow.objectName():
            UserWindow.setObjectName(u"UserWindow")
        UserWindow.resize(1245, 763)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserWindow.sizePolicy().hasHeightForWidth())
        UserWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        UserWindow.setFont(font)
        self.centralwidget = QWidget(UserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 10, 1211, 740))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, -1, -1, 200)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 20)
        self.btn_iniciar = QPushButton(self.verticalLayoutWidget_3)
        self.btn_iniciar.setObjectName(u"btn_iniciar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_iniciar.sizePolicy().hasHeightForWidth())
        self.btn_iniciar.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_iniciar.setFont(font2)
        self.btn_iniciar.setFocusPolicy(Qt.NoFocus)
        self.btn_iniciar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
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

        self.horizontalLayout_12.addWidget(self.btn_iniciar)

        self.btn_finalizar = QPushButton(self.verticalLayoutWidget_3)
        self.btn_finalizar.setObjectName(u"btn_finalizar")
        sizePolicy1.setHeightForWidth(self.btn_finalizar.sizePolicy().hasHeightForWidth())
        self.btn_finalizar.setSizePolicy(sizePolicy1)
        self.btn_finalizar.setFont(font2)
        self.btn_finalizar.setFocusPolicy(Qt.NoFocus)
        self.btn_finalizar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
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

        self.horizontalLayout_12.addWidget(self.btn_finalizar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.horizontalLayout.addWidget(self.label)

        self.label_operario = QLabel(self.verticalLayoutWidget_3)
        self.label_operario.setObjectName(u"label_operario")
        font4 = QFont()
        font4.setFamily(u"Segoe UI Light")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_operario.setFont(font4)

        self.horizontalLayout.addWidget(self.label_operario)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_legajo = QLabel(self.verticalLayoutWidget_3)
        self.label_legajo.setObjectName(u"label_legajo")
        self.label_legajo.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_legajo)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_formacion = QLabel(self.verticalLayoutWidget_3)
        self.label_formacion.setObjectName(u"label_formacion")
        self.label_formacion.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_formacion)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_coche = QLabel(self.verticalLayoutWidget_3)
        self.label_coche.setObjectName(u"label_coche")
        self.label_coche.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_coche)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_boguie = QLabel(self.verticalLayoutWidget_3)
        self.label_boguie.setObjectName(u"label_boguie")
        self.label_boguie.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_boguie)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.verticalLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_motor = QLabel(self.verticalLayoutWidget_3)
        self.label_motor.setObjectName(u"label_motor")
        self.label_motor.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_motor)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.verticalLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.label_modelo_rod_ant = QLabel(self.verticalLayoutWidget_3)
        self.label_modelo_rod_ant.setObjectName(u"label_modelo_rod_ant")
        self.label_modelo_rod_ant.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_modelo_rod_ant)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.verticalLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.label_modelo_rod_pos = QLabel(self.verticalLayoutWidget_3)
        self.label_modelo_rod_pos.setObjectName(u"label_modelo_rod_pos")
        self.label_modelo_rod_pos.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label_modelo_rod_pos)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.verticalLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.label_fase_tierra = QLabel(self.verticalLayoutWidget_3)
        self.label_fase_tierra.setObjectName(u"label_fase_tierra")
        self.label_fase_tierra.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_fase_tierra)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.verticalLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.label_fase_rod = QLabel(self.verticalLayoutWidget_3)
        self.label_fase_rod.setObjectName(u"label_fase_rod")
        self.label_fase_rod.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_fase_rod)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.btn_config_data = QPushButton(self.verticalLayoutWidget_3)
        self.btn_config_data.setObjectName(u"btn_config_data")
        sizePolicy1.setHeightForWidth(self.btn_config_data.sizePolicy().hasHeightForWidth())
        self.btn_config_data.setSizePolicy(sizePolicy1)
        self.btn_config_data.setFont(font2)
        self.btn_config_data.setFocusPolicy(Qt.NoFocus)
        self.btn_config_data.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 18px; /* Tama\u00f1o de fuente */\n"
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

        self.verticalLayout_7.addWidget(self.btn_config_data)

        self.verticalLayout_7.setStretch(0, 4)
        self.verticalLayout_7.setStretch(1, 2)
        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_7.setStretch(3, 2)
        self.verticalLayout_7.setStretch(4, 2)
        self.verticalLayout_7.setStretch(5, 2)

        self.horizontalLayout_11.addLayout(self.verticalLayout_7)

        self.line_3 = QFrame(self.verticalLayoutWidget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_11.addWidget(self.line_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_notificacion = QLabel(self.verticalLayoutWidget_3)
        self.label_notificacion.setObjectName(u"label_notificacion")
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_notificacion.setFont(font5)
        self.label_notificacion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_notificacion)

        self.line = QFrame(self.verticalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(80, -1, 80, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_23 = QLabel(self.verticalLayoutWidget_3)
        self.label_23.setObjectName(u"label_23")
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_23.setFont(font6)

        self.horizontalLayout_16.addWidget(self.label_23)

        self.lcd_temp_amb = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_temp_amb.setObjectName(u"lcd_temp_amb")
        sizePolicy.setHeightForWidth(self.lcd_temp_amb.sizePolicy().hasHeightForWidth())
        self.lcd_temp_amb.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.lcd_temp_amb)

        self.horizontalLayout_16.setStretch(0, 7)
        self.horizontalLayout_16.setStretch(1, 4)

        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_24 = QLabel(self.verticalLayoutWidget_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)

        self.horizontalLayout_15.addWidget(self.label_24)

        self.lcd_time_ensayo = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_time_ensayo.setObjectName(u"lcd_time_ensayo")
        sizePolicy.setHeightForWidth(self.lcd_time_ensayo.sizePolicy().hasHeightForWidth())
        self.lcd_time_ensayo.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.lcd_time_ensayo)

        self.horizontalLayout_15.setStretch(0, 7)
        self.horizontalLayout_15.setStretch(1, 4)

        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14.setStretch(0, 8)
        self.horizontalLayout_14.setStretch(1, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.line_2 = QFrame(self.verticalLayoutWidget_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 60, -1, 60)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_26 = QLabel(self.verticalLayoutWidget_3)
        self.label_26.setObjectName(u"label_26")
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_26.setFont(font7)

        self.horizontalLayout_17.addWidget(self.label_26)

        self.lcd_temp_ant = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_temp_ant.setObjectName(u"lcd_temp_ant")

        self.horizontalLayout_17.addWidget(self.lcd_temp_ant)

        self.horizontalLayout_17.setStretch(0, 7)
        self.horizontalLayout_17.setStretch(1, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_27 = QLabel(self.verticalLayoutWidget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)

        self.horizontalLayout_18.addWidget(self.label_27)

        self.lcd_axial_ant = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_axial_ant.setObjectName(u"lcd_axial_ant")

        self.horizontalLayout_18.addWidget(self.lcd_axial_ant)

        self.horizontalLayout_18.setStretch(0, 7)
        self.horizontalLayout_18.setStretch(1, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_28 = QLabel(self.verticalLayoutWidget_3)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)

        self.horizontalLayout_19.addWidget(self.label_28)

        self.lcd_radial_ant = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_radial_ant.setObjectName(u"lcd_radial_ant")

        self.horizontalLayout_19.addWidget(self.lcd_radial_ant)

        self.horizontalLayout_19.setStretch(0, 7)
        self.horizontalLayout_19.setStretch(1, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_19)

        self.verticalLayout_8.setStretch(0, 2)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)

        self.horizontalLayout_73.addLayout(self.verticalLayout_8)

        self.fft_ant = QHBoxLayout()
        self.fft_ant.setObjectName(u"fft_ant")

        self.horizontalLayout_73.addLayout(self.fft_ant)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 10, 20, 10)
        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(5, 8, -1, 8)
        self.state_bpfo_ant = QLabel(self.verticalLayoutWidget_3)
        self.state_bpfo_ant.setObjectName(u"state_bpfo_ant")
        self.state_bpfo_ant.setStyleSheet(u"QLabel#state_bpfo_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_69.addWidget(self.state_bpfo_ant)

        self.label_78 = QLabel(self.verticalLayoutWidget_3)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font6)

        self.horizontalLayout_69.addWidget(self.label_78)

        self.horizontalLayout_69.setStretch(0, 2)
        self.horizontalLayout_69.setStretch(1, 3)

        self.verticalLayout_17.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(5, 8, -1, 8)
        self.state_bpfi_ant = QLabel(self.verticalLayoutWidget_3)
        self.state_bpfi_ant.setObjectName(u"state_bpfi_ant")
        self.state_bpfi_ant.setStyleSheet(u"QLabel#state_bpfi_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_70.addWidget(self.state_bpfi_ant)

        self.label_80 = QLabel(self.verticalLayoutWidget_3)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font6)

        self.horizontalLayout_70.addWidget(self.label_80)

        self.horizontalLayout_70.setStretch(0, 2)
        self.horizontalLayout_70.setStretch(1, 3)

        self.verticalLayout_17.addLayout(self.horizontalLayout_70)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(5, 8, -1, 8)
        self.state_ftf_ant = QLabel(self.verticalLayoutWidget_3)
        self.state_ftf_ant.setObjectName(u"state_ftf_ant")
        self.state_ftf_ant.setStyleSheet(u"QLabel#state_ftf_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_71.addWidget(self.state_ftf_ant)

        self.label_82 = QLabel(self.verticalLayoutWidget_3)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font6)

        self.horizontalLayout_71.addWidget(self.label_82)

        self.horizontalLayout_71.setStretch(0, 2)
        self.horizontalLayout_71.setStretch(1, 3)

        self.verticalLayout_17.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalLayout_72.setContentsMargins(5, 8, -1, 8)
        self.state_bsf_ant = QLabel(self.verticalLayoutWidget_3)
        self.state_bsf_ant.setObjectName(u"state_bsf_ant")
        self.state_bsf_ant.setStyleSheet(u"QLabel#state_bsf_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_72.addWidget(self.state_bsf_ant)

        self.label_84 = QLabel(self.verticalLayoutWidget_3)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font6)

        self.horizontalLayout_72.addWidget(self.label_84)

        self.horizontalLayout_72.setStretch(0, 2)
        self.horizontalLayout_72.setStretch(1, 3)

        self.verticalLayout_17.addLayout(self.horizontalLayout_72)


        self.horizontalLayout_73.addLayout(self.verticalLayout_17)

        self.horizontalLayout_73.setStretch(0, 5)
        self.horizontalLayout_73.setStretch(1, 9)
        self.horizontalLayout_73.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_73)

        self.line_7 = QFrame(self.verticalLayoutWidget_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_7)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 60, -1, 60)
        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_85 = QLabel(self.verticalLayoutWidget_3)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font7)

        self.horizontalLayout_75.addWidget(self.label_85)

        self.lcd_temp_pos = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_temp_pos.setObjectName(u"lcd_temp_pos")

        self.horizontalLayout_75.addWidget(self.lcd_temp_pos)

        self.horizontalLayout_75.setStretch(0, 7)
        self.horizontalLayout_75.setStretch(1, 4)

        self.verticalLayout_18.addLayout(self.horizontalLayout_75)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_86 = QLabel(self.verticalLayoutWidget_3)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font7)

        self.horizontalLayout_76.addWidget(self.label_86)

        self.lcd_axial_pos = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_axial_pos.setObjectName(u"lcd_axial_pos")

        self.horizontalLayout_76.addWidget(self.lcd_axial_pos)

        self.horizontalLayout_76.setStretch(0, 7)
        self.horizontalLayout_76.setStretch(1, 4)

        self.verticalLayout_18.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_87 = QLabel(self.verticalLayoutWidget_3)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font7)

        self.horizontalLayout_77.addWidget(self.label_87)

        self.lcd_radial_pos = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_radial_pos.setObjectName(u"lcd_radial_pos")

        self.horizontalLayout_77.addWidget(self.lcd_radial_pos)

        self.horizontalLayout_77.setStretch(0, 7)
        self.horizontalLayout_77.setStretch(1, 4)

        self.verticalLayout_18.addLayout(self.horizontalLayout_77)

        self.verticalLayout_18.setStretch(0, 2)
        self.verticalLayout_18.setStretch(1, 2)
        self.verticalLayout_18.setStretch(2, 2)

        self.horizontalLayout_74.addLayout(self.verticalLayout_18)

        self.fft_pos = QHBoxLayout()
        self.fft_pos.setObjectName(u"fft_pos")

        self.horizontalLayout_74.addLayout(self.fft_pos)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 10, 20, 10)
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(5, 8, -1, 8)
        self.state_bpfo_pos = QLabel(self.verticalLayoutWidget_3)
        self.state_bpfo_pos.setObjectName(u"state_bpfo_pos")
        self.state_bpfo_pos.setStyleSheet(u"QLabel#state_bpfo_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_81.addWidget(self.state_bpfo_pos)

        self.label_93 = QLabel(self.verticalLayoutWidget_3)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font6)

        self.horizontalLayout_81.addWidget(self.label_93)

        self.horizontalLayout_81.setStretch(0, 2)
        self.horizontalLayout_81.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(5, 8, -1, 8)
        self.state_bpfi_pos = QLabel(self.verticalLayoutWidget_3)
        self.state_bpfi_pos.setObjectName(u"state_bpfi_pos")
        self.state_bpfi_pos.setStyleSheet(u"QLabel#state_bpfi_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_80.addWidget(self.state_bpfi_pos)

        self.label_91 = QLabel(self.verticalLayoutWidget_3)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font6)

        self.horizontalLayout_80.addWidget(self.label_91)

        self.horizontalLayout_80.setStretch(0, 2)
        self.horizontalLayout_80.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(5, 8, -1, 8)
        self.state_ftf_pos = QLabel(self.verticalLayoutWidget_3)
        self.state_ftf_pos.setObjectName(u"state_ftf_pos")
        self.state_ftf_pos.setStyleSheet(u"QLabel#state_ftf_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_79.addWidget(self.state_ftf_pos)

        self.label_89 = QLabel(self.verticalLayoutWidget_3)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font6)

        self.horizontalLayout_79.addWidget(self.label_89)

        self.horizontalLayout_79.setStretch(0, 2)
        self.horizontalLayout_79.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(5, 8, -1, 5)
        self.state_bsf_pos = QLabel(self.verticalLayoutWidget_3)
        self.state_bsf_pos.setObjectName(u"state_bsf_pos")
        self.state_bsf_pos.setStyleSheet(u"QLabel#state_bsf_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_82.addWidget(self.state_bsf_pos)

        self.label_95 = QLabel(self.verticalLayoutWidget_3)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font6)

        self.horizontalLayout_82.addWidget(self.label_95)

        self.horizontalLayout_82.setStretch(0, 2)
        self.horizontalLayout_82.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_82)


        self.horizontalLayout_74.addLayout(self.verticalLayout_19)

        self.horizontalLayout_74.setStretch(0, 5)
        self.horizontalLayout_74.setStretch(1, 9)
        self.horizontalLayout_74.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_74)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 4)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 18)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 18)

        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(2, 3)

        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        UserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserWindow)

        QMetaObject.connectSlotsByName(UserWindow)
    # setupUi

    def retranslateUi(self, UserWindow):
        UserWindow.setWindowTitle(QCoreApplication.translate("UserWindow", u"MainWindow", None))
        self.label_7.setText(QCoreApplication.translate("UserWindow", u"SMR - Menu de usuario", None))
        self.btn_iniciar.setText(QCoreApplication.translate("UserWindow", u"Iniciar \n"
"ensayo", None))
        self.btn_finalizar.setText(QCoreApplication.translate("UserWindow", u"Finalizar \n"
"ensayo", None))
        self.label.setText(QCoreApplication.translate("UserWindow", u"Operario:", None))
        self.label_operario.setText("")
        self.label_3.setText(QCoreApplication.translate("UserWindow", u"Legajo:", None))
        self.label_legajo.setText("")
        self.label_5.setText(QCoreApplication.translate("UserWindow", u"Formaci\u00f3n:", None))
        self.label_formacion.setText("")
        self.label_8.setText(QCoreApplication.translate("UserWindow", u"Coche:", None))
        self.label_coche.setText("")
        self.label_10.setText(QCoreApplication.translate("UserWindow", u"Boguie:", None))
        self.label_boguie.setText("")
        self.label_12.setText(QCoreApplication.translate("UserWindow", u"Motor:", None))
        self.label_motor.setText("")
        self.label_14.setText(QCoreApplication.translate("UserWindow", u"Rodamiento anterior:", None))
        self.label_modelo_rod_ant.setText("")
        self.label_16.setText(QCoreApplication.translate("UserWindow", u"Rodamiento posterior:", None))
        self.label_modelo_rod_pos.setText("")
        self.label_18.setText(QCoreApplication.translate("UserWindow", u"Fase a tierra:", None))
        self.label_fase_tierra.setText("")
        self.label_20.setText(QCoreApplication.translate("UserWindow", u"Fase a rodamiento:", None))
        self.label_fase_rod.setText("")
        self.btn_config_data.setText(QCoreApplication.translate("UserWindow", u"Configurar datos", None))
        self.label_notificacion.setText(QCoreApplication.translate("UserWindow", u"NOTIFICACION", None))
        self.label_23.setText(QCoreApplication.translate("UserWindow", u"Temperatura ambiente: ", None))
        self.label_24.setText(QCoreApplication.translate("UserWindow", u"Tiempo de ensayo: ", None))
        self.label_26.setText(QCoreApplication.translate("UserWindow", u"Temperatura(\u00b0C): ", None))
        self.label_27.setText(QCoreApplication.translate("UserWindow", u"Vib. axial(mm/s2): ", None))
        self.label_28.setText(QCoreApplication.translate("UserWindow", u"Vib. radial(mm/s2): ", None))
        self.state_bpfo_ant.setText("")
        self.label_78.setText(QCoreApplication.translate("UserWindow", u"BPFO", None))
        self.state_bpfi_ant.setText("")
        self.label_80.setText(QCoreApplication.translate("UserWindow", u"BPFI", None))
        self.state_ftf_ant.setText("")
        self.label_82.setText(QCoreApplication.translate("UserWindow", u"FTF", None))
        self.state_bsf_ant.setText("")
        self.label_84.setText(QCoreApplication.translate("UserWindow", u"BSF", None))
        self.label_85.setText(QCoreApplication.translate("UserWindow", u"Temperatura(\u00b0C): ", None))
        self.label_86.setText(QCoreApplication.translate("UserWindow", u"Vib. axial(mm/s2): ", None))
        self.label_87.setText(QCoreApplication.translate("UserWindow", u"Vib. radial(mm/s2): ", None))
        self.state_bpfo_pos.setText("")
        self.label_93.setText(QCoreApplication.translate("UserWindow", u"BPFO", None))
        self.state_bpfi_pos.setText("")
        self.label_91.setText(QCoreApplication.translate("UserWindow", u"BPFI", None))
        self.state_ftf_pos.setText("")
        self.label_89.setText(QCoreApplication.translate("UserWindow", u"FTF", None))
        self.state_bsf_pos.setText("")
        self.label_95.setText(QCoreApplication.translate("UserWindow", u"BSF", None))
    # retranslateUi

