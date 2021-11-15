from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from sql.datos import Producto

def cargar_tabla_productos(self):
	deleteAllRows(self.ui.tablaProductos)
	for i, row in enumerate(Producto.select()):
		self.ui.tablaProductos.insertRow(i)
		self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.id)))
		self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(row.codigo))
		self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(row.descripcion))
		self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(f'$ {row.precio}'))
		self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(row.stock))

def buscar(self):
	deleteAllRows(self.ui.tablaProductos)
	buscado = (self.ui.barraBusqueda.text()).lower()
	cont = 0
	for row in Producto.select():
		if buscado in row.descripcion:
			self.ui.tablaProductos.insertRow(cont)
			self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
			self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(row.codigo))
			self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(row.descripcion))
			self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(f'$ {row.precio}'))
			self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(row.stock))
			cont += 1

def reducir_stock(self):
	for i in range(int(self.ui.carrito.rowCount())):
		codigo = self.ui.carrito.item(i, 0).text()
		unidades = self.ui.carrito.item(i, 1).text()
		for row2 in Producto.select().where(Producto.codigo == codigo.lower()):
			row2.stock = int(row2.stock) - int(unidades)
			row2.save()

def deleteAllRows(table:QTableWidget) -> None:
	model:QAbstractTableModel = table.model()
	model.removeRows(0, model.rowCount())