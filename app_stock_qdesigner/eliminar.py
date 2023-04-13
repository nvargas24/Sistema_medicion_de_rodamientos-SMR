# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eliminar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        if not Eliminar.objectName():
            Eliminar.setObjectName(u"Eliminar")
        Eliminar.resize(296, 153)
        self.buttonBox = QDialogButtonBox(Eliminar)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(60, 100, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(Eliminar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 231, 31))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(9)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setFrame(True)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.titulo = QLabel(Eliminar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(30, 10, 221, 45))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.titulo.setFont(font1)
        self.titulo.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Eliminar)

        QMetaObject.connectSlotsByName(Eliminar)
    # setupUi

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(QCoreApplication.translate("Eliminar", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Eliminar", u"Producto:", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Eliminar", u"Ingrese nombre de producto", None))
        self.titulo.setText(QCoreApplication.translate("Eliminar", u"Eliminar articulo", None))
    # retranslateUi

