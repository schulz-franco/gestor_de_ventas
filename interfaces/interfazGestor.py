# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfazGestor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(757, 568)
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
        self.btnBuscar1.setMinimumSize(QtCore.QSize(70, 30))
        self.btnBuscar1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.tablaProductos.setMinimumSize(QtCore.QSize(0, 280))
        self.tablaProductos.setMaximumSize(QtCore.QSize(16777215, 300))
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
        self.selectProducto.setMaximumSize(QtCore.QSize(120, 16777215))
        self.selectProducto.setObjectName("selectProducto")
        self.horizontalLayout_4.addWidget(self.selectProducto)
        self.input1 = QtWidgets.QLineEdit(self.frame_6)
        self.input1.setMinimumSize(QtCore.QSize(0, 30))
        self.input1.setMaximumSize(QtCore.QSize(120, 16777215))
        self.input1.setObjectName("input1")
        self.horizontalLayout_4.addWidget(self.input1)
        self.input3 = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input3.sizePolicy().hasHeightForWidth())
        self.input3.setSizePolicy(sizePolicy)
        self.input3.setMinimumSize(QtCore.QSize(0, 30))
        self.input3.setMaximumSize(QtCore.QSize(140, 16777215))
        self.input3.setText("")
        self.input3.setObjectName("input3")
        self.horizontalLayout_4.addWidget(self.input3)
        self.checkIva = QtWidgets.QCheckBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkIva.sizePolicy().hasHeightForWidth())
        self.checkIva.setSizePolicy(sizePolicy)
        self.checkIva.setMinimumSize(QtCore.QSize(0, 30))
        self.checkIva.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.checkIva.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkIva.setObjectName("checkIva")
        self.horizontalLayout_4.addWidget(self.checkIva)
        self.btn_agregar_carrito = QtWidgets.QPushButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_agregar_carrito.sizePolicy().hasHeightForWidth())
        self.btn_agregar_carrito.setSizePolicy(sizePolicy)
        self.btn_agregar_carrito.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_agregar_carrito.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_agregar_carrito.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_agregar_carrito.setObjectName("btn_agregar_carrito")
        self.horizontalLayout_4.addWidget(self.btn_agregar_carrito)
        self.btnCancelar = QtWidgets.QToolButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCancelar.sizePolicy().hasHeightForWidth())
        self.btnCancelar.setSizePolicy(sizePolicy)
        self.btnCancelar.setMinimumSize(QtCore.QSize(0, 30))
        self.btnCancelar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnCancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout_4.addWidget(self.btnCancelar)
        self.btn_facturar = QtWidgets.QPushButton(self.frame_6)
        self.btn_facturar.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_facturar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_facturar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_facturar.setObjectName("btn_facturar")
        self.horizontalLayout_4.addWidget(self.btn_facturar)
        self.comboVendedor = QtWidgets.QComboBox(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboVendedor.sizePolicy().hasHeightForWidth())
        self.comboVendedor.setSizePolicy(sizePolicy)
        self.comboVendedor.setMinimumSize(QtCore.QSize(0, 30))
        self.comboVendedor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboVendedor.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboVendedor.setObjectName("comboVendedor")
        self.horizontalLayout_4.addWidget(self.comboVendedor)
        self.btnCerrarVenta = QtWidgets.QToolButton(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnCerrarVenta.sizePolicy().hasHeightForWidth())
        self.btnCerrarVenta.setSizePolicy(sizePolicy)
        self.btnCerrarVenta.setMinimumSize(QtCore.QSize(0, 30))
        self.btnCerrarVenta.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnCerrarVenta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCerrarVenta.setObjectName("btnCerrarVenta")
        self.horizontalLayout_4.addWidget(self.btnCerrarVenta)
        self.verticalLayout_4.addWidget(self.frame_6)
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
        self.importe_de_venta = QtWidgets.QLabel(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importe_de_venta.sizePolicy().hasHeightForWidth())
        self.importe_de_venta.setSizePolicy(sizePolicy)
        self.importe_de_venta.setStyleSheet("")
        self.importe_de_venta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.importe_de_venta.setObjectName("importe_de_venta")
        self.verticalLayout_4.addWidget(self.importe_de_venta)
        self.verticalLayout.addWidget(self.frame_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 757, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuProductos = QtWidgets.QMenu(self.menuBar)
        self.menuProductos.setObjectName("menuProductos")
        self.menuVentas = QtWidgets.QMenu(self.menuBar)
        self.menuVentas.setObjectName("menuVentas")
        self.menuEmpleados = QtWidgets.QMenu(self.menuBar)
        self.menuEmpleados.setObjectName("menuEmpleados")
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
        self.actionProductos_3 = QtWidgets.QAction(MainWindow)
        self.actionProductos_3.setObjectName("actionProductos_3")
        self.actionVentas_3 = QtWidgets.QAction(MainWindow)
        self.actionVentas_3.setObjectName("actionVentas_3")
        self.actionEmpleados_2 = QtWidgets.QAction(MainWindow)
        self.actionEmpleados_2.setObjectName("actionEmpleados_2")
        self.action_exportar_productos = QtWidgets.QAction(MainWindow)
        self.action_exportar_productos.setObjectName("action_exportar_productos")
        self.action_exportar_empleados = QtWidgets.QAction(MainWindow)
        self.action_exportar_empleados.setObjectName("action_exportar_empleados")
        self.action_exportar_ventas = QtWidgets.QAction(MainWindow)
        self.action_exportar_ventas.setObjectName("action_exportar_ventas")
        self.actionFacturas_3 = QtWidgets.QAction(MainWindow)
        self.actionFacturas_3.setObjectName("actionFacturas_3")
        self.action_exportar_facturas = QtWidgets.QAction(MainWindow)
        self.action_exportar_facturas.setObjectName("action_exportar_facturas")
        self.menuProductos.addAction(self.actionProductos_3)
        self.menuProductos.addAction(self.action_exportar_productos)
        self.menuVentas.addAction(self.actionVentas_3)
        self.menuVentas.addAction(self.action_exportar_ventas)
        self.menuVentas.addSeparator()
        self.menuVentas.addAction(self.actionFacturas_3)
        self.menuVentas.addAction(self.action_exportar_facturas)
        self.menuEmpleados.addAction(self.actionEmpleados_2)
        self.menuEmpleados.addAction(self.action_exportar_empleados)
        self.menuBar.addAction(self.menuProductos.menuAction())
        self.menuBar.addAction(self.menuEmpleados.menuAction())
        self.menuBar.addAction(self.menuVentas.menuAction())

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
        self.btn_agregar_carrito.setText(_translate("MainWindow", "Agregar al carrito"))
        self.btnCancelar.setText(_translate("MainWindow", "Limpiar carrito"))
        self.btn_facturar.setText(_translate("MainWindow", "Generar factura"))
        self.btnCerrarVenta.setText(_translate("MainWindow", "Cerrar venta"))
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
        self.importe_de_venta.setText(_translate("MainWindow", "TOTAL"))
        self.menuProductos.setTitle(_translate("MainWindow", "Productos"))
        self.menuVentas.setTitle(_translate("MainWindow", "Registros"))
        self.menuEmpleados.setTitle(_translate("MainWindow", "Empleados"))
        self.actionVentas.setText(_translate("MainWindow", "Ventas"))
        self.actionProductos.setText(_translate("MainWindow", "Productos"))
        self.actionClientes.setText(_translate("MainWindow", "Clientes"))
        self.actionProductos_2.setText(_translate("MainWindow", "Productos"))
        self.actionEmpleados.setText(_translate("MainWindow", "Empleados"))
        self.actionVentas_2.setText(_translate("MainWindow", "Ventas"))
        self.actionProductos_3.setText(_translate("MainWindow", "Gestionar"))
        self.actionVentas_3.setText(_translate("MainWindow", "Consultar ventas"))
        self.actionEmpleados_2.setText(_translate("MainWindow", "Gestionar"))
        self.action_exportar_productos.setText(_translate("MainWindow", "Exportar excel"))
        self.action_exportar_empleados.setText(_translate("MainWindow", "Exportar excel"))
        self.action_exportar_ventas.setText(_translate("MainWindow", "Exportar excel"))
        self.actionFacturas_3.setText(_translate("MainWindow", "Consultar facturas"))
        self.action_exportar_facturas.setText(_translate("MainWindow", "Exportar excel"))
