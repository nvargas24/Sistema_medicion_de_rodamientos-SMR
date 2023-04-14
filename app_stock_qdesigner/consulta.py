# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'consulta.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Consulta(object):
    def setupUi(self, Consulta):
        if not Consulta.objectName():
            Consulta.setObjectName(u"Consulta")
        Consulta.resize(556, 346)
        Consulta.setToolTipDuration(0)
        Consulta.setStyleSheet(u"QApplication::setStyle(\"fusion\");\n"
"")
        self.catalogo_list = QTableWidget(Consulta)
        if (self.catalogo_list.columnCount() < 5):
            self.catalogo_list.setColumnCount(5)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
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
        self.catalogo_list.setGeometry(QRect(20, 50, 511, 231))
        self.btn_cat_full = QPushButton(Consulta)
        self.btn_cat_full.setObjectName(u"btn_cat_full")
        self.btn_cat_full.setGeometry(QRect(150, 290, 121, 31))
        self.btn_volver = QPushButton(Consulta)
        self.btn_volver.setObjectName(u"btn_volver")
        self.btn_volver.setGeometry(QRect(280, 290, 121, 31))
        self.widget = QWidget(Consulta)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(29, 20, 491, 25))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_nombre = QLabel(self.widget)
        self.label_nombre.setObjectName(u"label_nombre")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_nombre.setFont(font1)

        self.horizontalLayout.addWidget(self.label_nombre)

        self.in_nombre = QLineEdit(self.widget)
        self.in_nombre.setObjectName(u"in_nombre")
        self.in_nombre.setTabletTracking(False)
        self.in_nombre.setFocusPolicy(Qt.StrongFocus)
        self.in_nombre.setAutoFillBackground(False)
        self.in_nombre.setInputMethodHints(Qt.ImhNone)
        self.in_nombre.setMaxLength(32767)
        self.in_nombre.setFrame(True)
        self.in_nombre.setDragEnabled(False)
        self.in_nombre.setReadOnly(False)
        self.in_nombre.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.in_nombre)

        self.label_precio = QLabel(self.widget)
        self.label_precio.setObjectName(u"label_precio")
        self.label_precio.setFont(font1)

        self.horizontalLayout.addWidget(self.label_precio)

        self.in_precio = QLineEdit(self.widget)
        self.in_precio.setObjectName(u"in_precio")
        self.in_precio.setTabletTracking(False)
        self.in_precio.setFocusPolicy(Qt.StrongFocus)
        self.in_precio.setAutoFillBackground(False)
        self.in_precio.setInputMethodHints(Qt.ImhNone)
        self.in_precio.setMaxLength(32767)
        self.in_precio.setFrame(True)
        self.in_precio.setDragEnabled(False)
        self.in_precio.setReadOnly(False)
        self.in_precio.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.in_precio)

        self.btn_buscar = QPushButton(self.widget)
        self.btn_buscar.setObjectName(u"btn_buscar")

        self.horizontalLayout.addWidget(self.btn_buscar)


        self.retranslateUi(Consulta)

        QMetaObject.connectSlotsByName(Consulta)
    # setupUi

    def retranslateUi(self, Consulta):
        Consulta.setWindowTitle(QCoreApplication.translate("Consulta", u"Form", None))
        ___qtablewidgetitem = self.catalogo_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Consulta", u"ID", None));
        ___qtablewidgetitem1 = self.catalogo_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Consulta", u"Producto", None));
        ___qtablewidgetitem2 = self.catalogo_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Consulta", u"Cantidad", None));
        ___qtablewidgetitem3 = self.catalogo_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Consulta", u"Precio", None));
        ___qtablewidgetitem4 = self.catalogo_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Consulta", u"Descripcion", None));
        self.btn_cat_full.setText(QCoreApplication.translate("Consulta", u"Catalogo completo", None))
        self.btn_volver.setText(QCoreApplication.translate("Consulta", u"Volver", None))
        self.label_nombre.setText(QCoreApplication.translate("Consulta", u"Producto:", None))
        self.in_nombre.setInputMask("")
        self.in_nombre.setText("")
        self.in_nombre.setPlaceholderText(QCoreApplication.translate("Consulta", u"Ingrese nombre de producto", None))
        self.label_precio.setText(QCoreApplication.translate("Consulta", u"Precio:", None))
        self.in_precio.setInputMask("")
        self.in_precio.setText("")
        self.in_precio.setPlaceholderText(QCoreApplication.translate("Consulta", u"Ingrese precio en pesos", None))
        self.btn_buscar.setText(QCoreApplication.translate("Consulta", u"Buscar", None))
    # retranslateUi

