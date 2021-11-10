import sys
import os
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidget, QTableWidgetItem

from interfaces.interfazGestor import Ui_MainWindow
from interfaces.interfazInformacionVentas import Ui_interfazInfoVentas
from interfaces.mensajeError import Ui_Dialog
from interfaces.interfazGestorProductos import Ui_gestion_productos
from interfaces.interfazNuevoProducto import Ui_nuevo_producto

from sql.productos import *
from sql.ventas import *
from sql.empleados import *

from controllers.carrito import *
from controllers.crear_db import *
from controllers.validacion import *
from controllers.gestion_productos import *
from controllers.nuevo_producto import agregar_producto
from controllers.editar_producto import cargar, editar_producto

import datetime

class Application(QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.fecha_hoy = datetime.date.today()

		iniciar_db()
		cargar_tabla_productos(self)
		cargar_tabla_ventas(self)
		cargar_comboVendedor(self)

		self.ui.actionProductos_2.triggered.connect(self.gestion_productos)

		self.ui.checkIva.setChecked(1)
		self.ui.btnBuscar1.clicked.connect(self.buscar)
		self.ui.barraBusqueda.setFocus()
		self.ui.barraBusqueda.returnPressed.connect(self.ui.btnBuscar1.click)
		self.ui.selectProducto.returnPressed.connect(self.ui.btn_agregar_carrito.click)
		self.ui.btn_agregar_carrito.clicked.connect(self.agregar_carrito)
		self.ui.input1.returnPressed.connect(self.ui.btn_agregar_carrito.click)
		self.ui.input3.returnPressed.connect(self.ui.btn_agregar_carrito.click)
		self.ui.btnCerrarVenta.clicked.connect(self.cerrar_venta)
		self.ui.btnCancelar.clicked.connect(self.cancelar_venta)

		self.ui.tablaVentas.cellDoubleClicked.connect(self.informacionVenta) # SIN TERMINAR

		self.importes_totales_dia()

		self.importe_total = 0
		self.total_ventas = 0

		self.showMaximized()
		self.show()

	def ventana_editar_producto(self):
		self.editar_producto = QDialog()
		self.editar_producto.ui = Ui_nuevo_producto()
		self.editar_producto.ui.setupUi(self.editar_producto)
		self.editar_producto.setWindowTitle('Editar producto')
		self.editar_producto.ui.btn_nuevo_producto.setText('Actualizar')
		self.editar_producto.ui.btn_nuevo_producto.clicked.connect(self.editar_producto_accion)
		try:
			cargar(self)
			self.editar_producto.show()
		except:
			self.mostrarError('Debe seleccionar un producto de la tabla primero.')

	def editar_producto_accion(self):
		editar_producto(self)
		cargar_tabla(self.gestion_productos)
		cargar_tabla_productos(self)

	def ventana_nuevo_producto(self):
		self.nuevo_producto = QDialog()
		self.nuevo_producto.ui = Ui_nuevo_producto()
		self.nuevo_producto.ui.setupUi(self.nuevo_producto)
		self.nuevo_producto.ui.input_codigo.setFocus()
		self.nuevo_producto.ui.btn_nuevo_producto.clicked.connect(self.agregar_nuevo_producto)
		self.nuevo_producto.show()

	def agregar_nuevo_producto(self):
		try:
			agregar_producto(self.nuevo_producto)
			cargar_tabla(self.gestion_productos)
			cargar_tabla_productos(self)
		except:
			self.mostrarError('Ya existe un producto que posee ese codigo.')

	def gestion_productos(self):
		self.gestion_productos = QDialog()
		self.gestion_productos.ui = Ui_gestion_productos()
		self.gestion_productos.ui.setupUi(self.gestion_productos)
		cargar_tabla(self.gestion_productos)
		self.gestion_productos.ui.btn_buscar.clicked.connect(self.buscar_gestion_productos)
		self.gestion_productos.ui.btn_nuevo.clicked.connect(self.ventana_nuevo_producto)
		self.gestion_productos.ui.btn_remover.clicked.connect(self.remover_gestion_productos)
		self.gestion_productos.ui.btn_editar.clicked.connect(self.ventana_editar_producto)
		self.gestion_productos.show()

	def remover_gestion_productos(self):
		try:
			eliminar(self.gestion_productos)
			cargar_tabla_productos(self)
		except:
			self.mostrarError('Ha ocurrido un error, contacte con el desarrollador.')

	def buscar_gestion_productos(self):
		buscar_gp(self.gestion_productos)

	def informacionVenta(self):
		self.informacionVenta = QDialog()
		self.informacionVenta.ui = Ui_interfazInfoVentas()
		self.informacionVenta.ui.setupUi(self.informacionVenta)
		self.informacionVenta.ui.codigo_vendedor.setText(f'Cod. Vendedor: {self.click_celda()[1]}')
		self.informacionVenta.ui.importe_total.setText(f'Importe total: {self.click_celda()[2]}')
		self.informacionVenta.ui.fecha_hora.setText(f'Fecha y hora de venta: {self.click_celda()[3]}')
		self.informacionVenta.show()

	def buscar(self):
		buscar(self)

	def click_celda(self):
		datos_fila = []
		for i in range(4):
			datos_fila.append(self.ui.tablaVentas.selectedIndexes()[i].data())
		return datos_fila

	def agregar_carrito(self):
		if self.ui.selectProducto.text() == '':
			self.mostrarError('Codigo de producto obligatorio.')
		elif validacion(self.ui.input1.text()) == False or validacion(self.ui.input3.text()) == False:
			self.mostrarError('Solo se permiten valores numericos.')
		else:
			try:
				self.importe_total = self.importe_total + agregar_al_carrito(self)			
			except:
				self.mostrarError('Codigo invalido o sin stock.')

	def mostrarError(self, mensaje):
		self.msgError = QDialog()
		self.msgError.ui = Ui_Dialog()
		self.msgError.ui.setupUi(self.msgError)
		self.msgError.ui.msgError.setText(mensaje)
		self.msgError.ui.btn_aceptar_error.clicked.connect(self.close)
		self.msgError.show()

	def close(self):
		self.msgError.close()

	def cerrar_venta(self):
		cerrar_venta(self)

	def cancelar_venta(self):
		cancelar_venta(self)

	def importes_totales_dia(self):
		importes_totales_dia(self)

if __name__ == '__main__':

	app = QApplication(sys.argv)
	application = Application()
	application.show()
	sys.exit(app.exec_())