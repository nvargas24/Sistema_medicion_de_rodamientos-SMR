# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'agregar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Agregar(object):
    def setupUi(self, Agregar):
        if not Agregar.objectName():
            Agregar.setObjectName(u"Agregar")
        Agregar.resize(292, 232)
        self.buttonBox = QDialogButtonBox(Agregar)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 180, 171, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.titulo = QLabel(Agregar)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(30, 10, 221, 45))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(Qt.AlignCenter)
        self.widget = QWidget(Agregar)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 231, 111))
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.widget)
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

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_3.setMaxLength(32767)
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setDragEnabled(False)
        self.lineEdit_3.setReadOnly(False)
        self.lineEdit_3.setClearButtonEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_4 = QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setTabletTracking(False)
        self.lineEdit_4.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_4.setMaxLength(32767)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_4)


        self.retranslateUi(Agregar)
        self.buttonBox.accepted.connect(Agregar.accept)
        self.buttonBox.rejected.connect(Agregar.reject)

        QMetaObject.connectSlotsByName(Agregar)
    # setupUi

    def retranslateUi(self, Agregar):
        Agregar.setWindowTitle(QCoreApplication.translate("Agregar", u"Dialog", None))
        self.titulo.setText(QCoreApplication.translate("Agregar", u"Nuevo articulo", None))
        self.label.setText(QCoreApplication.translate("Agregar", u"Producto:", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese nombre de producto", None))
        self.label_2.setText(QCoreApplication.translate("Agregar", u"Cantidad:", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese valor numerico", None))
        self.label_3.setText(QCoreApplication.translate("Agregar", u"Precio:", None))
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese valor numerico", None))
        self.label_4.setText(QCoreApplication.translate("Agregar", u"Descripcion:", None))
        self.lineEdit_4.setInputMask("")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Agregar", u"Ingrese una breve descripcion", None))
    # retranslateUi

