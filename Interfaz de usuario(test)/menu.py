# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
        MainWindow.resize(1013, 690)
        MainWindow.setStyleSheet(u"background-color: #EAEAEA;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 10, 971, 641))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(Qt.LeftToRight)
        self.label_25.setStyleSheet(u"font: 75 26pt \"MS Shell Dlg 2\";")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_25)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(20, 20, 20, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_21.addWidget(self.label_8)

        self.host_broker = QLineEdit(self.verticalLayoutWidget_2)
        self.host_broker.setObjectName(u"host_broker")
        font1 = QFont()
        font1.setPointSize(12)
        self.host_broker.setFont(font1)
        self.host_broker.setFocusPolicy(Qt.ClickFocus)
        self.host_broker.setAutoFillBackground(False)
        self.host_broker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.host_broker.setMaxLength(15)
        self.host_broker.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.host_broker)

        self.label_10 = QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_21.addWidget(self.label_10)

        self.port_broker = QLineEdit(self.verticalLayoutWidget_2)
        self.port_broker.setObjectName(u"port_broker")
        self.port_broker.setFont(font1)
        self.port_broker.setFocusPolicy(Qt.ClickFocus)
        self.port_broker.setAutoFillBackground(False)
        self.port_broker.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.port_broker.setMaxLength(4)
        self.port_broker.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.port_broker)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 21)
        self.horizontalLayout_21.setStretch(2, 2)
        self.horizontalLayout_21.setStretch(3, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 0, 20, -1)
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.label_6)

        self.time_ensayo = QTimeEdit(self.verticalLayoutWidget_2)
        self.time_ensayo.setObjectName(u"time_ensayo")
        self.time_ensayo.setFocusPolicy(Qt.ClickFocus)
        self.time_ensayo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.time_ensayo.setAlignment(Qt.AlignCenter)
        self.time_ensayo.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.time_ensayo.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.time_ensayo.setProperty("showGroupSeparator", False)
        self.time_ensayo.setCurrentSection(QDateTimeEdit.SecondSection)
        self.time_ensayo.setCalendarPopup(False)
        self.time_ensayo.setCurrentSectionIndex(1)
        self.time_ensayo.setTime(QTime(0, 0, 0))

        self.horizontalLayout_10.addWidget(self.time_ensayo)

        self.horizontalLayout_10.setStretch(0, 4)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(20, -1, 20, 10)
        self.btn_finish = QPushButton(self.verticalLayoutWidget_2)
        self.btn_finish.setObjectName(u"btn_finish")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_finish.sizePolicy().hasHeightForWidth())
        self.btn_finish.setSizePolicy(sizePolicy1)
        self.btn_finish.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_16.addWidget(self.btn_finish)

        self.btn_init = QPushButton(self.verticalLayoutWidget_2)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy1.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy1)
        self.btn_init.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_16.addWidget(self.btn_init)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.notificacion = QLabel(self.verticalLayoutWidget_2)
        self.notificacion.setObjectName(u"notificacion")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setWeight(50)
        self.notificacion.setFont(font2)
        self.notificacion.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.notificacion)

        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(2, 2)

        self.horizontalLayout_19.addLayout(self.verticalLayout_10)

        self.groupBox_freq = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_freq.setObjectName(u"groupBox_freq")
        self.groupBox_freq.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.horizontalLayoutWidget_5 = QWidget(self.groupBox_freq)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 40, 501, 125))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.horizontalLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_6.addWidget(self.label_9)

        self.slider_bpfo = QSlider(self.horizontalLayoutWidget_5)
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

        self.label_slider_bpfo = QLabel(self.horizontalLayoutWidget_5)
        self.label_slider_bpfo.setObjectName(u"label_slider_bpfo")

        self.horizontalLayout_6.addWidget(self.label_slider_bpfo)

        self.horizontalLayout_6.setStretch(1, 6)
        self.horizontalLayout_6.setStretch(2, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_11 = QLabel(self.horizontalLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.slider_bpfi = QSlider(self.horizontalLayoutWidget_5)
        self.slider_bpfi.setObjectName(u"slider_bpfi")
        self.slider_bpfi.setMinimum(100)
        self.slider_bpfi.setMaximum(19000)
        self.slider_bpfi.setSingleStep(500)
        self.slider_bpfi.setPageStep(500)
        self.slider_bpfi.setValue(12000)
        self.slider_bpfi.setOrientation(Qt.Horizontal)
        self.slider_bpfi.setTickInterval(500)

        self.horizontalLayout_7.addWidget(self.slider_bpfi)

        self.label_slider_bpfi = QLabel(self.horizontalLayoutWidget_5)
        self.label_slider_bpfi.setObjectName(u"label_slider_bpfi")

        self.horizontalLayout_7.addWidget(self.label_slider_bpfi)

        self.horizontalLayout_7.setStretch(1, 6)
        self.horizontalLayout_7.setStretch(2, 4)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.horizontalLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.slider_ftf = QSlider(self.horizontalLayoutWidget_5)
        self.slider_ftf.setObjectName(u"slider_ftf")
        self.slider_ftf.setMinimum(100)
        self.slider_ftf.setMaximum(19000)
        self.slider_ftf.setSingleStep(500)
        self.slider_ftf.setPageStep(500)
        self.slider_ftf.setValue(900)
        self.slider_ftf.setOrientation(Qt.Horizontal)
        self.slider_ftf.setTickInterval(500)

        self.horizontalLayout_8.addWidget(self.slider_ftf)

        self.label_slider_ftf = QLabel(self.horizontalLayoutWidget_5)
        self.label_slider_ftf.setObjectName(u"label_slider_ftf")

        self.horizontalLayout_8.addWidget(self.label_slider_ftf)

        self.horizontalLayout_8.setStretch(1, 6)
        self.horizontalLayout_8.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.horizontalLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.slider_bsf = QSlider(self.horizontalLayoutWidget_5)
        self.slider_bsf.setObjectName(u"slider_bsf")
        self.slider_bsf.setMinimum(100)
        self.slider_bsf.setMaximum(19000)
        self.slider_bsf.setSingleStep(500)
        self.slider_bsf.setPageStep(500)
        self.slider_bsf.setValue(500)
        self.slider_bsf.setOrientation(Qt.Horizontal)
        self.slider_bsf.setTickInterval(500)

        self.horizontalLayout_9.addWidget(self.slider_bsf)

        self.label_slider_bsf = QLabel(self.horizontalLayoutWidget_5)
        self.label_slider_bsf.setObjectName(u"label_slider_bsf")

        self.horizontalLayout_9.addWidget(self.label_slider_bsf)

        self.horizontalLayout_9.setStretch(1, 6)
        self.horizontalLayout_9.setStretch(2, 4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.horizontalLayout_19.addWidget(self.groupBox_freq)

        self.horizontalLayout_19.setStretch(0, 7)
        self.horizontalLayout_19.setStretch(1, 8)

        self.verticalLayout_9.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.grafico_fft = QVBoxLayout()
        self.grafico_fft.setObjectName(u"grafico_fft")

        self.verticalLayout_3.addLayout(self.grafico_fft)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")

        self.horizontalLayout.addWidget(self.label)

        self.progress_bar_programa = QProgressBar(self.verticalLayoutWidget_2)
        self.progress_bar_programa.setObjectName(u"progress_bar_programa")
        self.progress_bar_programa.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.progress_bar_programa.setValue(0)

        self.horizontalLayout.addWidget(self.progress_bar_programa)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 10)
        self.horizontalLayout.setStretch(3, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(0, 15)

        self.horizontalLayout_20.addLayout(self.verticalLayout_3)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_7)

        self.lcd_time_ensayo = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_time_ensayo.setObjectName(u"lcd_time_ensayo")
        self.lcd_time_ensayo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_time_ensayo.setSmallDecimalPoint(True)
        self.lcd_time_ensayo.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_11.addWidget(self.lcd_time_ensayo)

        self.horizontalLayout_11.setStretch(0, 9)
        self.horizontalLayout_11.setStretch(1, 7)

        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.progress_bar_ensayo = QProgressBar(self.verticalLayoutWidget_2)
        self.progress_bar_ensayo.setObjectName(u"progress_bar_ensayo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progress_bar_ensayo.sizePolicy().hasHeightForWidth())
        self.progress_bar_ensayo.setSizePolicy(sizePolicy2)
        self.progress_bar_ensayo.setValue(50)
        self.progress_bar_ensayo.setInvertedAppearance(False)
        self.progress_bar_ensayo.setTextDirection(QProgressBar.TopToBottom)

        self.verticalLayout_8.addWidget(self.progress_bar_ensayo)

        self.verticalLayout_8.setStretch(0, 3)
        self.verticalLayout_8.setStretch(1, 1)

        self.horizontalLayout_12.addLayout(self.verticalLayout_8)

        self.btn_forzar = QPushButton(self.verticalLayoutWidget_2)
        self.btn_forzar.setObjectName(u"btn_forzar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_forzar.sizePolicy().hasHeightForWidth())
        self.btn_forzar.setSizePolicy(sizePolicy3)
        self.btn_forzar.setFont(font1)

        self.horizontalLayout_12.addWidget(self.btn_forzar)

        self.horizontalLayout_12.setStretch(0, 6)
        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_12)

        self.groupBox_leds = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_leds.setObjectName(u"groupBox_leds")
        self.groupBox_leds.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.horizontalLayoutWidget_13 = QWidget(self.groupBox_leds)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(80, 30, 241, 87))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 0, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 5, 5, 5)
        self.led_bpfo = QLabel(self.horizontalLayoutWidget_13)
        self.led_bpfo.setObjectName(u"led_bpfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.led_bpfo.sizePolicy().hasHeightForWidth())
        self.led_bpfo.setSizePolicy(sizePolicy4)
        self.led_bpfo.setStyleSheet(u"QLabel#led_bpfo {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")
        self.led_bpfo.setScaledContents(True)
        self.led_bpfo.setMargin(0)
        self.led_bpfo.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_13.addWidget(self.led_bpfo)

        self.label_18 = QLabel(self.horizontalLayoutWidget_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"")

        self.horizontalLayout_13.addWidget(self.label_18)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 5, 5, 5)
        self.led_bpfi = QLabel(self.horizontalLayoutWidget_13)
        self.led_bpfi.setObjectName(u"led_bpfi")
        self.led_bpfi.setStyleSheet(u"QLabel#led_bpfi {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_14.addWidget(self.led_bpfi)

        self.label_20 = QLabel(self.horizontalLayoutWidget_13)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_14.addWidget(self.label_20)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_14)


        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 5, 5, 5)
        self.led_ftf = QLabel(self.horizontalLayoutWidget_13)
        self.led_ftf.setObjectName(u"led_ftf")
        self.led_ftf.setStyleSheet(u"QLabel#led_ftf{\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_17.addWidget(self.led_ftf)

        self.label_27 = QLabel(self.horizontalLayoutWidget_13)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_17.addWidget(self.label_27)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 5, 5, 5)
        self.led_bsf = QLabel(self.horizontalLayoutWidget_13)
        self.led_bsf.setObjectName(u"led_bsf")
        self.led_bsf.setStyleSheet(u"QLabel#led_bsf {\n"
"    background-color: red;\n"
"    border-radius: 10px;\n"
"    border: 2px solid darkred;\n"
"}")

        self.horizontalLayout_18.addWidget(self.led_bsf)

        self.label_29 = QLabel(self.horizontalLayoutWidget_13)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_18.addWidget(self.label_29)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 3)

        self.verticalLayout_7.addLayout(self.horizontalLayout_18)


        self.horizontalLayout_15.addLayout(self.verticalLayout_7)


        self.verticalLayout_11.addWidget(self.groupBox_leds)

        self.groupBox_meas = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_meas.setObjectName(u"groupBox_meas")
        self.groupBox_meas.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";")
        self.verticalLayoutWidget = QWidget(self.groupBox_meas)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 291, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lcd_temperatura = QLCDNumber(self.verticalLayoutWidget)
        self.lcd_temperatura.setObjectName(u"lcd_temperatura")
        self.lcd_temperatura.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_temperatura.setSmallDecimalPoint(True)
        self.lcd_temperatura.setDigitCount(5)
        self.lcd_temperatura.setMode(QLCDNumber.Dec)
        self.lcd_temperatura.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_temperatura.setProperty("value", 0.000000000000000)
        self.lcd_temperatura.setProperty("intValue", 0)

        self.horizontalLayout_2.addWidget(self.lcd_temperatura)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lcd_vibra_axial = QLCDNumber(self.verticalLayoutWidget)
        self.lcd_vibra_axial.setObjectName(u"lcd_vibra_axial")
        self.lcd_vibra_axial.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_vibra_axial.setSmallDecimalPoint(True)
        self.lcd_vibra_axial.setDigitCount(5)
        self.lcd_vibra_axial.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_3.addWidget(self.lcd_vibra_axial)

        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lcd_vibra_radial = QLCDNumber(self.verticalLayoutWidget)
        self.lcd_vibra_radial.setObjectName(u"lcd_vibra_radial")
        self.lcd_vibra_radial.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_vibra_radial.setSmallDecimalPoint(True)
        self.lcd_vibra_radial.setDigitCount(5)
        self.lcd_vibra_radial.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_4.addWidget(self.lcd_vibra_radial)

        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_11.addWidget(self.groupBox_meas)

        self.verticalLayout_11.setStretch(0, 4)
        self.verticalLayout_11.setStretch(1, 6)
        self.verticalLayout_11.setStretch(2, 7)

        self.horizontalLayout_20.addLayout(self.verticalLayout_11)

        self.horizontalLayout_20.setStretch(0, 14)
        self.horizontalLayout_20.setStretch(1, 9)

        self.verticalLayout_9.addLayout(self.horizontalLayout_20)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 6)
        self.verticalLayout_9.setStretch(2, 15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"SMR - Interfaz de personal de puesta en marcha", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.host_broker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"192.168.XXX.XXX", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"PORT:", None))
        self.port_broker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Tiempo de ensayos c/u:", None))
        self.time_ensayo.setDisplayFormat(QCoreApplication.translate("MainWindow", u"mm:ss", None))
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.notificacion.setText("")
        self.groupBox_freq.setTitle(QCoreApplication.translate("MainWindow", u"Frecuencias a detectar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"BPFO", None))
        self.label_slider_bpfo.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"BPFI", None))
        self.label_slider_bpfi.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"FTF", None))
        self.label_slider_ftf.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"BSF", None))
        self.label_slider_bsf.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Progreso:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tiempo de ensayo:", None))
        self.btn_forzar.setText(QCoreApplication.translate("MainWindow", u"Forzar", None))
        self.groupBox_leds.setTitle(QCoreApplication.translate("MainWindow", u"Fallas detectadas", None))
        self.led_bpfo.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"BPFO", None))
        self.led_bpfi.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"BPFI", None))
        self.led_ftf.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"FTF", None))
        self.led_bsf.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"BSF", None))
        self.groupBox_meas.setTitle(QCoreApplication.translate("MainWindow", u"Mediciones", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Temperatura (\u00b0C):", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vibracion axial:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Vibracion radial:", None))
    # retranslateUi

