# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_v2.ui'
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
        MainWindow.resize(1078, 739)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 20, 1031, 682))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.verticalLayoutWidget_2)
        self.titulo.setObjectName(u"titulo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.titulo.setFont(font)
        self.titulo.setLayoutDirection(Qt.LeftToRight)
        self.titulo.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")
        self.titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.titulo)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.configuraciones = QVBoxLayout()
        self.configuraciones.setSpacing(10)
        self.configuraciones.setObjectName(u"configuraciones")
        self.configuraciones.setContentsMargins(-1, 10, 10, -1)
        self.conf_tiempos = QVBoxLayout()
        self.conf_tiempos.setObjectName(u"conf_tiempos")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, -1)
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.time_ensayo = QTimeEdit(self.verticalLayoutWidget_2)
        self.time_ensayo.setObjectName(u"time_ensayo")
        self.time_ensayo.setFocusPolicy(Qt.NoFocus)
        self.time_ensayo.setContextMenuPolicy(Qt.NoContextMenu)
        self.time_ensayo.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.time_ensayo.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.time_ensayo.setProperty("showGroupSeparator", False)
        self.time_ensayo.setCurrentSection(QDateTimeEdit.SecondSection)
        self.time_ensayo.setCalendarPopup(False)
        self.time_ensayo.setCurrentSectionIndex(1)
        self.time_ensayo.setTimeSpec(Qt.LocalTime)
        self.time_ensayo.setTime(QTime(0, 0, 30))

        self.horizontalLayout_10.addWidget(self.time_ensayo)

        self.horizontalLayout_10.setStretch(0, 6)
        self.horizontalLayout_10.setStretch(1, 2)

        self.conf_tiempos.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, -1)
        self.label_15 = QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_19.addWidget(self.label_15)

        self.time_standby = QTimeEdit(self.verticalLayoutWidget_2)
        self.time_standby.setObjectName(u"time_standby")
        self.time_standby.setFocusPolicy(Qt.NoFocus)
        self.time_standby.setContextMenuPolicy(Qt.NoContextMenu)
        self.time_standby.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.time_standby.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.time_standby.setProperty("showGroupSeparator", False)
        self.time_standby.setCurrentSection(QDateTimeEdit.SecondSection)
        self.time_standby.setCalendarPopup(False)
        self.time_standby.setCurrentSectionIndex(1)
        self.time_standby.setTime(QTime(0, 0, 10))

        self.horizontalLayout_19.addWidget(self.time_standby)

        self.horizontalLayout_19.setStretch(0, 6)
        self.horizontalLayout_19.setStretch(1, 2)

        self.conf_tiempos.addLayout(self.horizontalLayout_19)

        self.botones = QHBoxLayout()
        self.botones.setObjectName(u"botones")
        self.botones.setContentsMargins(0, -1, 0, 0)
        self.btn_finish = QPushButton(self.verticalLayoutWidget_2)
        self.btn_finish.setObjectName(u"btn_finish")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_finish.sizePolicy().hasHeightForWidth())
        self.btn_finish.setSizePolicy(sizePolicy1)
        self.btn_finish.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.botones.addWidget(self.btn_finish)

        self.btn_init = QPushButton(self.verticalLayoutWidget_2)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy1.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy1)
        self.btn_init.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.botones.addWidget(self.btn_init)


        self.conf_tiempos.addLayout(self.botones)


        self.configuraciones.addLayout(self.conf_tiempos)

        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.configuraciones.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.status_anterior = QHBoxLayout()
        self.status_anterior.setSpacing(5)
        self.status_anterior.setObjectName(u"status_anterior")
        self.status_anterior.setContentsMargins(10, 10, -1, 10)
        self.led_ant = QLabel(self.verticalLayoutWidget_2)
        self.led_ant.setObjectName(u"led_ant")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.led_ant.sizePolicy().hasHeightForWidth())
        self.led_ant.setSizePolicy(sizePolicy2)
        self.led_ant.setStyleSheet(u"QLabel#led_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")
        self.led_ant.setScaledContents(True)
        self.led_ant.setMargin(0)
        self.led_ant.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.status_anterior.addWidget(self.led_ant)

        self.label_16 = QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_16.setFont(font1)
        self.label_16.setLayoutDirection(Qt.RightToLeft)
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.status_anterior.addWidget(self.label_16)

        self.status_anterior.setStretch(0, 2)
        self.status_anterior.setStretch(1, 3)

        self.horizontalLayout.addLayout(self.status_anterior)

        self.status_posterior = QHBoxLayout()
        self.status_posterior.setSpacing(5)
        self.status_posterior.setObjectName(u"status_posterior")
        self.status_posterior.setContentsMargins(10, 10, 0, 10)
        self.led_pos = QLabel(self.verticalLayoutWidget_2)
        self.led_pos.setObjectName(u"led_pos")
        sizePolicy2.setHeightForWidth(self.led_pos.sizePolicy().hasHeightForWidth())
        self.led_pos.setSizePolicy(sizePolicy2)
        self.led_pos.setStyleSheet(u"QLabel#led_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")
        self.led_pos.setScaledContents(True)
        self.led_pos.setMargin(0)
        self.led_pos.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.status_posterior.addWidget(self.led_pos)

        self.label_17 = QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.status_posterior.addWidget(self.label_17)

        self.status_posterior.setStretch(0, 2)
        self.status_posterior.setStretch(1, 3)

        self.horizontalLayout.addLayout(self.status_posterior)


        self.configuraciones.addLayout(self.horizontalLayout)

        self.notificacion = QLabel(self.verticalLayoutWidget_2)
        self.notificacion.setObjectName(u"notificacion")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setWeight(50)
        self.notificacion.setFont(font2)
        self.notificacion.setAlignment(Qt.AlignCenter)

        self.configuraciones.addWidget(self.notificacion)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ctrl_ensayo = QVBoxLayout()
        self.ctrl_ensayo.setSpacing(4)
        self.ctrl_ensayo.setObjectName(u"ctrl_ensayo")
        self.ctrl_ensayo.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.lcd_time_ensayo = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_time_ensayo.setObjectName(u"lcd_time_ensayo")
        self.lcd_time_ensayo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_time_ensayo.setSmallDecimalPoint(True)
        self.lcd_time_ensayo.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_11.addWidget(self.lcd_time_ensayo)

        self.horizontalLayout_11.setStretch(1, 5)

        self.ctrl_ensayo.addLayout(self.horizontalLayout_11)

        self.progress_bar_ensayo = QProgressBar(self.verticalLayoutWidget_2)
        self.progress_bar_ensayo.setObjectName(u"progress_bar_ensayo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progress_bar_ensayo.sizePolicy().hasHeightForWidth())
        self.progress_bar_ensayo.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setPointSize(9)
        self.progress_bar_ensayo.setFont(font4)
        self.progress_bar_ensayo.setValue(50)
        self.progress_bar_ensayo.setInvertedAppearance(False)
        self.progress_bar_ensayo.setTextDirection(QProgressBar.TopToBottom)

        self.ctrl_ensayo.addWidget(self.progress_bar_ensayo)

        self.ctrl_ensayo.setStretch(0, 2)
        self.ctrl_ensayo.setStretch(1, 6)

        self.horizontalLayout_5.addLayout(self.ctrl_ensayo)

        self.btn_forzar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_forzar.setObjectName(u"btn_forzar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_forzar.sizePolicy().hasHeightForWidth())
        self.btn_forzar.setSizePolicy(sizePolicy4)
        self.btn_forzar.setFont(font1)

        self.horizontalLayout_5.addWidget(self.btn_forzar)

        self.horizontalLayout_5.setStretch(0, 6)
        self.horizontalLayout_5.setStretch(1, 1)

        self.configuraciones.addLayout(self.horizontalLayout_5)

        self.capture = QPushButton(self.verticalLayoutWidget_2)
        self.capture.setObjectName(u"capture")
        sizePolicy4.setHeightForWidth(self.capture.sizePolicy().hasHeightForWidth())
        self.capture.setSizePolicy(sizePolicy4)
        self.capture.setFont(font1)

        self.configuraciones.addWidget(self.capture)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.configuraciones.addItem(self.verticalSpacer)

        self.configuraciones.setStretch(0, 3)
        self.configuraciones.setStretch(1, 1)
        self.configuraciones.setStretch(2, 1)
        self.configuraciones.setStretch(3, 1)
        self.configuraciones.setStretch(4, 2)
        self.configuraciones.setStretch(5, 1)
        self.configuraciones.setStretch(6, 4)

        self.horizontalLayout_20.addLayout(self.configuraciones)

        self.line_4 = QFrame(self.verticalLayoutWidget_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_20.addWidget(self.line_4)

        self.mediciones = QVBoxLayout()
        self.mediciones.setSpacing(0)
        self.mediciones.setObjectName(u"mediciones")
        self.layout_ant = QHBoxLayout()
        self.layout_ant.setSpacing(0)
        self.layout_ant.setObjectName(u"layout_ant")
        self.samples_ant = QVBoxLayout()
        self.samples_ant.setObjectName(u"samples_ant")

        self.layout_ant.addLayout(self.samples_ant)

        self.meas_ant = QVBoxLayout()
        self.meas_ant.setObjectName(u"meas_ant")
        self.meas_ant.setContentsMargins(5, 30, 0, 50)
        self.value_sample_ant = QLabel(self.verticalLayoutWidget_2)
        self.value_sample_ant.setObjectName(u"value_sample_ant")
        font5 = QFont()
        font5.setPointSize(14)
        self.value_sample_ant.setFont(font5)
        self.value_sample_ant.setLineWidth(2)

        self.meas_ant.addWidget(self.value_sample_ant)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lcd_temp_ant = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_temp_ant.setObjectName(u"lcd_temp_ant")
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.lcd_temp_ant.setFont(font6)
        self.lcd_temp_ant.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_temp_ant.setSmallDecimalPoint(True)
        self.lcd_temp_ant.setDigitCount(6)
        self.lcd_temp_ant.setMode(QLCDNumber.Dec)
        self.lcd_temp_ant.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_temp_ant.setProperty("value", 0.000000000000000)
        self.lcd_temp_ant.setProperty("intValue", 0)

        self.horizontalLayout_2.addWidget(self.lcd_temp_ant)

        self.horizontalLayout_2.setStretch(0, 8)
        self.horizontalLayout_2.setStretch(1, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lcd_axial_ant = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_axial_ant.setObjectName(u"lcd_axial_ant")
        self.lcd_axial_ant.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_axial_ant.setSmallDecimalPoint(True)
        self.lcd_axial_ant.setDigitCount(6)
        self.lcd_axial_ant.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_3.addWidget(self.lcd_axial_ant)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, -1, -1, -1)
        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lcd_radial_ant = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_radial_ant.setObjectName(u"lcd_radial_ant")
        self.lcd_radial_ant.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_radial_ant.setSmallDecimalPoint(True)
        self.lcd_radial_ant.setDigitCount(6)
        self.lcd_radial_ant.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_4.addWidget(self.lcd_radial_ant)

        self.horizontalLayout_4.setStretch(0, 8)
        self.horizontalLayout_4.setStretch(1, 6)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.meas_ant.addLayout(self.verticalLayout)

        self.mag_ant = QLabel(self.verticalLayoutWidget_2)
        self.mag_ant.setObjectName(u"mag_ant")
        sizePolicy4.setHeightForWidth(self.mag_ant.sizePolicy().hasHeightForWidth())
        self.mag_ant.setSizePolicy(sizePolicy4)
        self.mag_ant.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.meas_ant.addWidget(self.mag_ant)

        self.meas_ant.setStretch(0, 2)
        self.meas_ant.setStretch(1, 2)

        self.layout_ant.addLayout(self.meas_ant)

        self.layout_ant.setStretch(0, 20)
        self.layout_ant.setStretch(1, 9)

        self.mediciones.addLayout(self.layout_ant)

        self.layout_pos = QHBoxLayout()
        self.layout_pos.setSpacing(0)
        self.layout_pos.setObjectName(u"layout_pos")
        self.samples_pos = QVBoxLayout()
        self.samples_pos.setObjectName(u"samples_pos")

        self.layout_pos.addLayout(self.samples_pos)

        self.meas_pos = QVBoxLayout()
        self.meas_pos.setObjectName(u"meas_pos")
        self.meas_pos.setContentsMargins(5, 30, -1, 50)
        self.value_sample_pos = QLabel(self.verticalLayoutWidget_2)
        self.value_sample_pos.setObjectName(u"value_sample_pos")
        self.value_sample_pos.setFont(font5)

        self.meas_pos.addWidget(self.value_sample_pos)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, -1, 0, -1)
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.lcd_temp_pos = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_temp_pos.setObjectName(u"lcd_temp_pos")
        self.lcd_temp_pos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_temp_pos.setSmallDecimalPoint(True)
        self.lcd_temp_pos.setDigitCount(6)
        self.lcd_temp_pos.setMode(QLCDNumber.Dec)
        self.lcd_temp_pos.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_temp_pos.setProperty("value", 0.000000000000000)
        self.lcd_temp_pos.setProperty("intValue", 0)

        self.horizontalLayout_12.addWidget(self.lcd_temp_pos)

        self.horizontalLayout_12.setStretch(0, 8)
        self.horizontalLayout_12.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(10, -1, 0, -1)
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_24.addWidget(self.label_10)

        self.lcd_axial_pos = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_axial_pos.setObjectName(u"lcd_axial_pos")
        self.lcd_axial_pos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_axial_pos.setSmallDecimalPoint(True)
        self.lcd_axial_pos.setDigitCount(6)
        self.lcd_axial_pos.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_24.addWidget(self.lcd_axial_pos)

        self.horizontalLayout_24.setStretch(0, 8)
        self.horizontalLayout_24.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(10, -1, -1, -1)
        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"font: 9pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_25.addWidget(self.label_13)

        self.lcd_radial_pos = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_radial_pos.setObjectName(u"lcd_radial_pos")
        self.lcd_radial_pos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_radial_pos.setSmallDecimalPoint(True)
        self.lcd_radial_pos.setDigitCount(6)
        self.lcd_radial_pos.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_25.addWidget(self.lcd_radial_pos)

        self.horizontalLayout_25.setStretch(0, 8)
        self.horizontalLayout_25.setStretch(1, 6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_25)


        self.meas_pos.addLayout(self.verticalLayout_2)

        self.mag_pos = QLabel(self.verticalLayoutWidget_2)
        self.mag_pos.setObjectName(u"mag_pos")
        sizePolicy4.setHeightForWidth(self.mag_pos.sizePolicy().hasHeightForWidth())
        self.mag_pos.setSizePolicy(sizePolicy4)
        self.mag_pos.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.meas_pos.addWidget(self.mag_pos)

        self.meas_pos.setStretch(0, 2)
        self.meas_pos.setStretch(1, 2)

        self.layout_pos.addLayout(self.meas_pos)

        self.layout_pos.setStretch(0, 20)
        self.layout_pos.setStretch(1, 9)

        self.mediciones.addLayout(self.layout_pos)

        self.progress = QHBoxLayout()
        self.progress.setObjectName(u"progress")
        self.progress.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.progress.addItem(self.horizontalSpacer)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.progress.addWidget(self.label)

        self.progress_bar_programa = QProgressBar(self.verticalLayoutWidget_2)
        self.progress_bar_programa.setObjectName(u"progress_bar_programa")
        self.progress_bar_programa.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.progress_bar_programa.setValue(0)

        self.progress.addWidget(self.progress_bar_programa)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.progress.addItem(self.horizontalSpacer_2)

        self.progress.setStretch(0, 2)
        self.progress.setStretch(1, 1)
        self.progress.setStretch(2, 10)
        self.progress.setStretch(3, 2)

        self.mediciones.addLayout(self.progress)

        self.mediciones.setStretch(0, 10)
        self.mediciones.setStretch(1, 10)
        self.mediciones.setStretch(2, 1)

        self.horizontalLayout_20.addLayout(self.mediciones)

        self.horizontalLayout_20.setStretch(0, 5)
        self.horizontalLayout_20.setStretch(1, 1)
        self.horizontalLayout_20.setStretch(2, 15)

        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 18)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"SMR-Grafico temporal", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Duracion de ensayos:", None))
        self.time_ensayo.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Intervalo entre ensayos:", None))
        self.time_standby.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.led_ant.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.led_pos.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Posterior", None))
        self.notificacion.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tiempo de ensayo:", None))
        self.btn_forzar.setText(QCoreApplication.translate("MainWindow", u"Forzar", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.value_sample_ant.setText(QCoreApplication.translate("MainWindow", u"  Volt.: 0 V \n"
"  Sample: 0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Temp.(\u00b0C):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vib.ax.(m/s2):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Vib.rad.(m/s2):", None))
        self.mag_ant.setText(QCoreApplication.translate("MainWindow", u"    Mag.:", None))
        self.value_sample_pos.setText(QCoreApplication.translate("MainWindow", u"  Volt.: 0 V \n"
"  Sample: 0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Temp.(\u00b0C):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Vib.ax.(m/s2):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Vib.rad.(m/s2):", None))
        self.mag_pos.setText(QCoreApplication.translate("MainWindow", u"    Mag.:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progreso:", None))
    # retranslateUi

