# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazGestor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_10 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet("QFrame#frame_10 {\n"
"border: none;\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("QFrame#frame {\n"
"border: none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.barraBusqueda = QtWidgets.QLineEdit(self.frame)
        self.barraBusqueda.setMinimumSize(QtCore.QSize(0, 30))
        self.barraBusqueda.setText("")
        self.barraBusqueda.setObjectName("barraBusqueda")
        self.horizontalLayout.addWidget(self.barraBusqueda)
        self.btnBuscar1 = QtWidgets.QToolButton(self.frame)
        self.btnBuscar1.setMinimumSize(QtCore.QSize(0, 30))
        self.btnBuscar1.setObjectName("btnBuscar1")
        self.horizontalLayout.addWidget(self.btnBuscar1)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.frame_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("QFrame#frame_2 {\n"
"border: none;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tablaProductos = QtWidgets.QTableWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablaProductos.sizePolicy().hasHeightForWidth())
        self.tablaProductos.setSizePolicy(sizePolicy)
        self.tablaProductos.setMinimumSize(QtCore.QSize(0, 360))
        self.tablaProductos.setMaximumSize(QtCore.QSize(16777215, 360))
        self.tablaProductos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablaProductos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaProductos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablaProductos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablaProductos.setShowGrid(False)
        self.tablaProductos.setGridStyle(QtCore.Qt.SolidLine)
        self.tablaProductos.setObjectName("tablaProductos")
        self.tablaProductos.setColumnCount(5)
        self.tablaProductos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaProductos.setHorizontalHeaderItem(4, item)
        self.tablaProductos.horizontalHeader().setCascadingSectionResizes(True)
        self.tablaProductos.horizontalHeader().setDefaultSectionSize(200)
        self.tablaProductos.horizontalHeader().setSortIndicatorShown(False)
        self.tablaProductos.horizontalHeader().setStretchLastSection(True)
        self.tablaProductos.verticalHeader().setCascadingSectionResizes(False)
        self.tablaProductos.verticalHeader().setDefaultSectionSize(23)
        self.tablaProductos.verticalHeader().setSortIndicatorShown(False)
        self.tablaProductos.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.tablaProductos)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.verticalLayout.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet("QFrame#frame_9 {\n"
"border: none;\n"
"}")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("QFrame#frame_6 {\n"
"border: none;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.selectProducto = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectProducto.sizePolicy().hasHeightForWidth())
        self.selectProducto.setSizePolicy(sizePolicy)
        self.selectProducto.setMinimumSize(QtCore.QSize(0, 30))
        self.selectProducto.setObjectName("selectProducto")
        self.horizontalLayout_4.addWidget(self.selectProducto)
        self.input1 = QtWidgets.QLineEdit(self.frame_6)
        self.input1.setMinimumSize(QtCore.QSize(0, 30))
        self.input1.setObjectName("input1")
        self.horizontalLayout_4.addWidget(self.input1)
        self.input3 = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input3.sizePolicy().hasHeightForWidth())
        self.input3.setSizePolicy(sizePolicy)
        self.input3.setMinimumSize(QtCore.QSize(0, 30))
        self.input3.setText("")
        self.input3.setObjectName("input3")
        self.horizontalLayout_4.addWidget(self.input3)
        self.checkIva = QtWidgets.QCheckBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkIva.sizePolicy().hasHeightForWidth())
        self.checkIva.setSizePolicy(sizePolicy)
        self.checkIva.setMinimumSize(QtCore.QSize(0, 30))
        self.checkIva.setObjectName("checkIva")
        self.horizontalLayout_4.addWidget(self.checkIva)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_13 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet("QFrame#frame_13 {\n"
"border: none;\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label = QtWidgets.QLabel(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.horizontalLayout_8.addWidget(self.label)
        self.comboVendedor = QtWidgets.QComboBox(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboVendedor.sizePolicy().hasHeightForWidth())
        self.comboVendedor.setSizePolicy(sizePolicy)
        self.comboVendedor.setMinimumSize(QtCore.QSize(0, 30))
        self.comboVendedor.setObjectName("comboVendedor")
        self.horizontalLayout_8.addWidget(self.comboVendedor)
        self.btn_agregar_carrito = QtWidgets.QPushButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_agregar_carrito.sizePolicy().hasHeightForWidth())
        self.btn_agregar_carrito.setSizePolicy(sizePolicy)
        self.btn_agregar_carrito.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_agregar_carrito.setObjectName("btn_agregar_carrito")
        self.horizontalLayout_8.addWidget(self.btn_agregar_carrito)
        self.btnCerrarVenta = QtWidgets.QToolButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCerrarVenta.sizePolicy().hasHeightForWidth())
        self.btnCerrarVenta.setSizePolicy(sizePolicy)
        self.btnCerrarVenta.setMinimumSize(QtCore.QSize(0, 30))
        self.btnCerrarVenta.setObjectName("btnCerrarVenta")
        self.horizontalLayout_8.addWidget(self.btnCerrarVenta)
        self.btnCancelar = QtWidgets.QToolButton(self.frame_13)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setMinimumSize(QtCore.QSize(0, 30))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout_8.addWidget(self.btnCancelar)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.carrito = QtWidgets.QTableWidget(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carrito.sizePolicy().hasHeightForWidth())
        self.carrito.setSizePolicy(sizePolicy)
        self.carrito.setMinimumSize(QtCore.QSize(0, 100))
        self.carrito.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.carrito.setBaseSize(QtCore.QSize(0, 150))
        self.carrito.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.carrito.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.carrito.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.carrito.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.carrito.setShowGrid(False)
        self.carrito.setObjectName("carrito")
        self.carrito.setColumnCount(6)
        self.carrito.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.carrito.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.carrito.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.carrito.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.carrito.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.carrito.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.carrito.setHorizontalHeaderItem(5, item)
        self.carrito.horizontalHeader().setDefaultSectionSize(220)
        self.carrito.horizontalHeader().setHighlightSections(True)
        self.carrito.horizontalHeader().setSortIndicatorShown(False)
        self.carrito.horizontalHeader().setStretchLastSection(True)
        self.carrito.verticalHeader().setCascadingSectionResizes(False)
        self.carrito.verticalHeader().setDefaultSectionSize(23)
        self.carrito.verticalHeader().setSortIndicatorShown(False)
        self.carrito.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_4.addWidget(self.carrito)
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet("QFrame#frame_12 {\n"
"border: none;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.ingresos_totales_dia = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingresos_totales_dia.sizePolicy().hasHeightForWidth())
        self.ingresos_totales_dia.setSizePolicy(sizePolicy)
        self.ingresos_totales_dia.setObjectName("ingresos_totales_dia")
        self.horizontalLayout_7.addWidget(self.ingresos_totales_dia)
        self.ingresos_totales = QtWidgets.QLabel(self.frame_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingresos_totales.sizePolicy().hasHeightForWidth())
        self.ingresos_totales.setSizePolicy(sizePolicy)
        self.ingresos_totales.setObjectName("ingresos_totales")
        self.horizontalLayout_7.addWidget(self.ingresos_totales)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.verticalLayout.addWidget(self.frame_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 890, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuGestion = QtWidgets.QMenu(self.menuBar)
        self.menuGestion.setObjectName("menuGestion")
        MainWindow.setMenuBar(self.menuBar)
        self.actionVentas = QtWidgets.QAction(MainWindow)
        self.actionVentas.setObjectName("actionVentas")
        self.actionProductos = QtWidgets.QAction(MainWindow)
        self.actionProductos.setObjectName("actionProductos")
        self.actionClientes = QtWidgets.QAction(MainWindow)
        self.actionClientes.setObjectName("actionClientes")
        self.actionProductos_2 = QtWidgets.QAction(MainWindow)
        self.actionProductos_2.setObjectName("actionProductos_2")
        self.actionEmpleados = QtWidgets.QAction(MainWindow)
        self.actionEmpleados.setObjectName("actionEmpleados")
        self.actionVentas_2 = QtWidgets.QAction(MainWindow)
        self.actionVentas_2.setObjectName("actionVentas_2")
        self.menuGestion.addAction(self.actionProductos_2)
        self.menuGestion.addAction(self.actionEmpleados)
        self.menuGestion.addAction(self.actionVentas_2)
        self.menuBar.addAction(self.menuGestion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestor de ventas"))
        self.barraBusqueda.setPlaceholderText(_translate("MainWindow", "Buscar por descripcion"))
        self.btnBuscar1.setText(_translate("MainWindow", "Buscar"))
        item = self.tablaProductos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tablaProductos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Codigo"))
        item = self.tablaProductos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descripcion"))
        item = self.tablaProductos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Precio"))
        item = self.tablaProductos.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Stock"))
        self.selectProducto.setPlaceholderText(_translate("MainWindow", "Codigo de producto"))
        self.input1.setPlaceholderText(_translate("MainWindow", "Unidades"))
        self.input3.setPlaceholderText(_translate("MainWindow", "Porcentaje de descuento"))
        self.checkIva.setText(_translate("MainWindow", "Incluir IVA (21%)"))
        self.label.setText(_translate("MainWindow", "Empleado"))
        self.btn_agregar_carrito.setText(_translate("MainWindow", "Agregar al carrito"))
        self.btnCerrarVenta.setText(_translate("MainWindow", "Cerrar venta"))
        self.btnCancelar.setText(_translate("MainWindow", "Limpiar carrito"))
        item = self.carrito.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cod. Producto"))
        item = self.carrito.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Unidades"))
        item = self.carrito.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Importe"))
        item = self.carrito.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IVA"))
        item = self.carrito.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Descuento"))
        item = self.carrito.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Importe total"))
        self.ingresos_totales_dia.setText(_translate("MainWindow", "INGRESOS DEL DIA:"))
        self.ingresos_totales.setText(_translate("MainWindow", "INGRESOS DEL MES:"))
        self.menuGestion.setTitle(_translate("MainWindow", "Gestion"))
        self.actionVentas.setText(_translate("MainWindow", "Ventas"))
        self.actionProductos.setText(_translate("MainWindow", "Productos"))
        self.actionClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionProductos_2.setText(_translate("MainWindow", "Productos"))
        self.actionEmpleados.setText(_translate("MainWindow", "Empleados"))
        self.actionVentas_2.setText(_translate("MainWindow", "Ventas"))
