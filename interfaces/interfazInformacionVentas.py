# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazInformacionVentas.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_interfazInfoVentas(object):
    def setupUi(self, interfazInfoVentas):
        interfazInfoVentas.setObjectName("interfazInfoVentas")
        interfazInfoVentas.resize(393, 76)
        self.verticalLayout = QtWidgets.QVBoxLayout(interfazInfoVentas)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(interfazInfoVentas)
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.codigo_vendedor = QtWidgets.QLabel(self.frame)
        self.codigo_vendedor.setObjectName("codigo_vendedor")
        self.verticalLayout_2.addWidget(self.codigo_vendedor)
        self.importe_total = QtWidgets.QLabel(self.frame)
        self.importe_total.setObjectName("importe_total")
        self.verticalLayout_2.addWidget(self.importe_total)
        self.fecha_hora = QtWidgets.QLabel(self.frame)
        self.fecha_hora.setObjectName("fecha_hora")
        self.verticalLayout_2.addWidget(self.fecha_hora)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(interfazInfoVentas)
        QtCore.QMetaObject.connectSlotsByName(interfazInfoVentas)

    def retranslateUi(self, interfazInfoVentas):
        _translate = QtCore.QCoreApplication.translate
        interfazInfoVentas.setWindowTitle(_translate("interfazInfoVentas", "Venta"))
        self.codigo_vendedor.setText(_translate("interfazInfoVentas", "Cod. Vendedor:"))
        self.importe_total.setText(_translate("interfazInfoVentas", "Importe total:"))
        self.fecha_hora.setText(_translate("interfazInfoVentas", "Fecha y hora de venta:"))
