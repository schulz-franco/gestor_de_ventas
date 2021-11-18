from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from sql.datos import Vendedor, Venta
from control.operaciones_productos import reducir_stock, buscar
import datetime

def cerrar_venta(self):
    if self.ui.carrito.item(0, 0) is not None:
        if self.ui.comboVendedor.currentText() == 'Empleado':
            self.mostrarError('Primero debe seleccionar un empleado para cerrar la venta')
        else:
            reducir_stock(self)
            fecha = self.gestion_ventas.ui.tablaProductos.item(1, 3)
            importe_venta(self)
            deleteAllRows(self.ui.carrito)
            buscar(self)
            if not fecha == datetime.date.today():
                cargar_venta(self)
            else:
                cargar_venta(self)


def cargar_venta(self):
    for row in Vendedor.select().where(Vendedor.nombre == (self.ui.comboVendedor.currentText()).lower()):
        row.ventas = int(row.ventas) + 1
        row.save()
        Venta.create(
            codigo_vendedor=row.codigo,
            importe=self.importe_total
        )
        self.importe_total = 0


def importe_venta(self):
    importe = 0
    for cont in range(self.ui.carrito.rowCount()):
        importe = importe + int(self.ui.carrito.item(cont, 5).text()[2:])
    self.ui.importe_de_venta.setText(f'TOTAL: $ {importe}')
    self.ui.importe_de_venta.show()


def deleteAllRows(table: QTableWidget) -> None:
    model:QAbstractTableModel = table.model()
    model.removeRows(0, model.rowCount())