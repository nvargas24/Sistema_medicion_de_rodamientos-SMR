# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        MainWindow.resize(1105, 777)
        MainWindow.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(30, 30, 1041, 711))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btn_init = QPushButton(self.horizontalLayoutWidget_3)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy)
        self.btn_init.setFocusPolicy(Qt.NoFocus)
        self.btn_init.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_13.addWidget(self.btn_init)

        self.btn_finish = QPushButton(self.horizontalLayoutWidget_3)
        self.btn_finish.setObjectName(u"btn_finish")
        sizePolicy.setHeightForWidth(self.btn_finish.sizePolicy().hasHeightForWidth())
        self.btn_finish.setSizePolicy(sizePolicy)
        self.btn_finish.setFocusPolicy(Qt.NoFocus)
        self.btn_finish.setStyleSheet(u"QPushButton {\n"
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
"}\n"
"\n"
"/* Estilos para QPushButton en estado deshabilitado */\n"
"QPushButton:disabled {\n"
"    background-color: #F2F2F2;\n"
"    border-color: #D9D9D9;\n"
""
                        "    color: #B0B0B0; /* Cambia el color de texto a gris claro */\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_finish)

        self.horizontalLayout_13.setStretch(0, 2)
        self.horizontalLayout_13.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_13)

        self.label_notificacion = QLabel(self.horizontalLayoutWidget_3)
        self.label_notificacion.setObjectName(u"label_notificacion")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_notificacion.setFont(font)
        self.label_notificacion.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_notificacion)

        self.graph = QVBoxLayout()
        self.graph.setObjectName(u"graph")

        self.verticalLayout.addLayout(self.graph)

        self.graph2 = QVBoxLayout()
        self.graph2.setObjectName(u"graph2")

        self.verticalLayout.addLayout(self.graph2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_set_zero = QPushButton(self.horizontalLayoutWidget_3)
        self.btn_set_zero.setObjectName(u"btn_set_zero")
        sizePolicy.setHeightForWidth(self.btn_set_zero.sizePolicy().hasHeightForWidth())
        self.btn_set_zero.setSizePolicy(sizePolicy)
        self.btn_set_zero.setFocusPolicy(Qt.NoFocus)
        self.btn_set_zero.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_set_zero)

        self.btn_configurar = QPushButton(self.horizontalLayoutWidget_3)
        self.btn_configurar.setObjectName(u"btn_configurar")
        sizePolicy.setHeightForWidth(self.btn_configurar.sizePolicy().hasHeightForWidth())
        self.btn_configurar.setSizePolicy(sizePolicy)
        self.btn_configurar.setFocusPolicy(Qt.NoFocus)
        self.btn_configurar.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.btn_configurar)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 10)
        self.verticalLayout.setStretch(3, 6)
        self.verticalLayout.setStretch(4, 2)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line = QFrame(self.horizontalLayoutWidget_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_7 = QLabel(self.horizontalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Historic")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_7)

        self.lcd_time_ensayo = QLCDNumber(self.horizontalLayoutWidget_3)
        self.lcd_time_ensayo.setObjectName(u"lcd_time_ensayo")
        self.lcd_time_ensayo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lcd_time_ensayo.setSmallDecimalPoint(True)
        self.lcd_time_ensayo.setDigitCount(8)
        self.lcd_time_ensayo.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_11.addWidget(self.lcd_time_ensayo)

        self.horizontalLayout_11.setStretch(0, 4)
        self.horizontalLayout_11.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_11)

        self.table_data = QTableWidget(self.horizontalLayoutWidget_3)
        if (self.table_data.columnCount() < 4):
            self.table_data.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.table_data.rowCount() < 100):
            self.table_data.setRowCount(100)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setAutoScrollMargin(15)
        self.table_data.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_data.setShowGrid(True)
        self.table_data.setGridStyle(Qt.CustomDashLine)
        self.table_data.setSortingEnabled(True)
        self.table_data.setWordWrap(True)
        self.table_data.setRowCount(100)

        self.verticalLayout_2.addWidget(self.table_data)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 10)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(2, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar \n"
"ensayo", None))
        self.btn_finish.setText(QCoreApplication.translate("MainWindow", u"Finalizar \n"
"ensayo", None))
        self.label_notificacion.setText(QCoreApplication.translate("MainWindow", u"NOTIFICACION", None))
        self.btn_set_zero.setText(QCoreApplication.translate("MainWindow", u"SET ZERO", None))
        self.btn_configurar.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tiempo de ensayo:", None))
        ___qtablewidgetitem = self.table_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem1 = self.table_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem2 = self.table_data.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"y", None));
        ___qtablewidgetitem3 = self.table_data.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"z", None));
    # retranslateUi

