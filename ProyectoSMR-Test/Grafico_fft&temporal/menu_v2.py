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
        MainWindow.resize(1282, 767)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 20, 1231, 711))
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

        self.notificacion = QLabel(self.verticalLayoutWidget_2)
        self.notificacion.setObjectName(u"notificacion")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)
        self.notificacion.setFont(font1)
        self.notificacion.setAlignment(Qt.AlignCenter)

        self.configuraciones.addWidget(self.notificacion)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 20)
        self.ctrl_ensayo = QVBoxLayout()
        self.ctrl_ensayo.setSpacing(4)
        self.ctrl_ensayo.setObjectName(u"ctrl_ensayo")
        self.ctrl_ensayo.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.label_7.setFont(font2)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progress_bar_ensayo.sizePolicy().hasHeightForWidth())
        self.progress_bar_ensayo.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(9)
        self.progress_bar_ensayo.setFont(font3)
        self.progress_bar_ensayo.setValue(50)
        self.progress_bar_ensayo.setInvertedAppearance(False)
        self.progress_bar_ensayo.setTextDirection(QProgressBar.TopToBottom)

        self.ctrl_ensayo.addWidget(self.progress_bar_ensayo)

        self.ctrl_ensayo.setStretch(0, 5)
        self.ctrl_ensayo.setStretch(1, 4)

        self.horizontalLayout_5.addLayout(self.ctrl_ensayo)

        self.btn_forzar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_forzar.setObjectName(u"btn_forzar")
        sizePolicy2.setHeightForWidth(self.btn_forzar.sizePolicy().hasHeightForWidth())
        self.btn_forzar.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        self.btn_forzar.setFont(font4)

        self.horizontalLayout_5.addWidget(self.btn_forzar)

        self.horizontalLayout_5.setStretch(0, 6)
        self.horizontalLayout_5.setStretch(1, 1)

        self.configuraciones.addLayout(self.horizontalLayout_5)

        self.capture = QPushButton(self.verticalLayoutWidget_2)
        self.capture.setObjectName(u"capture")
        sizePolicy2.setHeightForWidth(self.capture.sizePolicy().hasHeightForWidth())
        self.capture.setSizePolicy(sizePolicy2)
        self.capture.setFont(font4)

        self.configuraciones.addWidget(self.capture)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, -1, -1, -1)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lcd_temp_ant = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_temp_ant.setObjectName(u"lcd_temp_ant")
        font5 = QFont()
        font5.setFamily(u"MS Shell Dlg 2")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.lcd_temp_ant.setFont(font5)
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
        self.label_3.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

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
        self.label_4.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

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


        self.configuraciones.addLayout(self.verticalLayout)

        self.configuraciones.setStretch(0, 3)
        self.configuraciones.setStretch(1, 1)
        self.configuraciones.setStretch(2, 1)
        self.configuraciones.setStretch(3, 2)
        self.configuraciones.setStretch(4, 1)
        self.configuraciones.setStretch(5, 3)

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
        self.meas_ant.setSpacing(10)
        self.meas_ant.setObjectName(u"meas_ant")
        self.meas_ant.setContentsMargins(5, 30, 0, 50)
        self.value_sample_ant = QLabel(self.verticalLayoutWidget_2)
        self.value_sample_ant.setObjectName(u"value_sample_ant")
        font6 = QFont()
        font6.setPointSize(14)
        self.value_sample_ant.setFont(font6)
        self.value_sample_ant.setLineWidth(2)
        self.value_sample_ant.setAlignment(Qt.AlignCenter)

        self.meas_ant.addWidget(self.value_sample_ant)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dial_sample_temp = QDial(self.verticalLayoutWidget_2)
        self.dial_sample_temp.setObjectName(u"dial_sample_temp")
        self.dial_sample_temp.setMinimum(1)
        self.dial_sample_temp.setMaximum(1024)
        self.dial_sample_temp.setSingleStep(16)
        self.dial_sample_temp.setValue(1024)
        self.dial_sample_temp.setTracking(True)
        self.dial_sample_temp.setWrapping(False)
        self.dial_sample_temp.setNotchesVisible(True)

        self.verticalLayout_3.addWidget(self.dial_sample_temp)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        font7 = QFont()
        font7.setPointSize(7)
        self.label_8.setFont(font7)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.value_sample_temp = QLabel(self.verticalLayoutWidget_2)
        self.value_sample_temp.setObjectName(u"value_sample_temp")
        self.value_sample_temp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.value_sample_temp)


        self.verticalLayout_3.addLayout(self.verticalLayout_8)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.dial_volt_init_temp = QDial(self.verticalLayoutWidget_2)
        self.dial_volt_init_temp.setObjectName(u"dial_volt_init_temp")
        self.dial_volt_init_temp.setMinimum(0)
        self.dial_volt_init_temp.setMaximum(1024)
        self.dial_volt_init_temp.setSingleStep(16)
        self.dial_volt_init_temp.setValue(0)
        self.dial_volt_init_temp.setNotchesVisible(True)

        self.verticalLayout_7.addWidget(self.dial_volt_init_temp)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_12 = QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_12)

        self.value_volt_init_temp = QLabel(self.verticalLayoutWidget_2)
        self.value_volt_init_temp.setObjectName(u"value_volt_init_temp")
        self.value_volt_init_temp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.value_volt_init_temp)


        self.verticalLayout_7.addLayout(self.verticalLayout_10)


        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.dial_volt_fin_temp = QDial(self.verticalLayoutWidget_2)
        self.dial_volt_fin_temp.setObjectName(u"dial_volt_fin_temp")
        self.dial_volt_fin_temp.setMinimum(1)
        self.dial_volt_fin_temp.setMaximum(1024)
        self.dial_volt_fin_temp.setSingleStep(16)
        self.dial_volt_fin_temp.setValue(1024)
        self.dial_volt_fin_temp.setNotchesVisible(True)

        self.verticalLayout_2.addWidget(self.dial_volt_fin_temp)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_5)

        self.value_volt_fin_temp = QLabel(self.verticalLayoutWidget_2)
        self.value_volt_fin_temp.setObjectName(u"value_volt_fin_temp")
        self.value_volt_fin_temp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.value_volt_fin_temp)


        self.verticalLayout_2.addLayout(self.verticalLayout_11)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.meas_ant.addLayout(self.horizontalLayout)

        self.mag_ant = QLabel(self.verticalLayoutWidget_2)
        self.mag_ant.setObjectName(u"mag_ant")
        sizePolicy2.setHeightForWidth(self.mag_ant.sizePolicy().hasHeightForWidth())
        self.mag_ant.setSizePolicy(sizePolicy2)
        self.mag_ant.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.mag_ant.setAlignment(Qt.AlignCenter)

        self.meas_ant.addWidget(self.mag_ant)

        self.meas_ant.setStretch(0, 2)

        self.layout_ant.addLayout(self.meas_ant)

        self.layout_ant.setStretch(0, 19)
        self.layout_ant.setStretch(1, 9)

        self.mediciones.addLayout(self.layout_ant)

        self.layout_pos = QHBoxLayout()
        self.layout_pos.setSpacing(0)
        self.layout_pos.setObjectName(u"layout_pos")
        self.fft_ant = QVBoxLayout()
        self.fft_ant.setObjectName(u"fft_ant")

        self.layout_pos.addLayout(self.fft_ant)

        self.meas_pos = QVBoxLayout()
        self.meas_pos.setSpacing(10)
        self.meas_pos.setObjectName(u"meas_pos")
        self.meas_pos.setContentsMargins(5, 60, -1, 70)
        self.value_fft_ant = QLabel(self.verticalLayoutWidget_2)
        self.value_fft_ant.setObjectName(u"value_fft_ant")
        self.value_fft_ant.setFont(font6)
        self.value_fft_ant.setLayoutDirection(Qt.RightToLeft)
        self.value_fft_ant.setAlignment(Qt.AlignCenter)

        self.meas_pos.addWidget(self.value_fft_ant)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.dial_freq_init_fft = QDial(self.verticalLayoutWidget_2)
        self.dial_freq_init_fft.setObjectName(u"dial_freq_init_fft")
        self.dial_freq_init_fft.setMinimum(-1)
        self.dial_freq_init_fft.setMaximum(512)
        self.dial_freq_init_fft.setSingleStep(8)
        self.dial_freq_init_fft.setValue(-1)
        self.dial_freq_init_fft.setSliderPosition(-1)
        self.dial_freq_init_fft.setNotchesVisible(True)

        self.verticalLayout_4.addWidget(self.dial_freq_init_fft)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        font8 = QFont()
        font8.setPointSize(6)
        self.label_9.setFont(font8)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_9)

        self.value_freq_init_fft = QLabel(self.verticalLayoutWidget_2)
        self.value_freq_init_fft.setObjectName(u"value_freq_init_fft")
        self.value_freq_init_fft.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.value_freq_init_fft)


        self.verticalLayout_4.addLayout(self.verticalLayout_12)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.dial_freq_fin_fft = QDial(self.verticalLayoutWidget_2)
        self.dial_freq_fin_fft.setObjectName(u"dial_freq_fin_fft")
        self.dial_freq_fin_fft.setMinimum(1)
        self.dial_freq_fin_fft.setMaximum(512)
        self.dial_freq_fin_fft.setSingleStep(8)
        self.dial_freq_fin_fft.setValue(512)
        self.dial_freq_fin_fft.setSliderPosition(512)
        self.dial_freq_fin_fft.setNotchesVisible(True)

        self.verticalLayout_5.addWidget(self.dial_freq_fin_fft)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font8)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_10)

        self.value_freq_fin_fft = QLabel(self.verticalLayoutWidget_2)
        self.value_freq_fin_fft.setObjectName(u"value_freq_fin_fft")
        self.value_freq_fin_fft.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.value_freq_fin_fft)


        self.verticalLayout_5.addLayout(self.verticalLayout_13)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial_amp_init_fft = QDial(self.verticalLayoutWidget_2)
        self.dial_amp_init_fft.setObjectName(u"dial_amp_init_fft")
        self.dial_amp_init_fft.setMinimum(-100)
        self.dial_amp_init_fft.setMaximum(90)
        self.dial_amp_init_fft.setSingleStep(10)
        self.dial_amp_init_fft.setValue(-50)
        self.dial_amp_init_fft.setNotchesVisible(True)

        self.verticalLayout_6.addWidget(self.dial_amp_init_fft)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font8)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_11)

        self.value_amp_init_fft = QLabel(self.verticalLayoutWidget_2)
        self.value_amp_init_fft.setObjectName(u"value_amp_init_fft")
        self.value_amp_init_fft.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.value_amp_init_fft)


        self.verticalLayout_6.addLayout(self.verticalLayout_14)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.dial_amp_fin_fft = QDial(self.verticalLayoutWidget_2)
        self.dial_amp_fin_fft.setObjectName(u"dial_amp_fin_fft")
        self.dial_amp_fin_fft.setMinimum(-90)
        self.dial_amp_fin_fft.setMaximum(100)
        self.dial_amp_fin_fft.setSingleStep(10)
        self.dial_amp_fin_fft.setValue(10)
        self.dial_amp_fin_fft.setNotchesVisible(True)

        self.verticalLayout_15.addWidget(self.dial_amp_fin_fft)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_13)

        self.value_amp_fin_fft = QLabel(self.verticalLayoutWidget_2)
        self.value_amp_fin_fft.setObjectName(u"value_amp_fin_fft")
        self.value_amp_fin_fft.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.value_amp_fin_fft)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.horizontalLayout_6.addLayout(self.verticalLayout_15)


        self.meas_pos.addLayout(self.horizontalLayout_6)

        self.meas_pos.setStretch(0, 2)

        self.layout_pos.addLayout(self.meas_pos)

        self.layout_pos.setStretch(0, 19)
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
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"SMR-Test-Rodamiento Anterior", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Duracion de ensayos:", None))
        self.time_ensayo.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Intervalo entre ensayos:", None))
        self.time_standby.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.notificacion.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tiempo de ensayo:", None))
        self.btn_forzar.setText(QCoreApplication.translate("MainWindow", u"Forzar", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Temp.(\u00b0C):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vib.ax.(m/s2):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Vib.rad.(m/s2):", None))
        self.value_sample_ant.setText(QCoreApplication.translate("MainWindow", u"  Volt.: 0V / Data:0 \n"
"  Sample: 0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Samples[#]", None))
        self.value_sample_temp.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Mag. Initial[V]", None))
        self.value_volt_init_temp.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Mag. Finish[V]", None))
        self.value_volt_fin_temp.setText("")
        self.mag_ant.setText(QCoreApplication.translate("MainWindow", u"  Mag.: 0V      Freq.: 0Hz", None))
        self.value_fft_ant.setText(QCoreApplication.translate("MainWindow", u"  Mag.: 0 dBV \n"
"  Freq.: 0Hz", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Freq. I.[Hz]", None))
        self.value_freq_init_fft.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Freq. F.[Hz]", None))
        self.value_freq_fin_fft.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Amp. I.[dBV]", None))
        self.value_amp_init_fft.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Amp. F.[dBV]", None))
        self.value_amp_fin_fft.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progreso:", None))
    # retranslateUi

