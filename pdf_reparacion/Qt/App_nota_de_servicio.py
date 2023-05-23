# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App_nota_de_servicio.ui'
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
        MainWindow.resize(843, 553)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 401, 261))
        self.nota_servicio = QVBoxLayout(self.verticalLayoutWidget_2)
        self.nota_servicio.setSpacing(10)
        self.nota_servicio.setObjectName(u"nota_servicio")
        self.nota_servicio.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.nota_servicio.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 20, 351, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_tipo_servicio = QLabel(self.verticalLayoutWidget)
        self.label_tipo_servicio.setObjectName(u"label_tipo_servicio")

        self.horizontalLayout_2.addWidget(self.label_tipo_servicio)

        self.tipo_servicio = QComboBox(self.verticalLayoutWidget)
        self.tipo_servicio.addItem("")
        self.tipo_servicio.addItem("")
        self.tipo_servicio.addItem("")
        self.tipo_servicio.setObjectName(u"tipo_servicio")

        self.horizontalLayout_2.addWidget(self.tipo_servicio)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_nom_sector = QLabel(self.verticalLayoutWidget)
        self.label_nom_sector.setObjectName(u"label_nom_sector")

        self.horizontalLayout_3.addWidget(self.label_nom_sector)

        self.nom_sector = QComboBox(self.verticalLayoutWidget)
        self.nom_sector.addItem("")
        self.nom_sector.addItem("")
        self.nom_sector.addItem("")
        self.nom_sector.addItem("")
        self.nom_sector.addItem("")
        self.nom_sector.addItem("")
        self.nom_sector.setObjectName(u"nom_sector")

        self.horizontalLayout_3.addWidget(self.nom_sector)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_nota_servicio = QLabel(self.verticalLayoutWidget)
        self.label_nota_servicio.setObjectName(u"label_nota_servicio")

        self.horizontalLayout.addWidget(self.label_nota_servicio)

        self.label_servicio = QLabel(self.verticalLayoutWidget)
        self.label_servicio.setObjectName(u"label_servicio")

        self.horizontalLayout.addWidget(self.label_servicio)

        self.label_sector = QLabel(self.verticalLayoutWidget)
        self.label_sector.setObjectName(u"label_sector")

        self.horizontalLayout.addWidget(self.label_sector)

        self.num_reparacion = QLineEdit(self.verticalLayoutWidget)
        self.num_reparacion.setObjectName(u"num_reparacion")

        self.horizontalLayout.addWidget(self.num_reparacion)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.nota_servicio.addWidget(self.groupBox_4)

        self.groupBox = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_5 = QWidget(self.groupBox)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 20, 381, 52))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_nom_solicitante = QLabel(self.verticalLayoutWidget_5)
        self.label_nom_solicitante.setObjectName(u"label_nom_solicitante")

        self.horizontalLayout_4.addWidget(self.label_nom_solicitante)

        self.nom_solicitante = QLineEdit(self.verticalLayoutWidget_5)
        self.nom_solicitante.setObjectName(u"nom_solicitante")

        self.horizontalLayout_4.addWidget(self.nom_solicitante)

        self.label_sector_solicitante = QLabel(self.verticalLayoutWidget_5)
        self.label_sector_solicitante.setObjectName(u"label_sector_solicitante")

        self.horizontalLayout_4.addWidget(self.label_sector_solicitante)

        self.sector_solicitante = QLineEdit(self.verticalLayoutWidget_5)
        self.sector_solicitante.setObjectName(u"sector_solicitante")

        self.horizontalLayout_4.addWidget(self.sector_solicitante)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_ref_ot = QLabel(self.verticalLayoutWidget_5)
        self.label_ref_ot.setObjectName(u"label_ref_ot")

        self.horizontalLayout_6.addWidget(self.label_ref_ot)

        self.ref_ot = QLineEdit(self.verticalLayoutWidget_5)
        self.ref_ot.setObjectName(u"ref_ot")

        self.horizontalLayout_6.addWidget(self.ref_ot)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.nota_servicio.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(10, 20, 381, 31))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_num_formacion = QLabel(self.horizontalLayoutWidget_7)
        self.label_num_formacion.setObjectName(u"label_num_formacion")

        self.horizontalLayout_7.addWidget(self.label_num_formacion)

        self.num_formacion = QComboBox(self.horizontalLayoutWidget_7)
        self.num_formacion.addItem("")
        self.num_formacion.addItem("")
        self.num_formacion.setObjectName(u"num_formacion")

        self.horizontalLayout_7.addWidget(self.num_formacion)

        self.label_num_coche = QLabel(self.horizontalLayoutWidget_7)
        self.label_num_coche.setObjectName(u"label_num_coche")

        self.horizontalLayout_7.addWidget(self.label_num_coche)

        self.num_coche = QComboBox(self.horizontalLayoutWidget_7)
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.addItem("")
        self.num_coche.setObjectName(u"num_coche")

        self.horizontalLayout_7.addWidget(self.num_coche)

        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 8)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 8)

        self.nota_servicio.addWidget(self.groupBox_2)

        self.nota_servicio.setStretch(0, 4)
        self.nota_servicio.setStretch(1, 3)
        self.nota_servicio.setStretch(2, 2)
        self.verticalLayoutWidget_9 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(420, 10, 411, 391))
        self.detalles_reparacion = QVBoxLayout(self.verticalLayoutWidget_9)
        self.detalles_reparacion.setSpacing(10)
        self.detalles_reparacion.setObjectName(u"detalles_reparacion")
        self.detalles_reparacion.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_9)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 382, 131))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_nom_modulo = QLabel(self.verticalLayoutWidget_4)
        self.label_nom_modulo.setObjectName(u"label_nom_modulo")

        self.horizontalLayout_8.addWidget(self.label_nom_modulo)

        self.nom_modulo = QComboBox(self.verticalLayoutWidget_4)
        self.nom_modulo.addItem("")
        self.nom_modulo.addItem("")
        self.nom_modulo.addItem("")
        self.nom_modulo.setObjectName(u"nom_modulo")

        self.horizontalLayout_8.addWidget(self.nom_modulo)

        self.label_nom_sistema = QLabel(self.verticalLayoutWidget_4)
        self.label_nom_sistema.setObjectName(u"label_nom_sistema")

        self.horizontalLayout_8.addWidget(self.label_nom_sistema)

        self.nom_sistema = QComboBox(self.verticalLayoutWidget_4)
        self.nom_sistema.addItem("")
        self.nom_sistema.addItem("")
        self.nom_sistema.setObjectName(u"nom_sistema")

        self.horizontalLayout_8.addWidget(self.nom_sistema)

        self.label_num_serie = QLabel(self.verticalLayoutWidget_4)
        self.label_num_serie.setObjectName(u"label_num_serie")

        self.horizontalLayout_8.addWidget(self.label_num_serie)

        self.num_serie = QLineEdit(self.verticalLayoutWidget_4)
        self.num_serie.setObjectName(u"num_serie")

        self.horizontalLayout_8.addWidget(self.num_serie)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.check_primer_ingreso = QCheckBox(self.verticalLayoutWidget_4)
        self.check_primer_ingreso.setObjectName(u"check_primer_ingreso")

        self.horizontalLayout_9.addWidget(self.check_primer_ingreso)

        self.label_num_servicio_ant = QLabel(self.verticalLayoutWidget_4)
        self.label_num_servicio_ant.setObjectName(u"label_num_servicio_ant")

        self.horizontalLayout_9.addWidget(self.label_num_servicio_ant)

        self.label_tipo_servicio_ant = QLabel(self.verticalLayoutWidget_4)
        self.label_tipo_servicio_ant.setObjectName(u"label_tipo_servicio_ant")

        self.horizontalLayout_9.addWidget(self.label_tipo_servicio_ant)

        self.label_num_recibe_ant = QLabel(self.verticalLayoutWidget_4)
        self.label_num_recibe_ant.setObjectName(u"label_num_recibe_ant")

        self.horizontalLayout_9.addWidget(self.label_num_recibe_ant)

        self.num_servicio_ant = QLineEdit(self.verticalLayoutWidget_4)
        self.num_servicio_ant.setObjectName(u"num_servicio_ant")

        self.horizontalLayout_9.addWidget(self.num_servicio_ant)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_obs = QLabel(self.verticalLayoutWidget_4)
        self.label_obs.setObjectName(u"label_obs")

        self.horizontalLayout_12.addWidget(self.label_obs)

        self.btn_tool_obs = QToolButton(self.verticalLayoutWidget_4)
        self.btn_tool_obs.setObjectName(u"btn_tool_obs")

        self.horizontalLayout_12.addWidget(self.btn_tool_obs)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)

        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.observaciones = QLineEdit(self.verticalLayoutWidget_4)
        self.observaciones.setObjectName(u"observaciones")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.observaciones.sizePolicy().hasHeightForWidth())
        self.observaciones.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.observaciones)

        self.verticalLayout_3.setStretch(1, 2)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.setStretch(2, 1)

        self.detalles_reparacion.addWidget(self.groupBox_3)

        self.groupBox_5 = QGroupBox(self.verticalLayoutWidget_9)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy1.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy1)
        self.verticalLayoutWidget_6 = QWidget(self.groupBox_5)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 20, 381, 191))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_nom_operario_int_en = QLabel(self.verticalLayoutWidget_6)
        self.label_nom_operario_int_en.setObjectName(u"label_nom_operario_int_en")

        self.horizontalLayout_5.addWidget(self.label_nom_operario_int_en)

        self.nom_operario_int_en = QLineEdit(self.verticalLayoutWidget_6)
        self.nom_operario_int_en.setObjectName(u"nom_operario_int_en")

        self.horizontalLayout_5.addWidget(self.nom_operario_int_en)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_detalle_rep = QLabel(self.verticalLayoutWidget_6)
        self.label_detalle_rep.setObjectName(u"label_detalle_rep")

        self.verticalLayout_13.addWidget(self.label_detalle_rep)

        self.detalle_rep = QLineEdit(self.verticalLayoutWidget_6)
        self.detalle_rep.setObjectName(u"detalle_rep")
        sizePolicy2.setHeightForWidth(self.detalle_rep.sizePolicy().hasHeightForWidth())
        self.detalle_rep.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.detalle_rep)


        self.verticalLayout_6.addLayout(self.verticalLayout_13)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_mat_utilizados = QLabel(self.verticalLayoutWidget_6)
        self.label_mat_utilizados.setObjectName(u"label_mat_utilizados")

        self.horizontalLayout_16.addWidget(self.label_mat_utilizados)

        self.btn_tool_mat_utilizados = QToolButton(self.verticalLayoutWidget_6)
        self.btn_tool_mat_utilizados.setObjectName(u"btn_tool_mat_utilizados")

        self.horizontalLayout_16.addWidget(self.btn_tool_mat_utilizados)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_16.setStretch(2, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.detalle_mat_utilizados = QLineEdit(self.verticalLayoutWidget_6)
        self.detalle_mat_utilizados.setObjectName(u"detalle_mat_utilizados")
        sizePolicy2.setHeightForWidth(self.detalle_mat_utilizados.sizePolicy().hasHeightForWidth())
        self.detalle_mat_utilizados.setSizePolicy(sizePolicy2)

        self.verticalLayout_7.addWidget(self.detalle_mat_utilizados)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_6.setStretch(1, 5)
        self.verticalLayout_6.setStretch(2, 6)

        self.detalles_reparacion.addWidget(self.groupBox_5)

        self.detalles_reparacion.setStretch(0, 6)
        self.detalles_reparacion.setStretch(1, 8)
        self.verticalLayoutWidget_10 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 290, 401, 111))
        self.verificacion = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verificacion.setSpacing(10)
        self.verificacion.setObjectName(u"verificacion")
        self.verificacion.setContentsMargins(0, 0, 0, 0)
        self.frame_verificacion = QGroupBox(self.verticalLayoutWidget_10)
        self.frame_verificacion.setObjectName(u"frame_verificacion")
        self.verticalLayoutWidget_11 = QWidget(self.frame_verificacion)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(10, 20, 381, 80))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_verificacion = QLabel(self.verticalLayoutWidget_11)
        self.label_verificacion.setObjectName(u"label_verificacion")
        self.label_verificacion.setMaximumSize(QSize(500, 16777215))
        self.label_verificacion.setScaledContents(False)
        self.label_verificacion.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_verificacion)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.con_especificiacion = QRadioButton(self.verticalLayoutWidget_11)
        self.con_especificiacion.setObjectName(u"con_especificiacion")

        self.horizontalLayout_11.addWidget(self.con_especificiacion)

        self.codigos = QLineEdit(self.verticalLayoutWidget_11)
        self.codigos.setObjectName(u"codigos")

        self.horizontalLayout_11.addWidget(self.codigos)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.sin_especificacion = QRadioButton(self.verticalLayoutWidget_11)
        self.sin_especificacion.setObjectName(u"sin_especificacion")

        self.horizontalLayout_10.addWidget(self.sin_especificacion)

        self.testing = QLineEdit(self.verticalLayoutWidget_11)
        self.testing.setObjectName(u"testing")

        self.horizontalLayout_10.addWidget(self.testing)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)


        self.verificacion.addWidget(self.frame_verificacion)

        self.verticalLayoutWidget_12 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(20, 420, 291, 101))
        self.datos_operario = QVBoxLayout(self.verticalLayoutWidget_12)
        self.datos_operario.setObjectName(u"datos_operario")
        self.datos_operario.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_nom_recibio = QLabel(self.verticalLayoutWidget_12)
        self.label_nom_recibio.setObjectName(u"label_nom_recibio")

        self.horizontalLayout_13.addWidget(self.label_nom_recibio)

        self.nom_recibio = QComboBox(self.verticalLayoutWidget_12)
        self.nom_recibio.addItem("")
        self.nom_recibio.addItem("")
        self.nom_recibio.addItem("")
        self.nom_recibio.addItem("")
        self.nom_recibio.addItem("")
        self.nom_recibio.setObjectName(u"nom_recibio")

        self.horizontalLayout_13.addWidget(self.nom_recibio)

        self.label_fecha_recibio = QLabel(self.verticalLayoutWidget_12)
        self.label_fecha_recibio.setObjectName(u"label_fecha_recibio")

        self.horizontalLayout_13.addWidget(self.label_fecha_recibio)

        self.fecha_recibio = QDateEdit(self.verticalLayoutWidget_12)
        self.fecha_recibio.setObjectName(u"fecha_recibio")
        self.fecha_recibio.setWrapping(False)
        self.fecha_recibio.setProperty("showGroupSeparator", False)
        self.fecha_recibio.setCalendarPopup(True)
        self.fecha_recibio.setCurrentSectionIndex(0)
        self.fecha_recibio.setTimeSpec(Qt.LocalTime)
        self.fecha_recibio.setDate(QDate(2023, 5, 10))

        self.horizontalLayout_13.addWidget(self.fecha_recibio)


        self.datos_operario.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_nom_realizo = QLabel(self.verticalLayoutWidget_12)
        self.label_nom_realizo.setObjectName(u"label_nom_realizo")

        self.horizontalLayout_14.addWidget(self.label_nom_realizo)

        self.nom_realizo = QComboBox(self.verticalLayoutWidget_12)
        self.nom_realizo.addItem("")
        self.nom_realizo.addItem("")
        self.nom_realizo.addItem("")
        self.nom_realizo.addItem("")
        self.nom_realizo.addItem("")
        self.nom_realizo.setObjectName(u"nom_realizo")

        self.horizontalLayout_14.addWidget(self.nom_realizo)

        self.label_fecha_realizo = QLabel(self.verticalLayoutWidget_12)
        self.label_fecha_realizo.setObjectName(u"label_fecha_realizo")

        self.horizontalLayout_14.addWidget(self.label_fecha_realizo)

        self.fehca_realizo = QDateEdit(self.verticalLayoutWidget_12)
        self.fehca_realizo.setObjectName(u"fehca_realizo")
        self.fehca_realizo.setCalendarPopup(True)
        self.fehca_realizo.setDate(QDate(2023, 5, 10))

        self.horizontalLayout_14.addWidget(self.fehca_realizo)


        self.datos_operario.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_nom_verifico = QLabel(self.verticalLayoutWidget_12)
        self.label_nom_verifico.setObjectName(u"label_nom_verifico")

        self.horizontalLayout_15.addWidget(self.label_nom_verifico)

        self.nom_verifico = QComboBox(self.verticalLayoutWidget_12)
        self.nom_verifico.addItem("")
        self.nom_verifico.addItem("")
        self.nom_verifico.addItem("")
        self.nom_verifico.addItem("")
        self.nom_verifico.addItem("")
        self.nom_verifico.setObjectName(u"nom_verifico")

        self.horizontalLayout_15.addWidget(self.nom_verifico)

        self.label_fecha_verifico = QLabel(self.verticalLayoutWidget_12)
        self.label_fecha_verifico.setObjectName(u"label_fecha_verifico")

        self.horizontalLayout_15.addWidget(self.label_fecha_verifico)

        self.fecha_verifico = QDateEdit(self.verticalLayoutWidget_12)
        self.fecha_verifico.setObjectName(u"fecha_verifico")
        self.fecha_verifico.setCurrentSection(QDateTimeEdit.DaySection)
        self.fecha_verifico.setCalendarPopup(True)
        self.fecha_verifico.setDate(QDate(2023, 5, 10))

        self.horizontalLayout_15.addWidget(self.fecha_verifico)


        self.datos_operario.addLayout(self.horizontalLayout_15)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(560, 420, 131, 101))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.guardar_pdf = QPushButton(self.verticalLayoutWidget_3)
        self.guardar_pdf.setObjectName(u"guardar_pdf")

        self.verticalLayout_2.addWidget(self.guardar_pdf)

        self.imprimir = QPushButton(self.verticalLayoutWidget_3)
        self.imprimir.setObjectName(u"imprimir")

        self.verticalLayout_2.addWidget(self.imprimir)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_2.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Nota de servicio", None))
        self.label_tipo_servicio.setText(QCoreApplication.translate("MainWindow", u"Tipo de servicio:", None))
        self.tipo_servicio.setItemText(0, QCoreApplication.translate("MainWindow", u"Intervenciones realizadas sobre formaci\u00f3n", None))
        self.tipo_servicio.setItemText(1, QCoreApplication.translate("MainWindow", u"Reparaci\u00f3n realizada en los distintos laboratorios", None))
        self.tipo_servicio.setItemText(2, QCoreApplication.translate("MainWindow", u"Ensayo realizado en campo o en laboratorio", None))

        self.label_nom_sector.setText(QCoreApplication.translate("MainWindow", u"Recibe:", None))
        self.nom_sector.setItemText(0, QCoreApplication.translate("MainWindow", u"Castelar", None))
        self.nom_sector.setItemText(1, QCoreApplication.translate("MainWindow", u"Villa Luro", None))
        self.nom_sector.setItemText(2, QCoreApplication.translate("MainWindow", u"Liniers", None))
        self.nom_sector.setItemText(3, QCoreApplication.translate("MainWindow", u"Haedo", None))
        self.nom_sector.setItemText(4, QCoreApplication.translate("MainWindow", u"Laboratorio de Electr\u00f3nica", None))
        self.nom_sector.setItemText(5, QCoreApplication.translate("MainWindow", u"Laboratorio de Mecanica", None))

        self.label_nota_servicio.setText(QCoreApplication.translate("MainWindow", u"Nota de servicio n\u00b0:", None))
        self.label_servicio.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_sector.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Datos de solicitante", None))
        self.label_nom_solicitante.setText(QCoreApplication.translate("MainWindow", u"Nombre y apellido: ", None))
        self.label_sector_solicitante.setText(QCoreApplication.translate("MainWindow", u"Sector:", None))
        self.label_ref_ot.setText(QCoreApplication.translate("MainWindow", u"Referencia Ingreso O.T. N\u00b0 ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Origen del componente o formacion intervenida", None))
        self.label_num_formacion.setText(QCoreApplication.translate("MainWindow", u"Formacion:", None))
        self.num_formacion.setItemText(0, QCoreApplication.translate("MainWindow", u"No especificado", None))
        self.num_formacion.setItemText(1, QCoreApplication.translate("MainWindow", u"SC222", None))

        self.label_num_coche.setText(QCoreApplication.translate("MainWindow", u"Coche:", None))
        self.num_coche.setItemText(0, QCoreApplication.translate("MainWindow", u"No especificado", None))
        self.num_coche.setItemText(1, QCoreApplication.translate("MainWindow", u"RC01", None))
        self.num_coche.setItemText(2, QCoreApplication.translate("MainWindow", u"RC02", None))
        self.num_coche.setItemText(3, QCoreApplication.translate("MainWindow", u"RC03", None))
        self.num_coche.setItemText(4, QCoreApplication.translate("MainWindow", u"RC04", None))
        self.num_coche.setItemText(5, QCoreApplication.translate("MainWindow", u"RC05", None))
        self.num_coche.setItemText(6, QCoreApplication.translate("MainWindow", u"RC06", None))
        self.num_coche.setItemText(7, QCoreApplication.translate("MainWindow", u"RC07", None))
        self.num_coche.setItemText(8, QCoreApplication.translate("MainWindow", u"RC08", None))
        self.num_coche.setItemText(9, QCoreApplication.translate("MainWindow", u"RC09", None))
        self.num_coche.setItemText(10, QCoreApplication.translate("MainWindow", u"RC10", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Descripcion del componente o sistema a reparar, revisar o ensayar", None))
        self.label_nom_modulo.setText(QCoreApplication.translate("MainWindow", u"Modulo:", None))
        self.nom_modulo.setItemText(0, QCoreApplication.translate("MainWindow", u"DACU", None))
        self.nom_modulo.setItemText(1, QCoreApplication.translate("MainWindow", u"IDU", None))
        self.nom_modulo.setItemText(2, QCoreApplication.translate("MainWindow", u"Balasto 110V", None))

        self.label_nom_sistema.setText(QCoreApplication.translate("MainWindow", u"Sistema:", None))
        self.nom_sistema.setItemText(0, QCoreApplication.translate("MainWindow", u"PIDS", None))
        self.nom_sistema.setItemText(1, QCoreApplication.translate("MainWindow", u"Iluminaci\u00f3n", None))

        self.label_num_serie.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 Serie:", None))
        self.check_primer_ingreso.setText(QCoreApplication.translate("MainWindow", u"\u00bfPrimer ingreso?", None))
        self.label_num_servicio_ant.setText(QCoreApplication.translate("MainWindow", u"N\u00b0 de servicio anterior:", None))
        self.label_tipo_servicio_ant.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_num_recibe_ant.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label_obs.setText(QCoreApplication.translate("MainWindow", u"Observaciones:", None))
        self.btn_tool_obs.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n de los trabajos realizados", None))
        self.label_nom_operario_int_en.setText(QCoreApplication.translate("MainWindow", u"Nombre operario de taller: ", None))
        self.label_detalle_rep.setText(QCoreApplication.translate("MainWindow", u"Detalle de trabajo realizado:", None))
        self.label_mat_utilizados.setText(QCoreApplication.translate("MainWindow", u"Materiales utilizados:", None))
        self.btn_tool_mat_utilizados.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.frame_verificacion.setTitle(QCoreApplication.translate("MainWindow", u"Verificaci\u00f3n", None))
        self.label_verificacion.setText(QCoreApplication.translate("MainWindow", u"\u00bfContiene el m\u00f3dulo o sistema, especificaci\u00f3n para su verificaci\u00f3n o revisi\u00f3n?", None))
        self.con_especificiacion.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.codigos.setText("")
        self.codigos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Indicar c\u00f3digo de documentos utilizados", None))
        self.sin_especificacion.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.testing.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Indicar prueba realizada", None))
        self.label_nom_recibio.setText(QCoreApplication.translate("MainWindow", u"Recibio:", None))
        self.nom_recibio.setItemText(0, QCoreApplication.translate("MainWindow", u"Armada Sebastian", None))
        self.nom_recibio.setItemText(1, QCoreApplication.translate("MainWindow", u"Calder\u00f3n Diego", None))
        self.nom_recibio.setItemText(2, QCoreApplication.translate("MainWindow", u"Lo Castro Agustin", None))
        self.nom_recibio.setItemText(3, QCoreApplication.translate("MainWindow", u"Pilato Bruno", None))
        self.nom_recibio.setItemText(4, QCoreApplication.translate("MainWindow", u"Vargas Nahuel", None))

        self.label_fecha_recibio.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_nom_realizo.setText(QCoreApplication.translate("MainWindow", u"Realizo:", None))
        self.nom_realizo.setItemText(0, QCoreApplication.translate("MainWindow", u"Armada Sebastian", None))
        self.nom_realizo.setItemText(1, QCoreApplication.translate("MainWindow", u"Calder\u00f3n Diego", None))
        self.nom_realizo.setItemText(2, QCoreApplication.translate("MainWindow", u"Lo Castro Agustin", None))
        self.nom_realizo.setItemText(3, QCoreApplication.translate("MainWindow", u"Pilato Bruno", None))
        self.nom_realizo.setItemText(4, QCoreApplication.translate("MainWindow", u"Vargas Nahuel", None))

        self.label_fecha_realizo.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_nom_verifico.setText(QCoreApplication.translate("MainWindow", u"Verifico:", None))
        self.nom_verifico.setItemText(0, QCoreApplication.translate("MainWindow", u"Armada Sebastian", None))
        self.nom_verifico.setItemText(1, QCoreApplication.translate("MainWindow", u"Calder\u00f3n Diego", None))
        self.nom_verifico.setItemText(2, QCoreApplication.translate("MainWindow", u"Lo Castro Agustin", None))
        self.nom_verifico.setItemText(3, QCoreApplication.translate("MainWindow", u"Pilato Bruno", None))
        self.nom_verifico.setItemText(4, QCoreApplication.translate("MainWindow", u"Vargas Nahuel", None))

        self.label_fecha_verifico.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.guardar_pdf.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.imprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Guardar e imprimir", None))
    # retranslateUi

