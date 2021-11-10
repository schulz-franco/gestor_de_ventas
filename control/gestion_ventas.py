from sql.ventas import Venta
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget

def conf_tabla_ventas(self):
    self.ui.tablaProductos.horizontalHeaderItem(1).setText('Cod. Empleado')
    self.ui.tablaProductos.horizontalHeaderItem(2).setText('Importe')
    self.ui.tablaProductos.horizontalHeaderItem(3).setText('Fecha de venta')
    self.ui.tablaProductos.horizontalHeaderItem(4).setText('Hora de venta')
    self.ui.barra_busqueda.setPlaceholderText('Codigo de empleado, nombre o fecha')
    self.ui.btn_nuevo.hide()
    self.ui.btn_cargar_stock.hide()
    self.ui.input_unidades.hide()

def cargar_tabla_gestion_ventas(self):
    deleteAllRows(self.ui.tablaProductos)
    for i, row in enumerate(Venta.select()):
        self.ui.tablaProductos.insertRow(i)
        self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.venta)))
        self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(f'C-{(row.codigo_vendedor).upper()}'))
        self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(f'$ {row.importe}'))
        self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(str(row.fecha_registro)))

def filtros_venta(self):
    pass

def deleteAllRows(table: QTableWidget) -> None:
    model: QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())