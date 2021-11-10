from sql.productos import Producto
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

def cargar_tabla(self):
    deleteAllRows(self.ui.tablaProductos)
    for i, row in enumerate(Producto.select()):
        self.ui.tablaProductos.insertRow(i)
        self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.id)))
        self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(row.codigo))
        self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(row.descripcion))
        self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(f'$ {row.precio}'))
        self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(row.stock))

def buscar_gp(self):
    codigos = []
    deleteAllRows(self.ui.tablaProductos)
    if self.ui.barra_busqueda.text() == '':
        cargar_tabla(self)
    else:
        buscado = (self.ui.barra_busqueda.text()).lower()
        cont = 0
        for row in Producto.select():
            if buscado in row.codigo:
                self.ui.tablaProductos.insertRow(cont)
                self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(row.codigo))
                self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(row.descripcion))
                self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(f'$ {row.precio}'))
                self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(row.stock))
                codigos.append(row.codigo)
                cont += 1

        for i, row in enumerate(Producto.select()):
            habilitado = True
            if buscado in row.descripcion:
                for code in codigos:
                    if code == row.codigo:
                        habilitado = False
                if habilitado:
                    self.ui.tablaProductos.insertRow(cont)
                    self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                    self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(row.codigo))
                    self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(row.descripcion))
                    self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(f'$ {row.precio}'))
                    self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(row.stock))
                    cont += 1

def eliminar(self):
    codigo = self.ui.tablaProductos.selectedIndexes()[1].data()
    for item in Producto.select().where(Producto.codigo == codigo.lower()):
        item.delete_instance()
    cargar_tabla(self)

def deleteAllRows(table: QTableWidget) -> None:
    model: QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())