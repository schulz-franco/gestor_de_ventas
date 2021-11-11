# coding=utf-8
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
    self.ui.btn_editar.hide()


def cargar_tabla_gestion_empleados(self):
    deleteAllRows(self.ui.tablaProductos)
    for i, row in enumerate(Vendedor.select()):
        self.ui.tablaProductos.insertRow(i)
        self.ui.tablaProductos.setItem(i, 0, QTableWidgetItem(str(row.id)))
        self.ui.tablaProductos.setItem(i, 1, QTableWidgetItem(f'C-{row.codigo.upper()}'))
        self.ui.tablaProductos.setItem(i, 2, QTableWidgetItem(row.nombre.capitalize()))
        self.ui.tablaProductos.setItem(i, 3, QTableWidgetItem(row.apellido.capitalize()))
        self.ui.tablaProductos.setItem(i, 4, QTableWidgetItem(''))


def buscar_ge(self):
    codigos = []
    deleteAllRows(self.ui.tablaProductos)
    if self.ui.barra_busqueda.text() == '':
        cargar_tabla_gestion_empleados(self)
    else:
        buscado = (self.ui.barra_busqueda.text()).lower()
        cont = 0
        for row in Vendedor.select():
            if buscado in row.codigo:
                self.ui.tablaProductos.insertRow(cont)
                self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(f'C-{row.codigo.upper()}'))
                self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(row.nombre.capitalize()))
                self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(row.apellido.capitalize()))
                self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(''))
                codigos.append(row.codigo)
                cont += 1

        for i, row in enumerate(Vendedor.select()):
            habilitado = True
            if buscado in row.nombre:
                for code in codigos:
                    if code == row.codigo:
                        habilitado = False
                if habilitado:
                    self.ui.tablaProductos.insertRow(cont)
                    self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                    self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(f'C-{row.codigo.upper()}'))
                    self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(row.nombre.capitalize()))
                    self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(row.apellido.capitalize()))
                    self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(''))
                    codigos.append(row.codigo)
                    cont += 1

        for i, row in enumerate(Vendedor.select()):
            habilitado = True
            if buscado in row.apellido:
                for code in codigos:
                    if code == row.codigo:
                        habilitado = False
                if habilitado:
                    self.ui.tablaProductos.insertRow(cont)
                    self.ui.tablaProductos.setItem(cont, 0, QTableWidgetItem(str(row.id)))
                    self.ui.tablaProductos.setItem(cont, 1, QTableWidgetItem(f'C-{row.codigo.upper()}'))
                    self.ui.tablaProductos.setItem(cont, 2, QTableWidgetItem(row.nombre.capitalize()))
                    self.ui.tablaProductos.setItem(cont, 3, QTableWidgetItem(row.apellido.capitalize()))
                    self.ui.tablaProductos.setItem(cont, 4, QTableWidgetItem(''))
                    cont += 1


def eliminar_empleado(self):
    codigo = self.ui.tablaProductos.selectedIndexes()[1].data()[2:]
    for item in Vendedor.select().where(Vendedor.codigo == codigo.lower()):
        item.delete_instance()
    cargar_tabla_gestion_empleados(self)


def deleteAllRows(table: QTableWidget) -> None:
    model: QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())
