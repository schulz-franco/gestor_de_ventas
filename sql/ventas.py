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
    if self.ui.carrito.item(0, 0) is not None:
        reducir_stock(self)
        fecha = self.gestion_ventas.ui.tablaProductos.item(1, 3)
        importe_venta(self)
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


def importe_venta(self):
    importe = 0
    for cont in range(self.ui.carrito.rowCount()):
        importe = importe + int(self.ui.carrito.item(cont, 5).text()[2:])
    self.ui.importe_de_venta.setText(f'TOTAL: ${importe}')


def deleteAllRows(table: QTableWidget) -> None:
    model:QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())
