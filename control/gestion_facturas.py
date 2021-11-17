from sql.datos import Facturas
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget

def conf_tabla_facturas(self):
    self.ui.tablaProductos.horizontalHeaderItem(1).setText('Numero')
    self.ui.tablaProductos.horizontalHeaderItem(2).setText('Cliente')
    self.ui.tablaProductos.horizontalHeaderItem(3).setText('Fecha de emisión')
    self.ui.tablaProductos.horizontalHeaderItem(4).setText('Importe')
    self.ui.barra_busqueda.setPlaceholderText('Nombre, apellido o fecha de emisión (mes-día)')
    self.ui.frame_3.hide()

def cargar_tabla_facturas(self):
    deleteAllRows(self.ui.tablaProductos)
    for i, row in enumerate(Facturas.select()):
        self.ui.tablaProductos.insertRow(i)
        self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.id)))
        self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(str(row.numero)))
        self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(f'{row.nombre_cliente} {row.apellido_cliente}'))
        self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(str(row.fecha_emision)))
        self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(str(row.importe_total)))

def filtros_factura(self):
    ids = []
    deleteAllRows(self.ui.tablaProductos)
    if self.ui.barra_busqueda.text() == '':
        cargar_tabla_facturas(self)
    else:
        buscado = self.ui.barra_busqueda.text().lower()
        cont = 0
        for row in Facturas.select():
            if buscado in row.nombre_cliente.lower() or buscado in row.apellido_cliente.lower():
                self.ui.tablaProductos.insertRow(cont)
                self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(str(row.numero)))
                self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(f'{row.nombre_cliente} {row.apellido_cliente}'))
                self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(str(row.fecha_emision)))
                self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(str(row.importe_total)))
                ids.append(row.numero)
                cont += 1

        for row in Facturas.select():
            habilitado = True
            if buscado in str(row.fecha_emision):
                for code in ids:
                    if code == row.numero:
                        habilitado = False
                if habilitado:
                    self.ui.tablaProductos.insertRow(cont)
                    self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                    self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(str(row.numero)))
                    self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(f'{row.nombre_cliente} {row.apellido_cliente}'))
                    self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(str(row.fecha_emision)))
                    self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(str(row.importe_total)))
                    cont += 1

def deleteAllRows(table: QTableWidget) -> None:
    model: QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())