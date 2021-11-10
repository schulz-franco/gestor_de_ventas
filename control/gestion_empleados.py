from sql.empleados import Vendedor
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

def conf_tabla_empleados(self):
    self.ui.tablaProductos.horizontalHeaderItem(1).setText('Cod. Empleado')
    self.ui.tablaProductos.horizontalHeaderItem(2).setText('Nombre')
    self.ui.tablaProductos.horizontalHeaderItem(3).setText('Apellido')
    self.ui.tablaProductos.horizontalHeaderItem(4).setText('Ventas realizadas')
    self.ui.barra_busqueda.setPlaceholderText('Codigo, apellido o nombre')
    self.ui.btn_cargar_stock.setText('Mas información')
    self.ui.input_unidades.hide()

def cargar_tabla_gestion_empleados(self):
    deleteAllRows(self.ui.tablaProductos)
    for i, row in enumerate(Vendedor.select()):
        self.ui.tablaProductos.insertRow(i)
        self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.id)))
        self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(f'C-{(row.codigo).upper()}'))
        self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(row.nombre.capitalize()))
        self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(row.apellido.capitalize()))
        self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(''))

def deleteAllRows(table: QTableWidget) -> None:
    model: QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())