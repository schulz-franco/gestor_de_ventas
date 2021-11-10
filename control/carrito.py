from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from sql.productos import Producto, cargar_tabla_productos

def agregar_al_carrito(self):
	cont = 0
	item = []
	for row in Producto.select().where(Producto.codigo == self.ui.selectProducto.text().lower()):
		if self.ui.input1.text() == '':
			self.ui.input1.setText('1')
		unidades = int(self.ui.input1.text())
		if int(row.stock) <= 0:
			row.stock = 0
			row.save()
			cargar_tabla_productos(self)
			self.ui.input1.setText('')
			return 'no_stock'
		if int(row.stock) < unidades:
			self.ui.input1.setText('')
			return 'no_stock'
		else:
			if self.ui.input1.text() == '':
				self.ui.input1.setText('1')
			if not self.ui.input3.text() == '':
				descuento = int(self.ui.input3.text())
			else:
				descuento = 0
			cantidad = int(self.ui.input1.text())
			precio = int(row.precio)
			item.append((row.codigo).upper())
			item.append(int(self.ui.input1.text()))
			importe = precio*cantidad
			item.append(importe)
			if self.ui.checkIva.isChecked():
				item.append(int(importe*0.21))
			else:
				item.append('-')
			descuento_importe = (importe / 100) * descuento
			item.append(f'{descuento}%')
			if self.ui.checkIva.isChecked():
				item.append(int(importe+(importe*0.21)-int(descuento_importe)))
			else:
				item.append(int(importe-int(descuento_importe)))
			self.ui.carrito.insertRow(cont)
			for i in range(6):
				if i > 1 and i != 4:
					self.ui.carrito.setItem(cont, i, QTableWidgetItem(f'$ {str(item[i])}'))
				else:
					self.ui.carrito.setItem(cont, i, QTableWidgetItem(str(item[i])))
			cont += 1
	self.ui.input1.setText('')
	self.ui.input3.setText('')
	self.ui.selectProducto.setText('')
	return int(item[5])

def cancelar_venta(self):
	deleteAllRows(self.ui.carrito)
	self.importe_total = 0

def deleteAllRows(table:QTableWidget) -> None:
    model:QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())