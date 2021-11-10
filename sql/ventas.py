from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from peewee import *
import datetime

from sql.productos import reducir_stock, cargar_tabla_productos
from sql.empleados import Vendedor

db = SqliteDatabase('db.sqlite')

class Venta(Model):
	venta = AutoField(unique=True)
	codigo_vendedor = CharField()
	importe = CharField()
	fecha_registro = DateField(default=datetime.datetime.now())

	class Meta:
		database = db
		db_table = 'ventas'

def cerrar_venta(self):
	if self.ui.carrito.item(0, 0) != None:
		reducir_stock(self)
		fecha = self.gestion_ventas.ui.tablaProductos.item(1, 3)
		deleteAllRows(self.ui.carrito)
		cargar_tabla_productos(self)
		if not fecha == datetime.date.today():
			cargar_venta(self)
		else:
			cargar_venta(self)

def cargar_venta(self):
	for row in Vendedor.select().where(Vendedor.nombre == (self.ui.comboVendedor.currentText()).lower()):
		Venta.create(
			codigo_vendedor=row.codigo,
			importe=self.importe_total,
			registro=datetime.datetime.now())
		self.importe_total = 0
		importes_totales_dia(self)

def importes_totales_dia(self):
	monto = 0
	for row in Venta.select().where(Venta.fecha_registro == datetime.date.today()):
		monto = monto + int(row.importe)
	self.ui.ingresos_totales_dia.setText(f'Ingresos dia actual: ${monto}')
	monto = 0
	for row in Venta.select():
		mes_hoy = str(datetime.date.today()).split('-')
		mes_venta = str(row.fecha_registro).split('-')
		if mes_venta[1] == mes_hoy[1]:
			monto = monto + int(row.importe)
	self.ui.ingresos_totales.setText(f'Ingresos mes actual: ${monto}')

def deleteAllRows(table:QTableWidget) -> None:
    model:QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())