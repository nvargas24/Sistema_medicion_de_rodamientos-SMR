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
        MainWindow.resize(750, 368)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_opciones = QGroupBox(self.centralwidget)
        self.menu_opciones.setObjectName(u"menu_opciones")
        self.menu_opciones.setGeometry(QRect(20, 90, 161, 231))
        self.agregar = QPushButton(self.menu_opciones)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(20, 20, 121, 41))
        self.eliminar = QPushButton(self.menu_opciones)
        self.eliminar.setObjectName(u"eliminar")
        self.eliminar.setGeometry(QRect(20, 70, 121, 41))
        self.modificar = QPushButton(self.menu_opciones)
        self.modificar.setObjectName(u"modificar")
        self.modificar.setGeometry(QRect(20, 120, 121, 41))
        self.consultar = QPushButton(self.menu_opciones)
        self.consultar.setObjectName(u"consultar")
        self.consultar.setGeometry(QRect(20, 170, 121, 41))
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(190, 20, 441, 31))
        font = QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.subtitulo = QLabel(self.centralwidget)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(230, 60, 391, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.subtitulo.setFont(font1)
        self.catalogo_list = QTableWidget(self.centralwidget)
        if (self.catalogo_list.columnCount() < 5):
            self.catalogo_list.setColumnCount(5)
        font2 = QFont()
        font2.setBold(False)
        font2.setWeight(50)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.catalogo_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.catalogo_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.catalogo_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.catalogo_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.catalogo_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.catalogo_list.setObjectName(u"catalogo_list")
        self.catalogo_list.setGeometry(QRect(190, 100, 511, 221))
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
        ___qtablewidgetitem = self.catalogo_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.catalogo_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.catalogo_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem3 = self.catalogo_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Precio", None));
        ___qtablewidgetitem4 = self.catalogo_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
    # retranslateUi

