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
        AdminWindow.resize(580, 600)
        self.centralwidget = QWidget(AdminWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 551, 571))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tab_rodamiento = QTabWidget(self.verticalLayoutWidget)
        self.tab_rodamiento.setObjectName(u"tab_rodamiento")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.tab_rodamiento.setFont(font1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayoutWidget_7 = QWidget(self.tab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(20, 20, 551, 441))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_13 = QLabel(self.verticalLayoutWidget_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_9.addWidget(self.label_13)

        self.cbox_modelo_rod_ant = QComboBox(self.verticalLayoutWidget_7)
        self.cbox_modelo_rod_ant.setObjectName(u"cbox_modelo_rod_ant")

        self.horizontalLayout_9.addWidget(self.cbox_modelo_rod_ant)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.verticalLayoutWidget_7)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_8.addWidget(self.label_14)

        self.rad_btn_h_ant = QRadioButton(self.verticalLayoutWidget_7)
        self.rad_btn_h_ant.setObjectName(u"rad_btn_h_ant")

        self.verticalLayout_8.addWidget(self.rad_btn_h_ant)

        self.rad_btn_a_ant = QRadioButton(self.verticalLayoutWidget_7)
        self.rad_btn_a_ant.setObjectName(u"rad_btn_a_ant")

        self.verticalLayout_8.addWidget(self.rad_btn_a_ant)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.verticalLayoutWidget_7)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_9.addWidget(self.label_15)

        self.rad_btn_v300_ant = QRadioButton(self.verticalLayoutWidget_7)
        self.rad_btn_v300_ant.setObjectName(u"rad_btn_v300_ant")

        self.verticalLayout_9.addWidget(self.rad_btn_v300_ant)

        self.rad_btn_v1500_ant = QRadioButton(self.verticalLayoutWidget_7)
        self.rad_btn_v1500_ant.setObjectName(u"rad_btn_v1500_ant")

        self.verticalLayout_9.addWidget(self.rad_btn_v1500_ant)

        self.rad_btn_v1800_ant = QRadioButton(self.verticalLayoutWidget_7)
        self.rad_btn_v1800_ant.setObjectName(u"rad_btn_v1800_ant")

        self.verticalLayout_9.addWidget(self.rad_btn_v1800_ant)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addLayout(self.verticalLayout_9)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_7)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(30, 30, 411, 91))
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

        self.horizontalLayout_12.addWidget(self.label_16)

        self.sbox_bpfo_ant = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_bpfo_ant.setObjectName(u"sbox_bpfo_ant")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbox_bpfo_ant.sizePolicy().hasHeightForWidth())
        self.sbox_bpfo_ant.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.sbox_bpfo_ant)

        self.label_17 = QLabel(self.horizontalLayoutWidget_7)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.label_17)

        self.horizontalLayout_12.setStretch(0, 4)
        self.horizontalLayout_12.setStretch(1, 8)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_18 = QLabel(self.horizontalLayoutWidget_7)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.sbox_bpfi_ant = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_bpfi_ant.setObjectName(u"sbox_bpfi_ant")
        sizePolicy.setHeightForWidth(self.sbox_bpfi_ant.sizePolicy().hasHeightForWidth())
        self.sbox_bpfi_ant.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.sbox_bpfi_ant)

        self.label_19 = QLabel(self.horizontalLayoutWidget_7)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)

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

        self.horizontalLayout_14.addWidget(self.label_20)

        self.sbox_ftf_ant = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_ftf_ant.setObjectName(u"sbox_ftf_ant")
        sizePolicy.setHeightForWidth(self.sbox_ftf_ant.sizePolicy().hasHeightForWidth())
        self.sbox_ftf_ant.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.sbox_ftf_ant)

        self.label_21 = QLabel(self.horizontalLayoutWidget_7)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_14.addWidget(self.label_21)

        self.horizontalLayout_14.setStretch(0, 4)
        self.horizontalLayout_14.setStretch(1, 8)
        self.horizontalLayout_14.setStretch(2, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_22 = QLabel(self.horizontalLayoutWidget_7)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_15.addWidget(self.label_22)

        self.sbox_bsf_ant = QSpinBox(self.horizontalLayoutWidget_7)
        self.sbox_bsf_ant.setObjectName(u"sbox_bsf_ant")
        sizePolicy.setHeightForWidth(self.sbox_bsf_ant.sizePolicy().hasHeightForWidth())
        self.sbox_bsf_ant.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.sbox_bsf_ant)

        self.label_23 = QLabel(self.horizontalLayoutWidget_7)
        self.label_23.setObjectName(u"label_23")

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

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 10, -1, 10)
        self.btn_guardar_ant = QPushButton(self.verticalLayoutWidget_7)
        self.btn_guardar_ant.setObjectName(u"btn_guardar_ant")
        self.btn_guardar_ant.setStyleSheet(u"QPushButton {\n"
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
        self.btn_guardar_ant.setCheckable(False)
        self.btn_guardar_ant.setAutoRepeat(False)
        self.btn_guardar_ant.setAutoDefault(False)
        self.btn_guardar_ant.setFlat(False)

        self.horizontalLayout_16.addWidget(self.btn_guardar_ant)

        self.btn_reset_ant = QPushButton(self.verticalLayoutWidget_7)
        self.btn_reset_ant.setObjectName(u"btn_reset_ant")
        self.btn_reset_ant.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.btn_reset_ant)

        self.btn_new_rod_ant = QPushButton(self.verticalLayoutWidget_7)
        self.btn_new_rod_ant.setObjectName(u"btn_new_rod_ant")
        self.btn_new_rod_ant.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.btn_new_rod_ant)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 3)
        self.verticalLayout_7.setStretch(2, 3)
        self.verticalLayout_7.setStretch(3, 3)
        self.tab_rodamiento.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_2 = QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 529, 441))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.cbox_modelo_rod_pos = QComboBox(self.verticalLayoutWidget_2)
        self.cbox_modelo_rod_pos.setObjectName(u"cbox_modelo_rod_pos")

        self.horizontalLayout.addWidget(self.cbox_modelo_rod_pos)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.rad_btn_h_pos = QRadioButton(self.verticalLayoutWidget_2)
        self.rad_btn_h_pos.setObjectName(u"rad_btn_h_pos")

        self.verticalLayout_3.addWidget(self.rad_btn_h_pos)

        self.rad_btn_a_pos = QRadioButton(self.verticalLayoutWidget_2)
        self.rad_btn_a_pos.setObjectName(u"rad_btn_a_pos")

        self.verticalLayout_3.addWidget(self.rad_btn_a_pos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.rad_btn_v300_pos = QRadioButton(self.verticalLayoutWidget_2)
        self.rad_btn_v300_pos.setObjectName(u"rad_btn_v300_pos")

        self.verticalLayout_4.addWidget(self.rad_btn_v300_pos)

        self.rad_btn_v1500_pos = QRadioButton(self.verticalLayoutWidget_2)
        self.rad_btn_v1500_pos.setObjectName(u"rad_btn_v1500_pos")

        self.verticalLayout_4.addWidget(self.rad_btn_v1500_pos)

        self.rad_btn_v1800_pos = QRadioButton(self.verticalLayoutWidget_2)
        self.rad_btn_v1800_pos.setObjectName(u"rad_btn_v1800_pos")

        self.verticalLayout_4.addWidget(self.rad_btn_v1800_pos)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(30, 30, 411, 91))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.sbox_bpfo_pos = QSpinBox(self.horizontalLayoutWidget_5)
        self.sbox_bpfo_pos.setObjectName(u"sbox_bpfo_pos")
        sizePolicy.setHeightForWidth(self.sbox_bpfo_pos.sizePolicy().hasHeightForWidth())
        self.sbox_bpfo_pos.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.sbox_bpfo_pos)

        self.label_10 = QLabel(self.horizontalLayoutWidget_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.sbox_bpfi_pos = QSpinBox(self.horizontalLayoutWidget_5)
        self.sbox_bpfi_pos.setObjectName(u"sbox_bpfi_pos")
        sizePolicy.setHeightForWidth(self.sbox_bpfi_pos.sizePolicy().hasHeightForWidth())
        self.sbox_bpfi_pos.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.sbox_bpfi_pos)

        self.label_9 = QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 8)
        self.horizontalLayout_4.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_7.addLayout(self.verticalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.sbox_bsf_pos = QSpinBox(self.horizontalLayoutWidget_5)
        self.sbox_bsf_pos.setObjectName(u"sbox_bsf_pos")
        sizePolicy.setHeightForWidth(self.sbox_bsf_pos.sizePolicy().hasHeightForWidth())
        self.sbox_bsf_pos.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.sbox_bsf_pos)

        self.label_11 = QLabel(self.horizontalLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_5.addWidget(self.label_11)

        self.horizontalLayout_5.setStretch(0, 4)
        self.horizontalLayout_5.setStretch(1, 8)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.horizontalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.sbox_ftf_pos = QSpinBox(self.horizontalLayoutWidget_5)
        self.sbox_ftf_pos.setObjectName(u"sbox_ftf_pos")
        sizePolicy.setHeightForWidth(self.sbox_ftf_pos.sizePolicy().hasHeightForWidth())
        self.sbox_ftf_pos.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.sbox_ftf_pos)

        self.label_12 = QLabel(self.horizontalLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 8)
        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalLayout_7.setStretch(0, 7)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 7)

        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 10, -1, 10)
        self.btn_guardar_pos = QPushButton(self.verticalLayoutWidget_2)
        self.btn_guardar_pos.setObjectName(u"btn_guardar_pos")
        self.btn_guardar_pos.setStyleSheet(u"QPushButton {\n"
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
        self.btn_guardar_pos.setCheckable(False)
        self.btn_guardar_pos.setAutoRepeat(False)
        self.btn_guardar_pos.setAutoDefault(False)
        self.btn_guardar_pos.setFlat(False)

        self.horizontalLayout_8.addWidget(self.btn_guardar_pos)

        self.btn_reset_pos = QPushButton(self.verticalLayoutWidget_2)
        self.btn_reset_pos.setObjectName(u"btn_reset_pos")
        self.btn_reset_pos.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_8.addWidget(self.btn_reset_pos)

        self.btn_new_rod_pos = QPushButton(self.verticalLayoutWidget_2)
        self.btn_new_rod_pos.setObjectName(u"btn_new_rod_pos")
        self.btn_new_rod_pos.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_8.addWidget(self.btn_new_rod_pos)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(3, 3)
        self.tab_rodamiento.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tab_rodamiento)

        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)

        self.tab_rodamiento.setCurrentIndex(0)
        self.btn_guardar_ant.setDefault(False)
        self.btn_guardar_pos.setDefault(False)


        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AdminWindow", u"SMR-Menu Administrador", None))
        self.label_13.setText(QCoreApplication.translate("AdminWindow", u"Modelo de rodamiento:", None))
        self.label_14.setText(QCoreApplication.translate("AdminWindow", u"Sentido de rotacion:", None))
        self.rad_btn_h_ant.setText(QCoreApplication.translate("AdminWindow", u"Horario", None))
        self.rad_btn_a_ant.setText(QCoreApplication.translate("AdminWindow", u"Antiorario", None))
        self.label_15.setText(QCoreApplication.translate("AdminWindow", u"Velocidad de motor:", None))
        self.rad_btn_v300_ant.setText(QCoreApplication.translate("AdminWindow", u"300 RPM", None))
        self.rad_btn_v1500_ant.setText(QCoreApplication.translate("AdminWindow", u"1500 RPM", None))
        self.rad_btn_v1800_ant.setText(QCoreApplication.translate("AdminWindow", u"1800 RPM", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AdminWindow", u"Frecuencias a detectar", None))
        self.label_16.setText(QCoreApplication.translate("AdminWindow", u"BPFO", None))
        self.label_17.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.label_18.setText(QCoreApplication.translate("AdminWindow", u"BPFI", None))
        self.label_19.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.label_20.setText(QCoreApplication.translate("AdminWindow", u"FTF", None))
        self.label_21.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.label_22.setText(QCoreApplication.translate("AdminWindow", u"BSF", None))
        self.label_23.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.btn_guardar_ant.setText(QCoreApplication.translate("AdminWindow", u"Guardar \n"
" configuracion", None))
        self.btn_reset_ant.setText(QCoreApplication.translate("AdminWindow", u"Restablecer \n"
"freuencias", None))
        self.btn_new_rod_ant.setText(QCoreApplication.translate("AdminWindow", u"Guardar\n"
" nuevo modelo", None))
        self.tab_rodamiento.setTabText(self.tab_rodamiento.indexOf(self.tab), QCoreApplication.translate("AdminWindow", u"Rodamiento anterior", None))
        self.label_2.setText(QCoreApplication.translate("AdminWindow", u"Modelo de rodamiento:", None))
        self.label_3.setText(QCoreApplication.translate("AdminWindow", u"Sentido de rotacion:", None))
        self.rad_btn_h_pos.setText(QCoreApplication.translate("AdminWindow", u"Horario", None))
        self.rad_btn_a_pos.setText(QCoreApplication.translate("AdminWindow", u"Antiorario", None))
        self.label_4.setText(QCoreApplication.translate("AdminWindow", u"Velocidad de motor:", None))
        self.rad_btn_v300_pos.setText(QCoreApplication.translate("AdminWindow", u"300 RPM", None))
        self.rad_btn_v1500_pos.setText(QCoreApplication.translate("AdminWindow", u"1500 RPM", None))
        self.rad_btn_v1800_pos.setText(QCoreApplication.translate("AdminWindow", u"1800 RPM", None))
        self.groupBox.setTitle(QCoreApplication.translate("AdminWindow", u"Frecuencias a detectar", None))
        self.label_5.setText(QCoreApplication.translate("AdminWindow", u"BPFO", None))
        self.label_10.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.label_6.setText(QCoreApplication.translate("AdminWindow", u"BPFI", None))
        self.label_9.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.label_7.setText(QCoreApplication.translate("AdminWindow", u"BSF", None))
        self.label_11.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.label_8.setText(QCoreApplication.translate("AdminWindow", u"FTF", None))
        self.label_12.setText(QCoreApplication.translate("AdminWindow", u"Hz", None))
        self.btn_guardar_pos.setText(QCoreApplication.translate("AdminWindow", u"Guardar \n"
" configuracion", None))
        self.btn_reset_pos.setText(QCoreApplication.translate("AdminWindow", u"Restablecer \n"
"frecuencias", None))
        self.btn_new_rod_pos.setText(QCoreApplication.translate("AdminWindow", u"Guardar\n"
" nuevo modelo", None))
        self.tab_rodamiento.setTabText(self.tab_rodamiento.indexOf(self.tab_2), QCoreApplication.translate("AdminWindow", u"Rodamiento posterior", None))
    # retranslateUi

