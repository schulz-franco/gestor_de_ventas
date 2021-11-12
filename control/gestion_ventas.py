# coding=utf-8
from sql.ventas import Venta
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget


def conf_tabla_ventas(self):
    self.ui.tablaProductos.horizontalHeaderItem(1).setText('Cod. Empleado')
    self.ui.tablaProductos.horizontalHeaderItem(2).setText('Importe')
    self.ui.tablaProductos.horizontalHeaderItem(3).setText('Fecha de venta')
    self.ui.tablaProductos.horizontalHeaderItem(4).setText('Hora de venta')
    self.ui.barra_busqueda.setPlaceholderText('Codigo de empleado o fecha de venta (mes-día)')
    self.ui.frame_3.hide()


def cargar_tabla_gestion_ventas(self):
    deleteAllRows(self.ui.tablaProductos)
    for i, row in enumerate(Venta.select()):
        self.ui.tablaProductos.insertRow(i)
        self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.venta)))
        self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(f'C-{row.codigo_vendedor.upper()}'))
        self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(f'$ {row.importe}'))
        self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(str(row.fecha_registro)))
        self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(str(row.hora_registro)[:8]))


def filtros_venta(self):
    ids = []
    deleteAllRows(self.ui.tablaProductos)
    if self.ui.barra_busqueda.text() == '':
        cargar_tabla_gestion_ventas(self)
    else:
        buscado = (self.ui.barra_busqueda.text()).lower()
        cont = 0
        for row in Venta.select():
            if buscado in row.codigo_vendedor:
                self.ui.tablaProductos.insertRow(cont)
                self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.venta)))
                self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(f'C-{(row.codigo_vendedor).upper()}'))
                self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(f'$ {row.importe}'))
                self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(str(row.fecha_registro)))
                self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(str(row.hora_registro)[:8]))
                ids.append(row.codigo_vendedor)
                cont += 1

        for i, row in enumerate(Venta.select()):
            habilitado = True
            if buscado in str(row.fecha_registro):
                for code in ids:
                    if code == row.venta:
                        habilitado = False
                if habilitado:
                    self.ui.tablaProductos.insertRow(cont)
                    self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.venta)))
                    self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(f'C-{row.codigo_vendedor.upper()}'))
                    self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(f'$ {row.importe}'))
                    self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(str(row.fecha_registro)))
                    self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(str(row.hora_registro)[:8]))
                    cont += 1


def deleteAllRows(table: QTableWidget) -> None:
    model: QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())
