# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2_opengl.ui'
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
        MainWindow.resize(623, 371)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 30, 571, 301))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.sbox_ang_x = QSpinBox(self.horizontalLayoutWidget)
        self.sbox_ang_x.setObjectName(u"sbox_ang_x")
        self.sbox_ang_x.setWrapping(True)
        self.sbox_ang_x.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_ang_x.setMaximum(360)

        self.horizontalLayout_2.addWidget(self.sbox_ang_x)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.sbox_ang_y = QSpinBox(self.horizontalLayoutWidget)
        self.sbox_ang_y.setObjectName(u"sbox_ang_y")
        self.sbox_ang_y.setWrapping(True)
        self.sbox_ang_y.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_ang_y.setMaximum(360)

        self.horizontalLayout_3.addWidget(self.sbox_ang_y)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.sbox_ang_z = QSpinBox(self.horizontalLayoutWidget)
        self.sbox_ang_z.setObjectName(u"sbox_ang_z")
        self.sbox_ang_z.setWrapping(True)
        self.sbox_ang_z.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_ang_z.setMaximum(360)

        self.horizontalLayout_4.addWidget(self.sbox_ang_z)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layout_opengl = QHBoxLayout()
        self.layout_opengl.setObjectName(u"layout_opengl")

        self.horizontalLayout.addLayout(self.layout_opengl)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"angX", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"angY", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"angZ", None))
    # retranslateUi

