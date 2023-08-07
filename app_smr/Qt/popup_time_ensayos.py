# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_time_ensayos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TimeEnsayosWindow(object):
    def setupUi(self, TimeEnsayosWindow):
        if not TimeEnsayosWindow.objectName():
            TimeEnsayosWindow.setObjectName(u"TimeEnsayosWindow")
        TimeEnsayosWindow.resize(404, 368)
        self.verticalLayoutWidget = QWidget(TimeEnsayosWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 341, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(70, -1, 70, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_4)

        self.label_time_ensayo1 = QLabel(self.verticalLayoutWidget)
        self.label_time_ensayo1.setObjectName(u"label_time_ensayo1")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_time_ensayo1.setFont(font2)
        self.label_time_ensayo1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_time_ensayo1)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_11)

        self.label_time_ensayo2 = QLabel(self.verticalLayoutWidget)
        self.label_time_ensayo2.setObjectName(u"label_time_ensayo2")
        self.label_time_ensayo2.setFont(font2)
        self.label_time_ensayo2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.label_time_ensayo2)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_21.addWidget(self.label_9)

        self.label_time_ensayo3 = QLabel(self.verticalLayoutWidget)
        self.label_time_ensayo3.setObjectName(u"label_time_ensayo3")
        self.label_time_ensayo3.setFont(font2)
        self.label_time_ensayo3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_time_ensayo3)

        self.horizontalLayout_21.setStretch(0, 1)
        self.horizontalLayout_21.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_6)

        self.label_time_ensayo4 = QLabel(self.verticalLayoutWidget)
        self.label_time_ensayo4.setObjectName(u"label_time_ensayo4")
        self.label_time_ensayo4.setFont(font2)
        self.label_time_ensayo4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.label_time_ensayo4)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_23.addWidget(self.label_8)

        self.label_time_ensayo5 = QLabel(self.verticalLayoutWidget)
        self.label_time_ensayo5.setObjectName(u"label_time_ensayo5")
        self.label_time_ensayo5.setFont(font2)

        self.horizontalLayout_23.addWidget(self.label_time_ensayo5)

        self.horizontalLayout_23.setStretch(0, 1)
        self.horizontalLayout_23.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_23)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(100, -1, 100, -1)
        self.btn_ingresar = QPushButton(self.verticalLayoutWidget)
        self.btn_ingresar.setObjectName(u"btn_ingresar")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ingresar.sizePolicy().hasHeightForWidth())
        self.btn_ingresar.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_ingresar.setFont(font3)
        self.btn_ingresar.setFocusPolicy(Qt.NoFocus)
        self.btn_ingresar.setStyleSheet(u"QPushButton {\n"
"    background-color: #F2F2F2; /* Color de fondo */\n"
"    border: 2px solid #D9D9D9; /* Borde gris claro */\n"
"    border-radius: 15px; /* Bordes curvos */\n"
"    padding: 5px 10px; /* Espacio interno para texto */\n"
"    font-weight: bold; /* Texto en negrita */\n"
"    font-size: 14px; /* Tama\u00f1o de fuente */\n"
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

        self.horizontalLayout.addWidget(self.btn_ingresar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(1, 4)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 4)

        self.retranslateUi(TimeEnsayosWindow)

        QMetaObject.connectSlotsByName(TimeEnsayosWindow)
    # setupUi

    def retranslateUi(self, TimeEnsayosWindow):
        TimeEnsayosWindow.setWindowTitle(QCoreApplication.translate("TimeEnsayosWindow", u"Dialog", None))
        self.label_7.setText(QCoreApplication.translate("TimeEnsayosWindow", u"Tiempos de ensayos", None))
        self.label_4.setText(QCoreApplication.translate("TimeEnsayosWindow", u"Ensayo 1:", None))
        self.label_time_ensayo1.setText("")
        self.label_11.setText(QCoreApplication.translate("TimeEnsayosWindow", u"Ensayo 2:", None))
        self.label_time_ensayo2.setText("")
        self.label_9.setText(QCoreApplication.translate("TimeEnsayosWindow", u"Ensayo 3:", None))
        self.label_time_ensayo3.setText("")
        self.label_6.setText(QCoreApplication.translate("TimeEnsayosWindow", u"Ensayo 4:", None))
        self.label_time_ensayo4.setText("")
        self.label_8.setText(QCoreApplication.translate("TimeEnsayosWindow", u"Ensayo 5:", None))
        self.label_time_ensayo5.setText("")
        self.btn_ingresar.setText(QCoreApplication.translate("TimeEnsayosWindow", u"OK", None))
    # retranslateUi

