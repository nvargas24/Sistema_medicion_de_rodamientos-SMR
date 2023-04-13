# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app_stock.ui'
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
        MainWindow.resize(628, 383)
        MainWindow.setStyleSheet(u"QApplication::setStyle(\"fusion\");\n"
"")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_opciones = QGroupBox(self.centralwidget)
        self.menu_opciones.setObjectName(u"menu_opciones")
        self.menu_opciones.setGeometry(QRect(30, 90, 161, 241))
        self.agregar = QPushButton(self.menu_opciones)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(20, 30, 121, 41))
        self.eliminar = QPushButton(self.menu_opciones)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(20, 80, 121, 41))
        self.modificar = QPushButton(self.menu_opciones)
        self.modificar.setObjectName(u"modificar")
        self.modificar.setGeometry(QRect(20, 130, 121, 41))
        self.consultar = QPushButton(self.menu_opciones)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(20, 180, 121, 41))
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(120, 20, 441, 31))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(160, 60, 391, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.subtitulo.setFont(font1)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(210, 100, 371, 231))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_opciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
        self.agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar articulo", None))
        self.eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar articulo", None))
        self.modificar.setText(QCoreApplication.translate("MainWindow", u"Modificar articulo", None))
        self.consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar Stock", None))
        self.titulo.setText(QCoreApplication.translate("MainWindow", u"Electronica del oeste", None))
        self.subtitulo.setText(QCoreApplication.translate("MainWindow", u"Bienvenido, seleccione la opcion a realizar", None))
    # retranslateUi

