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
        UserWindow.resize(795, 754)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UserWindow.sizePolicy().hasHeightForWidth())
        UserWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        UserWindow.setFont(font)
        UserWindow.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.centralwidget = QWidget(UserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_11 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(40, 10, 711, 721))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_11)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_7)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, 10)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_iniciar = QPushButton(self.verticalLayoutWidget_11)
        self.btn_iniciar.setObjectName(u"btn_iniciar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_iniciar.sizePolicy().hasHeightForWidth())
        self.btn_iniciar.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
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

        self.horizontalLayout_13.addWidget(self.btn_iniciar)

        self.btn_finalizar = QPushButton(self.verticalLayoutWidget_11)
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

        self.horizontalLayout_13.addWidget(self.btn_finalizar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.btn_config_data = QPushButton(self.verticalLayoutWidget_11)
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

        self.verticalLayout_3.addWidget(self.btn_config_data)

        self.btn_ver_ensayos = QPushButton(self.verticalLayoutWidget_11)
        self.btn_ver_ensayos.setObjectName(u"btn_ver_ensayos")
        sizePolicy1.setHeightForWidth(self.btn_ver_ensayos.sizePolicy().hasHeightForWidth())
        self.btn_ver_ensayos.setSizePolicy(sizePolicy1)
        self.btn_ver_ensayos.setFont(font2)
        self.btn_ver_ensayos.setFocusPolicy(Qt.NoFocus)
        self.btn_ver_ensayos.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.btn_ver_ensayos)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget_4 = QWidget(self.groupBox)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 160, 51))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.horizontalLayout.addWidget(self.label)

        self.label_operario = QLabel(self.verticalLayoutWidget_4)
        self.label_operario.setObjectName(u"label_operario")
        font4 = QFont()
        font4.setFamily(u"Segoe UI Light")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.label_operario.setFont(font4)

        self.horizontalLayout.addWidget(self.label_operario)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_legajo = QLabel(self.verticalLayoutWidget_4)
        self.label_legajo.setObjectName(u"label_legajo")
        self.label_legajo.setFont(font4)

        self.horizontalLayout_2.addWidget(self.label_legajo)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 20, 160, 51))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.verticalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_formacion = QLabel(self.verticalLayoutWidget_5)
        self.label_formacion.setObjectName(u"label_formacion")
        self.label_formacion.setFont(font4)

        self.horizontalLayout_3.addWidget(self.label_formacion)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 5)

        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_8 = QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_8)

        self.label_coche = QLabel(self.verticalLayoutWidget_5)
        self.label_coche.setObjectName(u"label_coche")
        self.label_coche.setFont(font4)

        self.horizontalLayout_4.addWidget(self.label_coche)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout_10.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayoutWidget_7 = QWidget(self.groupBox_4)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(10, 20, 161, 51))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.verticalLayoutWidget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_boguie = QLabel(self.verticalLayoutWidget_7)
        self.label_boguie.setObjectName(u"label_boguie")
        self.label_boguie.setFont(font4)

        self.horizontalLayout_5.addWidget(self.label_boguie)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 5)

        self.verticalLayout_12.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.verticalLayoutWidget_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_12)

        self.label_motor = QLabel(self.verticalLayoutWidget_7)
        self.label_motor.setObjectName(u"label_motor")
        self.label_motor.setFont(font4)

        self.horizontalLayout_6.addWidget(self.label_motor)

        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 5)

        self.verticalLayout_12.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_11)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 160, 51))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_18 = QLabel(self.verticalLayoutWidget_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_18)

        self.label_fase_tierra = QLabel(self.verticalLayoutWidget_6)
        self.label_fase_tierra.setObjectName(u"label_fase_tierra")
        self.label_fase_tierra.setFont(font4)

        self.horizontalLayout_9.addWidget(self.label_fase_tierra)

        self.horizontalLayout_9.setStretch(0, 6)
        self.horizontalLayout_9.setStretch(1, 2)

        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.verticalLayoutWidget_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.label_rod_tierra = QLabel(self.verticalLayoutWidget_6)
        self.label_rod_tierra.setObjectName(u"label_rod_tierra")
        self.label_rod_tierra.setFont(font4)

        self.horizontalLayout_10.addWidget(self.label_rod_tierra)

        self.horizontalLayout_10.setStretch(0, 6)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_11.addLayout(self.horizontalLayout_10)


        self.verticalLayout_2.addWidget(self.groupBox_3)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 7)

        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_notificacion = QLabel(self.verticalLayoutWidget_11)
        self.label_notificacion.setObjectName(u"label_notificacion")
        font5 = QFont()
        font5.setFamily(u"Segoe UI Semibold")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_notificacion.setFont(font5)
        self.label_notificacion.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_notificacion)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 0, -1)
        self.label_24 = QLabel(self.verticalLayoutWidget_11)
        self.label_24.setObjectName(u"label_24")
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_24.setFont(font6)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_24)

        self.lcd_time_ensayo = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_time_ensayo.setObjectName(u"lcd_time_ensayo")
        sizePolicy.setHeightForWidth(self.lcd_time_ensayo.sizePolicy().hasHeightForWidth())
        self.lcd_time_ensayo.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.lcd_time_ensayo)

        self.horizontalLayout_15.setStretch(0, 6)
        self.horizontalLayout_15.setStretch(1, 8)

        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.label_23 = QLabel(self.verticalLayoutWidget_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_23)

        self.lcd_temp_amb = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_temp_amb.setObjectName(u"lcd_temp_amb")
        sizePolicy.setHeightForWidth(self.lcd_temp_amb.sizePolicy().hasHeightForWidth())
        self.lcd_temp_amb.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.lcd_temp_amb)

        self.horizontalLayout_16.setStretch(0, 6)
        self.horizontalLayout_16.setStretch(1, 8)

        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.verticalLayout_7.setStretch(0, 8)
        self.verticalLayout_7.setStretch(1, 3)

        self.horizontalLayout_18.addLayout(self.verticalLayout_7)

        self.horizontalLayout_18.setStretch(0, 8)
        self.horizontalLayout_18.setStretch(1, 6)

        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.verticalLayoutWidget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.label_modelo_rod_ant = QLabel(self.verticalLayoutWidget_11)
        self.label_modelo_rod_ant.setObjectName(u"label_modelo_rod_ant")
        self.label_modelo_rod_ant.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_modelo_rod_ant)

        self.horizontalLayout_7.setStretch(0, 7)
        self.horizontalLayout_7.setStretch(1, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_30 = QLabel(self.verticalLayoutWidget_11)
        self.label_30.setObjectName(u"label_30")
        font7 = QFont()
        font7.setFamily(u"Segoe UI Semibold")
        font7.setPointSize(11)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_30.setFont(font7)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_30)

        self.label_time_stap_pos = QLabel(self.verticalLayoutWidget_11)
        self.label_time_stap_pos.setObjectName(u"label_time_stap_pos")
        self.label_time_stap_pos.setFont(font7)

        self.horizontalLayout_21.addWidget(self.label_time_stap_pos)

        self.horizontalLayout_21.setStretch(0, 7)
        self.horizontalLayout_21.setStretch(1, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(20, 0, 20, 0)
        self.label_26 = QLabel(self.verticalLayoutWidget_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font7)
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_26)

        self.lcd_temp_ant = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_temp_ant.setObjectName(u"lcd_temp_ant")

        self.verticalLayout_8.addWidget(self.lcd_temp_ant)

        self.label_27 = QLabel(self.verticalLayoutWidget_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_27)

        self.lcd_axial_ant = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_axial_ant.setObjectName(u"lcd_axial_ant")

        self.verticalLayout_8.addWidget(self.lcd_axial_ant)

        self.label_28 = QLabel(self.verticalLayoutWidget_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_28)

        self.lcd_radial_ant = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_radial_ant.setObjectName(u"lcd_radial_ant")

        self.verticalLayout_8.addWidget(self.lcd_radial_ant)


        self.horizontalLayout_73.addLayout(self.verticalLayout_8)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, 5, 0)
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setSpacing(15)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(5, 8, -1, 8)
        self.state_bpfo_ant = QLabel(self.verticalLayoutWidget_11)
        self.state_bpfo_ant.setObjectName(u"state_bpfo_ant")
        self.state_bpfo_ant.setStyleSheet(u"QLabel#state_bpfo_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_83.addWidget(self.state_bpfo_ant)

        self.label_94 = QLabel(self.verticalLayoutWidget_11)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font6)

        self.horizontalLayout_83.addWidget(self.label_94)

        self.horizontalLayout_83.setStretch(0, 2)
        self.horizontalLayout_83.setStretch(1, 3)

        self.verticalLayout_20.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setSpacing(15)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(5, 8, -1, 8)
        self.state_bpfi_ant = QLabel(self.verticalLayoutWidget_11)
        self.state_bpfi_ant.setObjectName(u"state_bpfi_ant")
        self.state_bpfi_ant.setStyleSheet(u"QLabel#state_bpfi_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_84.addWidget(self.state_bpfi_ant)

        self.label_92 = QLabel(self.verticalLayoutWidget_11)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font6)

        self.horizontalLayout_84.addWidget(self.label_92)

        self.horizontalLayout_84.setStretch(0, 2)
        self.horizontalLayout_84.setStretch(1, 3)

        self.verticalLayout_20.addLayout(self.horizontalLayout_84)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setSpacing(15)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(5, 8, -1, 8)
        self.state_ftf_ant = QLabel(self.verticalLayoutWidget_11)
        self.state_ftf_ant.setObjectName(u"state_ftf_ant")
        self.state_ftf_ant.setStyleSheet(u"QLabel#state_ftf_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_85.addWidget(self.state_ftf_ant)

        self.label_90 = QLabel(self.verticalLayoutWidget_11)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font6)

        self.horizontalLayout_85.addWidget(self.label_90)

        self.horizontalLayout_85.setStretch(0, 2)
        self.horizontalLayout_85.setStretch(1, 3)

        self.verticalLayout_20.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(15)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(5, 8, -1, 5)
        self.state_bsf_ant = QLabel(self.verticalLayoutWidget_11)
        self.state_bsf_ant.setObjectName(u"state_bsf_ant")
        self.state_bsf_ant.setStyleSheet(u"QLabel#state_bsf_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_86.addWidget(self.state_bsf_ant)

        self.label_96 = QLabel(self.verticalLayoutWidget_11)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font6)

        self.horizontalLayout_86.addWidget(self.label_96)

        self.horizontalLayout_86.setStretch(0, 2)
        self.horizontalLayout_86.setStretch(1, 3)

        self.verticalLayout_20.addLayout(self.horizontalLayout_86)

        self.verticalLayout_20.setStretch(0, 1)
        self.verticalLayout_20.setStretch(1, 1)
        self.verticalLayout_20.setStretch(2, 1)
        self.verticalLayout_20.setStretch(3, 1)

        self.horizontalLayout_73.addLayout(self.verticalLayout_20)

        self.horizontalLayout_73.setStretch(0, 4)
        self.horizontalLayout_73.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_73)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 8)

        self.horizontalLayout_17.addLayout(self.verticalLayout_4)

        self.line = QFrame(self.verticalLayoutWidget_11)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_17.addWidget(self.line)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.verticalLayoutWidget_11)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.label_modelo_rod_pos = QLabel(self.verticalLayoutWidget_11)
        self.label_modelo_rod_pos.setObjectName(u"label_modelo_rod_pos")
        self.label_modelo_rod_pos.setFont(font4)

        self.horizontalLayout_8.addWidget(self.label_modelo_rod_pos)

        self.horizontalLayout_8.setStretch(0, 9)
        self.horizontalLayout_8.setStretch(1, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_29 = QLabel(self.verticalLayoutWidget_11)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font7)
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_20.addWidget(self.label_29)

        self.label_time_stap_ant = QLabel(self.verticalLayoutWidget_11)
        self.label_time_stap_ant.setObjectName(u"label_time_stap_ant")
        self.label_time_stap_ant.setFont(font7)

        self.horizontalLayout_20.addWidget(self.label_time_stap_ant)

        self.horizontalLayout_20.setStretch(0, 9)
        self.horizontalLayout_20.setStretch(1, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(20, 0, 20, 0)
        self.label_85 = QLabel(self.verticalLayoutWidget_11)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font7)
        self.label_85.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_85)

        self.lcd_temp_pos = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_temp_pos.setObjectName(u"lcd_temp_pos")

        self.verticalLayout_18.addWidget(self.lcd_temp_pos)

        self.label_86 = QLabel(self.verticalLayoutWidget_11)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font7)
        self.label_86.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_86)

        self.lcd_axial_pos = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_axial_pos.setObjectName(u"lcd_axial_pos")

        self.verticalLayout_18.addWidget(self.lcd_axial_pos)

        self.label_87 = QLabel(self.verticalLayoutWidget_11)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font7)
        self.label_87.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_87)

        self.lcd_radial_pos = QLCDNumber(self.verticalLayoutWidget_11)
        self.lcd_radial_pos.setObjectName(u"lcd_radial_pos")

        self.verticalLayout_18.addWidget(self.lcd_radial_pos)


        self.horizontalLayout_74.addLayout(self.verticalLayout_18)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, 0, 5, 0)
        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setSpacing(15)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(5, 8, -1, 8)
        self.state_bpfo_pos = QLabel(self.verticalLayoutWidget_11)
        self.state_bpfo_pos.setObjectName(u"state_bpfo_pos")
        self.state_bpfo_pos.setStyleSheet(u"QLabel#state_bpfo_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_81.addWidget(self.state_bpfo_pos)

        self.label_93 = QLabel(self.verticalLayoutWidget_11)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font6)

        self.horizontalLayout_81.addWidget(self.label_93)

        self.horizontalLayout_81.setStretch(0, 2)
        self.horizontalLayout_81.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setSpacing(15)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(5, 8, -1, 8)
        self.state_bpfi_pos = QLabel(self.verticalLayoutWidget_11)
        self.state_bpfi_pos.setObjectName(u"state_bpfi_pos")
        self.state_bpfi_pos.setStyleSheet(u"QLabel#state_bpfi_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_80.addWidget(self.state_bpfi_pos)

        self.label_91 = QLabel(self.verticalLayoutWidget_11)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font6)

        self.horizontalLayout_80.addWidget(self.label_91)

        self.horizontalLayout_80.setStretch(0, 2)
        self.horizontalLayout_80.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setSpacing(15)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(5, 8, -1, 8)
        self.state_ftf_pos = QLabel(self.verticalLayoutWidget_11)
        self.state_ftf_pos.setObjectName(u"state_ftf_pos")
        self.state_ftf_pos.setStyleSheet(u"QLabel#state_ftf_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_79.addWidget(self.state_ftf_pos)

        self.label_89 = QLabel(self.verticalLayoutWidget_11)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font6)

        self.horizontalLayout_79.addWidget(self.label_89)

        self.horizontalLayout_79.setStretch(0, 2)
        self.horizontalLayout_79.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setSpacing(15)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(5, 8, -1, 5)
        self.state_bsf_pos = QLabel(self.verticalLayoutWidget_11)
        self.state_bsf_pos.setObjectName(u"state_bsf_pos")
        self.state_bsf_pos.setStyleSheet(u"QLabel#state_bsf_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_82.addWidget(self.state_bsf_pos)

        self.label_95 = QLabel(self.verticalLayoutWidget_11)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font6)

        self.horizontalLayout_82.addWidget(self.label_95)

        self.horizontalLayout_82.setStretch(0, 2)
        self.horizontalLayout_82.setStretch(1, 3)

        self.verticalLayout_19.addLayout(self.horizontalLayout_82)

        self.verticalLayout_19.setStretch(0, 1)
        self.verticalLayout_19.setStretch(1, 1)
        self.verticalLayout_19.setStretch(2, 1)
        self.verticalLayout_19.setStretch(3, 1)

        self.horizontalLayout_74.addLayout(self.verticalLayout_19)

        self.horizontalLayout_74.setStretch(0, 4)
        self.horizontalLayout_74.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_74)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 8)

        self.horizontalLayout_17.addLayout(self.verticalLayout_5)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)
        self.horizontalLayout_17.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 15, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.verticalLayoutWidget_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.horizontalLayout_12.addWidget(self.label_2)

        self.progress_bar = QProgressBar(self.verticalLayoutWidget_11)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setSizeIncrement(QSize(0, 1))
        self.progress_bar.setValue(0)

        self.horizontalLayout_12.addWidget(self.progress_bar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 5)
        self.horizontalLayout_12.setStretch(3, 2)

        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.verticalLayout_9.setStretch(0, 2)
        self.verticalLayout_9.setStretch(1, 4)
        self.verticalLayout_9.setStretch(2, 4)
        self.verticalLayout_9.setStretch(3, 9)
        self.verticalLayout_9.setStretch(4, 1)
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
        self.btn_config_data.setText(QCoreApplication.translate("UserWindow", u"Configurar datos", None))
        self.btn_ver_ensayos.setText(QCoreApplication.translate("UserWindow", u"Ver tiempos de \n"
"ensayos", None))
        self.groupBox.setTitle(QCoreApplication.translate("UserWindow", u"Datos de usuario", None))
        self.label.setText(QCoreApplication.translate("UserWindow", u"Operario:", None))
        self.label_operario.setText("")
        self.label_3.setText(QCoreApplication.translate("UserWindow", u"Legajo:", None))
        self.label_legajo.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("UserWindow", u"Datos de formaci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("UserWindow", u"Formaci\u00f3n:", None))
        self.label_formacion.setText("")
        self.label_8.setText(QCoreApplication.translate("UserWindow", u"Coche:", None))
        self.label_coche.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("UserWindow", u"Datos de motor", None))
        self.label_10.setText(QCoreApplication.translate("UserWindow", u"Boguie:", None))
        self.label_boguie.setText("")
        self.label_12.setText(QCoreApplication.translate("UserWindow", u"Motor:", None))
        self.label_motor.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("UserWindow", u"Megado", None))
        self.label_18.setText(QCoreApplication.translate("UserWindow", u"Fase a tierra:", None))
        self.label_fase_tierra.setText("")
        self.label_20.setText(QCoreApplication.translate("UserWindow", u"Fase a rodamiento:", None))
        self.label_rod_tierra.setText("")
        self.label_notificacion.setText(QCoreApplication.translate("UserWindow", u"NOTIFICACION", None))
        self.label_24.setText(QCoreApplication.translate("UserWindow", u"Tiempo \n"
" de ensayo: ", None))
        self.label_23.setText(QCoreApplication.translate("UserWindow", u"Temp. ambiente: ", None))
        self.label_14.setText(QCoreApplication.translate("UserWindow", u"Rodamiento anterior:", None))
        self.label_modelo_rod_ant.setText("")
        self.label_30.setText(QCoreApplication.translate("UserWindow", u"Time stap:", None))
        self.label_time_stap_pos.setText("")
        self.label_26.setText(QCoreApplication.translate("UserWindow", u"Temperatura(\u00b0C)", None))
        self.label_27.setText(QCoreApplication.translate("UserWindow", u"Vib. axial(mm/s2)", None))
        self.label_28.setText(QCoreApplication.translate("UserWindow", u"Vib. radial(mm/s2)", None))
        self.state_bpfo_ant.setText("")
        self.label_94.setText(QCoreApplication.translate("UserWindow", u"BPFO", None))
        self.state_bpfi_ant.setText("")
        self.label_92.setText(QCoreApplication.translate("UserWindow", u"BPFI", None))
        self.state_ftf_ant.setText("")
        self.label_90.setText(QCoreApplication.translate("UserWindow", u"FTF", None))
        self.state_bsf_ant.setText("")
        self.label_96.setText(QCoreApplication.translate("UserWindow", u"BSF", None))
        self.label_16.setText(QCoreApplication.translate("UserWindow", u"Rodamiento posterior:", None))
        self.label_modelo_rod_pos.setText("")
        self.label_29.setText(QCoreApplication.translate("UserWindow", u"Time stap:", None))
        self.label_time_stap_ant.setText("")
        self.label_85.setText(QCoreApplication.translate("UserWindow", u"Temperatura(\u00b0C)", None))
        self.label_86.setText(QCoreApplication.translate("UserWindow", u"Vib. axial(mm/s2)", None))
        self.label_87.setText(QCoreApplication.translate("UserWindow", u"Vib. radial(mm/s2)", None))
        self.state_bpfo_pos.setText("")
        self.label_93.setText(QCoreApplication.translate("UserWindow", u"BPFO", None))
        self.state_bpfi_pos.setText("")
        self.label_91.setText(QCoreApplication.translate("UserWindow", u"BPFI", None))
        self.state_ftf_pos.setText("")
        self.label_89.setText(QCoreApplication.translate("UserWindow", u"FTF", None))
        self.state_bsf_pos.setText("")
        self.label_95.setText(QCoreApplication.translate("UserWindow", u"BSF", None))
        self.label_2.setText(QCoreApplication.translate("UserWindow", u"Progreso", None))
    # retranslateUi

