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
        MainWindow.resize(1124, 741)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 20, 1071, 681))
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

        self.groupBox_freq = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_freq.setObjectName(u"groupBox_freq")
        self.groupBox_freq.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.layoutWidget = QWidget(self.groupBox_freq)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 261, 151))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.slider_bpfo = QSlider(self.layoutWidget)
        self.slider_bpfo.setObjectName(u"slider_bpfo")
        self.slider_bpfo.setMinimum(100)
        self.slider_bpfo.setMaximum(19000)
        self.slider_bpfo.setSingleStep(500)
        self.slider_bpfo.setPageStep(500)
        self.slider_bpfo.setValue(15000)
        self.slider_bpfo.setSliderPosition(15000)
        self.slider_bpfo.setOrientation(Qt.Horizontal)
        self.slider_bpfo.setTickPosition(QSlider.NoTicks)
        self.slider_bpfo.setTickInterval(500)

        self.horizontalLayout_6.addWidget(self.slider_bpfo)

        self.label_slider_bpfo = QLabel(self.layoutWidget)
        self.label_slider_bpfo.setObjectName(u"label_slider_bpfo")

        self.horizontalLayout_6.addWidget(self.label_slider_bpfo)

        self.horizontalLayout_6.setStretch(1, 6)
        self.horizontalLayout_6.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.slider_bpfi = QSlider(self.layoutWidget)
        self.slider_bpfi.setObjectName(u"slider_bpfi")
        self.slider_bpfi.setMinimum(100)
        self.slider_bpfi.setMaximum(19000)
        self.slider_bpfi.setSingleStep(500)
        self.slider_bpfi.setPageStep(500)
        self.slider_bpfi.setValue(12000)
        self.slider_bpfi.setOrientation(Qt.Horizontal)
        self.slider_bpfi.setTickInterval(500)

        self.horizontalLayout_7.addWidget(self.slider_bpfi)

        self.label_slider_bpfi = QLabel(self.layoutWidget)
        self.label_slider_bpfi.setObjectName(u"label_slider_bpfi")

        self.horizontalLayout_7.addWidget(self.label_slider_bpfi)

        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.slider_ftf = QSlider(self.layoutWidget)
        self.slider_ftf.setObjectName(u"slider_ftf")
        self.slider_ftf.setMinimum(100)
        self.slider_ftf.setMaximum(19000)
        self.slider_ftf.setSingleStep(500)
        self.slider_ftf.setPageStep(500)
        self.slider_ftf.setValue(900)
        self.slider_ftf.setOrientation(Qt.Horizontal)
        self.slider_ftf.setTickInterval(500)

        self.horizontalLayout_8.addWidget(self.slider_ftf)

        self.label_slider_ftf = QLabel(self.layoutWidget)
        self.label_slider_ftf.setObjectName(u"label_slider_ftf")

        self.horizontalLayout_8.addWidget(self.label_slider_ftf)

        self.horizontalLayout_8.setStretch(1, 6)
        self.horizontalLayout_8.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.slider_bsf = QSlider(self.layoutWidget)
        self.slider_bsf.setObjectName(u"slider_bsf")
        self.slider_bsf.setMinimum(100)
        self.slider_bsf.setMaximum(19000)
        self.slider_bsf.setSingleStep(500)
        self.slider_bsf.setPageStep(500)
        self.slider_bsf.setValue(500)
        self.slider_bsf.setOrientation(Qt.Horizontal)
        self.slider_bsf.setTickInterval(500)

        self.horizontalLayout_9.addWidget(self.slider_bsf)

        self.label_slider_bsf = QLabel(self.layoutWidget)
        self.label_slider_bsf.setObjectName(u"label_slider_bsf")

        self.horizontalLayout_9.addWidget(self.label_slider_bsf)

        self.horizontalLayout_9.setStretch(1, 6)
        self.horizontalLayout_9.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.configuraciones.addWidget(self.groupBox_freq)

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

        self.captureFFT = QPushButton(self.verticalLayoutWidget_2)
        self.captureFFT.setObjectName(u"captureFFT")
        sizePolicy4.setHeightForWidth(self.captureFFT.sizePolicy().hasHeightForWidth())
        self.captureFFT.setSizePolicy(sizePolicy4)
        self.captureFFT.setFont(font1)

        self.configuraciones.addWidget(self.captureFFT)

        self.configuraciones.setStretch(0, 3)
        self.configuraciones.setStretch(1, 4)
        self.configuraciones.setStretch(2, 1)
        self.configuraciones.setStretch(3, 1)
        self.configuraciones.setStretch(4, 1)
        self.configuraciones.setStretch(5, 2)
        self.configuraciones.setStretch(6, 1)

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
        self.fft_ant = QVBoxLayout()
        self.fft_ant.setObjectName(u"fft_ant")

        self.layout_ant.addLayout(self.fft_ant)

        self.fallas_ant = QVBoxLayout()
        self.fallas_ant.setSpacing(6)
        self.fallas_ant.setObjectName(u"fallas_ant")
        self.fallas_ant.setContentsMargins(0, 50, -1, 50)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 7, 0, 7)
        self.led_bpfo_ant = QLabel(self.verticalLayoutWidget_2)
        self.led_bpfo_ant.setObjectName(u"led_bpfo_ant")
        sizePolicy2.setHeightForWidth(self.led_bpfo_ant.sizePolicy().hasHeightForWidth())
        self.led_bpfo_ant.setSizePolicy(sizePolicy2)
        self.led_bpfo_ant.setStyleSheet(u"QLabel#led_bpfo_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")
        self.led_bpfo_ant.setScaledContents(True)
        self.led_bpfo_ant.setMargin(0)
        self.led_bpfo_ant.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_13.addWidget(self.led_bpfo_ant)

        self.label_18 = QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font3)
        self.label_18.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 3)

        self.fallas_ant.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 7, 0, 7)
        self.led_bpfi_ant = QLabel(self.verticalLayoutWidget_2)
        self.led_bpfi_ant.setObjectName(u"led_bpfi_ant")
        self.led_bpfi_ant.setStyleSheet(u"QLabel#led_bpfi_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_14.addWidget(self.led_bpfi_ant)

        self.label_20 = QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_14.addWidget(self.label_20)

        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 3)

        self.fallas_ant.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 7, 0, 7)
        self.led_ftf_ant = QLabel(self.verticalLayoutWidget_2)
        self.led_ftf_ant.setObjectName(u"led_ftf_ant")
        self.led_ftf_ant.setStyleSheet(u"QLabel#led_ftf_ant{\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_17.addWidget(self.led_ftf_ant)

        self.label_27 = QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_17.addWidget(self.label_27)

        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(1, 3)

        self.fallas_ant.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 7, 0, 7)
        self.led_bsf_ant = QLabel(self.verticalLayoutWidget_2)
        self.led_bsf_ant.setObjectName(u"led_bsf_ant")
        self.led_bsf_ant.setStyleSheet(u"QLabel#led_bsf_ant {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_18.addWidget(self.led_bsf_ant)

        self.label_29 = QLabel(self.verticalLayoutWidget_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_18.addWidget(self.label_29)

        self.horizontalLayout_18.setStretch(0, 2)
        self.horizontalLayout_18.setStretch(1, 3)

        self.fallas_ant.addLayout(self.horizontalLayout_18)


        self.layout_ant.addLayout(self.fallas_ant)

        self.meas_ant = QVBoxLayout()
        self.meas_ant.setObjectName(u"meas_ant")
        self.meas_ant.setContentsMargins(5, 50, 0, 70)
        self.value_fft_ant = QLabel(self.verticalLayoutWidget_2)
        self.value_fft_ant.setObjectName(u"value_fft_ant")
        font5 = QFont()
        font5.setPointSize(14)
        self.value_fft_ant.setFont(font5)
        self.value_fft_ant.setLineWidth(2)

        self.meas_ant.addWidget(self.value_fft_ant)

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


        self.layout_ant.addLayout(self.meas_ant)

        self.layout_ant.setStretch(0, 20)
        self.layout_ant.setStretch(1, 4)
        self.layout_ant.setStretch(2, 9)

        self.mediciones.addLayout(self.layout_ant)

        self.layout_pos = QHBoxLayout()
        self.layout_pos.setSpacing(0)
        self.layout_pos.setObjectName(u"layout_pos")
        self.fft_pos = QVBoxLayout()
        self.fft_pos.setObjectName(u"fft_pos")

        self.layout_pos.addLayout(self.fft_pos)

        self.fallas_pos = QVBoxLayout()
        self.fallas_pos.setSpacing(7)
        self.fallas_pos.setObjectName(u"fallas_pos")
        self.fallas_pos.setContentsMargins(-1, 50, -1, 50)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 7, 0, 7)
        self.led_bpfo_pos = QLabel(self.verticalLayoutWidget_2)
        self.led_bpfo_pos.setObjectName(u"led_bpfo_pos")
        sizePolicy2.setHeightForWidth(self.led_bpfo_pos.sizePolicy().hasHeightForWidth())
        self.led_bpfo_pos.setSizePolicy(sizePolicy2)
        self.led_bpfo_pos.setStyleSheet(u"QLabel#led_bpfo_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")
        self.led_bpfo_pos.setScaledContents(True)
        self.led_bpfo_pos.setMargin(0)
        self.led_bpfo_pos.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_15.addWidget(self.led_bpfo_pos)

        self.label_19 = QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_15.addWidget(self.label_19)

        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 3)

        self.fallas_pos.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 7, 0, 7)
        self.led_bpfi_pos = QLabel(self.verticalLayoutWidget_2)
        self.led_bpfi_pos.setObjectName(u"led_bpfi_pos")
        self.led_bpfi_pos.setStyleSheet(u"QLabel#led_bpfi_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_21.addWidget(self.led_bpfi_pos)

        self.label_21 = QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_21.addWidget(self.label_21)

        self.horizontalLayout_21.setStretch(0, 2)
        self.horizontalLayout_21.setStretch(1, 3)

        self.fallas_pos.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 7, 0, 7)
        self.led_ftf_pos = QLabel(self.verticalLayoutWidget_2)
        self.led_ftf_pos.setObjectName(u"led_ftf_pos")
        self.led_ftf_pos.setStyleSheet(u"QLabel#led_ftf_pos{\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_22.addWidget(self.led_ftf_pos)

        self.label_28 = QLabel(self.verticalLayoutWidget_2)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_22.addWidget(self.label_28)

        self.horizontalLayout_22.setStretch(0, 2)
        self.horizontalLayout_22.setStretch(1, 3)

        self.fallas_pos.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 7, 0, 7)
        self.led_bsf_pos = QLabel(self.verticalLayoutWidget_2)
        self.led_bsf_pos.setObjectName(u"led_bsf_pos")
        self.led_bsf_pos.setStyleSheet(u"QLabel#led_bsf_pos {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_23.addWidget(self.led_bsf_pos)

        self.label_30 = QLabel(self.verticalLayoutWidget_2)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setStyleSheet(u"font: 11pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_23.addWidget(self.label_30)

        self.horizontalLayout_23.setStretch(0, 2)
        self.horizontalLayout_23.setStretch(1, 3)

        self.fallas_pos.addLayout(self.horizontalLayout_23)


        self.layout_pos.addLayout(self.fallas_pos)

        self.meas_pos = QVBoxLayout()
        self.meas_pos.setObjectName(u"meas_pos")
        self.meas_pos.setContentsMargins(5, 50, -1, 70)
        self.value_fft_pos = QLabel(self.verticalLayoutWidget_2)
        self.value_fft_pos.setObjectName(u"value_fft_pos")
        self.value_fft_pos.setFont(font5)

        self.meas_pos.addWidget(self.value_fft_pos)

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


        self.layout_pos.addLayout(self.meas_pos)

        self.layout_pos.setStretch(0, 20)
        self.layout_pos.setStretch(1, 4)
        self.layout_pos.setStretch(2, 9)

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
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"SMR-Interfaz de personal de puesta en marcha", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Duracion de ensayos:", None))
        self.time_ensayo.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Intervalo entre ensayos:", None))
        self.time_standby.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.groupBox_freq.setTitle(QCoreApplication.translate("MainWindow", u"Frecuencias a detectar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BPFO", None))
        self.label_slider_bpfo.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"BPFI", None))
        self.label_slider_bpfi.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"FTF", None))
        self.label_slider_ftf.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"BSF", None))
        self.label_slider_bsf.setText("")
        self.led_ant.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Anterior", None))
        self.led_pos.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Posterior", None))
        self.notificacion.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tiempo de ensayo:", None))
        self.btn_forzar.setText(QCoreApplication.translate("MainWindow", u"Forzar", None))
        self.captureFFT.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.led_bpfo_ant.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"BPFO", None))
        self.led_bpfi_ant.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"BPFI", None))
        self.led_ftf_ant.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"FTF", None))
        self.led_bsf_ant.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"BSF", None))
        self.value_fft_ant.setText(QCoreApplication.translate("MainWindow", u"  Freq.: 0 Hz \n"
"  Mag.: 0dBV", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Temp.(\u00b0C):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vib.ax.(m/s2):", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Vib.rad.(m/s2):", None))
        self.led_bpfo_pos.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"BPFO", None))
        self.led_bpfi_pos.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"BPFI", None))
        self.led_ftf_pos.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"FTF", None))
        self.led_bsf_pos.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"BSF", None))
        self.value_fft_pos.setText(QCoreApplication.translate("MainWindow", u"  Freq.: 0 Hz \n"
"  Mag.: 0dBV", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Temp.(\u00b0C):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Vib.ax.(m/s2):", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Vib.rad.(m/s2):", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progreso:", None))
    # retranslateUi

