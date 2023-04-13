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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(552, 343)
        Form.setToolTipDuration(0)
        Form.setStyleSheet(u"QApplication::setStyle(\"fusion\");\n"
"")
        self.catalogo_list = QTableWidget(Form)
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
        self.agregar = QPushButton(Form)
        self.agregar.setObjectName(u"agregar")
        self.agregar.setGeometry(QRect(130, 290, 131, 41))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 20, 151, 20))
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(True)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 16, 61, 20))
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 20, 41, 16))
        self.label_2.setFont(font1)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(290, 20, 151, 20))
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.agregar_2 = QPushButton(Form)
        self.agregar_2.setObjectName(u"agregar_2")
        self.agregar_2.setGeometry(QRect(270, 290, 121, 41))
        self.agregar_3 = QPushButton(Form)
        self.agregar_3.setObjectName(u"agregar_3")
        self.agregar_3.setGeometry(QRect(460, 20, 61, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.catalogo_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.catalogo_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Producto", None));
        ___qtablewidgetitem2 = self.catalogo_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Cantidad", None));
        ___qtablewidgetitem3 = self.catalogo_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Precio", None));
        ___qtablewidgetitem4 = self.catalogo_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Descripcion", None));
        self.agregar.setText(QCoreApplication.translate("Form", u"Ver catatologo completo", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Ingrese nombre de producto", None))
        self.label.setText(QCoreApplication.translate("Form", u"Producto", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Precio", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Ingrese precio en pesos", None))
        self.agregar_2.setText(QCoreApplication.translate("Form", u"Volver", None))
        self.agregar_3.setText(QCoreApplication.translate("Form", u"Buscar", None))
    # retranslateUi

