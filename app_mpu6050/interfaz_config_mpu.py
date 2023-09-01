# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz_config_mpu.ui'
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
        MainWindow.resize(700, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(40, 30, 611, 401))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_cal_accel = QPushButton(self.verticalLayoutWidget_3)
        self.btn_cal_accel.setObjectName(u"btn_cal_accel")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cal_accel.sizePolicy().hasHeightForWidth())
        self.btn_cal_accel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        self.btn_cal_accel.setFont(font)
        self.btn_cal_accel.setMouseTracking(False)
        self.btn_cal_accel.setTabletTracking(False)
        self.btn_cal_accel.setAcceptDrops(False)

        self.verticalLayout_6.addWidget(self.btn_cal_accel)

        self.btn_register = QPushButton(self.verticalLayoutWidget_3)
        self.btn_register.setObjectName(u"btn_register")
        sizePolicy.setHeightForWidth(self.btn_register.sizePolicy().hasHeightForWidth())
        self.btn_register.setSizePolicy(sizePolicy)
        self.btn_register.setFont(font)
        self.btn_register.setMouseTracking(False)
        self.btn_register.setTabletTracking(False)
        self.btn_register.setAcceptDrops(False)

        self.verticalLayout_6.addWidget(self.btn_register)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.groupBox = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget_2 = QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 30, 71, 103))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radbtn_2g = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.radbtn_2g)
        self.radbtn_2g.setObjectName(u"radbtn_2g")
        self.radbtn_2g.setChecked(True)

        self.verticalLayout_2.addWidget(self.radbtn_2g)

        self.radbtn_4g = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_2.addButton(self.radbtn_4g)
        self.radbtn_4g.setObjectName(u"radbtn_4g")

        self.verticalLayout_2.addWidget(self.radbtn_4g)

        self.radbtn_8g = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_2.addButton(self.radbtn_8g)
        self.radbtn_8g.setObjectName(u"radbtn_8g")

        self.verticalLayout_2.addWidget(self.radbtn_8g)

        self.radbtn_16g = QRadioButton(self.verticalLayoutWidget_2)
        self.buttonGroup_2.addButton(self.radbtn_16g)
        self.radbtn_16g.setObjectName(u"radbtn_16g")

        self.verticalLayout_2.addWidget(self.radbtn_16g)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 30, 74, 103))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.radbtn_250d = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.radbtn_250d)
        self.radbtn_250d.setObjectName(u"radbtn_250d")
        self.radbtn_250d.setChecked(True)

        self.verticalLayout_10.addWidget(self.radbtn_250d)

        self.radbtn_500d = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_4.addButton(self.radbtn_500d)
        self.radbtn_500d.setObjectName(u"radbtn_500d")

        self.verticalLayout_10.addWidget(self.radbtn_500d)

        self.radbtn_1000d = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_4.addButton(self.radbtn_1000d)
        self.radbtn_1000d.setObjectName(u"radbtn_1000d")

        self.verticalLayout_10.addWidget(self.radbtn_1000d)

        self.radbtn_2000d = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_4.addButton(self.radbtn_2000d)
        self.radbtn_2000d.setObjectName(u"radbtn_2000d")

        self.verticalLayout_10.addWidget(self.radbtn_2000d)


        self.horizontalLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 171, 132))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.radbtn_10hz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.radbtn_10hz)
        self.radbtn_10hz.setObjectName(u"radbtn_10hz")
        self.radbtn_10hz.setChecked(True)

        self.verticalLayout_8.addWidget(self.radbtn_10hz)

        self.radbtn_100hz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_100hz)
        self.radbtn_100hz.setObjectName(u"radbtn_100hz")

        self.verticalLayout_8.addWidget(self.radbtn_100hz)

        self.radbtn_125hz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_125hz)
        self.radbtn_125hz.setObjectName(u"radbtn_125hz")

        self.verticalLayout_8.addWidget(self.radbtn_125hz)

        self.radbtn_250hz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_250hz)
        self.radbtn_250hz.setObjectName(u"radbtn_250hz")

        self.verticalLayout_8.addWidget(self.radbtn_250hz)

        self.radbtn_400hz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_400hz)
        self.radbtn_400hz.setObjectName(u"radbtn_400hz")

        self.verticalLayout_8.addWidget(self.radbtn_400hz)


        self.horizontalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.radbtn_500hz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_500hz)
        self.radbtn_500hz.setObjectName(u"radbtn_500hz")

        self.verticalLayout_9.addWidget(self.radbtn_500hz)

        self.radbtn_1khz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_1khz)
        self.radbtn_1khz.setObjectName(u"radbtn_1khz")

        self.verticalLayout_9.addWidget(self.radbtn_1khz)

        self.radbtn_2khz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_2khz)
        self.radbtn_2khz.setObjectName(u"radbtn_2khz")

        self.verticalLayout_9.addWidget(self.radbtn_2khz)

        self.radbtn_4khz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_4khz)
        self.radbtn_4khz.setObjectName(u"radbtn_4khz")

        self.verticalLayout_9.addWidget(self.radbtn_4khz)

        self.radbtn_8khz = QRadioButton(self.horizontalLayoutWidget)
        self.buttonGroup_3.addButton(self.radbtn_8khz)
        self.radbtn_8khz.setObjectName(u"radbtn_8khz")

        self.verticalLayout_9.addWidget(self.radbtn_8khz)


        self.horizontalLayout_7.addLayout(self.verticalLayout_9)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 5)

        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.label_notificacion = QLabel(self.verticalLayoutWidget_3)
        self.label_notificacion.setObjectName(u"label_notificacion")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_notificacion.setFont(font1)
        self.label_notificacion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_notificacion)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.lcd_x = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_x.setObjectName(u"lcd_x")

        self.verticalLayout_3.addWidget(self.lcd_x)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.offset_x = QLabel(self.verticalLayoutWidget_3)
        self.offset_x.setObjectName(u"offset_x")
        self.offset_x.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.offset_x)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.lcd_y = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_y.setObjectName(u"lcd_y")

        self.verticalLayout_4.addWidget(self.lcd_y)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.offset_y = QLabel(self.verticalLayoutWidget_3)
        self.offset_y.setObjectName(u"offset_y")
        self.offset_y.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.offset_y)

        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)

        self.lcd_z = QLCDNumber(self.verticalLayoutWidget_3)
        self.lcd_z.setObjectName(u"lcd_z")

        self.verticalLayout_5.addWidget(self.lcd_z)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.offset_z = QLabel(self.verticalLayoutWidget_3)
        self.offset_z.setObjectName(u"offset_z")
        self.offset_z.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.offset_z)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 3)

        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 6, -1, 6)
        self.radbtn_g = QRadioButton(self.verticalLayoutWidget_3)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radbtn_g)
        self.radbtn_g.setObjectName(u"radbtn_g")
        self.radbtn_g.setChecked(True)

        self.verticalLayout.addWidget(self.radbtn_g)

        self.radbtn_mm_s2 = QRadioButton(self.verticalLayoutWidget_3)
        self.buttonGroup.addButton(self.radbtn_mm_s2)
        self.radbtn_mm_s2.setObjectName(u"radbtn_mm_s2")

        self.verticalLayout.addWidget(self.radbtn_mm_s2)

        self.radbtn_m_s2 = QRadioButton(self.verticalLayoutWidget_3)
        self.buttonGroup.addButton(self.radbtn_m_s2)
        self.radbtn_m_s2.setObjectName(u"radbtn_m_s2")

        self.verticalLayout.addWidget(self.radbtn_m_s2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(200, -1, 200, -1)
        self.btn_show_graph = QPushButton(self.verticalLayoutWidget_3)
        self.btn_show_graph.setObjectName(u"btn_show_graph")
        sizePolicy.setHeightForWidth(self.btn_show_graph.sizePolicy().hasHeightForWidth())
        self.btn_show_graph.setSizePolicy(sizePolicy)
        self.btn_show_graph.setFont(font)

        self.horizontalLayout_8.addWidget(self.btn_show_graph)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.verticalLayout_7.setStretch(0, 3)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 2)
        self.verticalLayout_7.setStretch(3, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_cal_accel.setText(QCoreApplication.translate("MainWindow", u"Calibraci\u00f3n \n"
"acelerometro", None))
        self.btn_register.setText(QCoreApplication.translate("MainWindow", u"Iniciar registro", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sensibilidad accel", None))
        self.radbtn_2g.setText(QCoreApplication.translate("MainWindow", u"2G", None))
        self.radbtn_4g.setText(QCoreApplication.translate("MainWindow", u"4G", None))
        self.radbtn_8g.setText(QCoreApplication.translate("MainWindow", u"8G", None))
        self.radbtn_16g.setText(QCoreApplication.translate("MainWindow", u"16G", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Sensibilidad gyro", None))
        self.radbtn_250d.setText(QCoreApplication.translate("MainWindow", u"250\u00b0/s", None))
        self.radbtn_500d.setText(QCoreApplication.translate("MainWindow", u"500\u00b0/s", None))
        self.radbtn_1000d.setText(QCoreApplication.translate("MainWindow", u"1000\u00b0/s", None))
        self.radbtn_2000d.setText(QCoreApplication.translate("MainWindow", u"2000\u00b0/s", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Frecuencia de muestreo", None))
        self.radbtn_10hz.setText(QCoreApplication.translate("MainWindow", u"10Hz", None))
        self.radbtn_100hz.setText(QCoreApplication.translate("MainWindow", u"100Hz", None))
        self.radbtn_125hz.setText(QCoreApplication.translate("MainWindow", u"125Hz", None))
        self.radbtn_250hz.setText(QCoreApplication.translate("MainWindow", u"250Hz", None))
        self.radbtn_400hz.setText(QCoreApplication.translate("MainWindow", u"400Hz", None))
        self.radbtn_500hz.setText(QCoreApplication.translate("MainWindow", u"500Hz", None))
        self.radbtn_1khz.setText(QCoreApplication.translate("MainWindow", u"1kHz", None))
        self.radbtn_2khz.setText(QCoreApplication.translate("MainWindow", u"2kHz", None))
        self.radbtn_4khz.setText(QCoreApplication.translate("MainWindow", u"4kHz", None))
        self.radbtn_8khz.setText(QCoreApplication.translate("MainWindow", u"8kHz", None))
        self.label_notificacion.setText(QCoreApplication.translate("MainWindow", u"NOTIFICACION", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Offset:", None))
        self.offset_x.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Offset:", None))
        self.offset_y.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Offset:", None))
        self.offset_z.setText(QCoreApplication.translate("MainWindow", u"---", None))
        self.radbtn_g.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.radbtn_mm_s2.setText(QCoreApplication.translate("MainWindow", u"mm/s2", None))
        self.radbtn_m_s2.setText(QCoreApplication.translate("MainWindow", u"m/s2", None))
        self.btn_show_graph.setText(QCoreApplication.translate("MainWindow", u"Ver Grafico", None))
    # retranslateUi

