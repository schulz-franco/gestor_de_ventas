from PyQt5.QtWidgets import QApplication, QDialog

from interfaces.interfazAdmin import Ui_admin_db

from sql.productos import Producto, db
from sql.ventas import Venta
from sql.empleados import Vendedor

import sys

class interfaz_db_helper(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_admin_db()
        self.ui.setupUi(self)

        self.cargar_elementos_empleados()
        self.cargar_elementos_productos()
        self.cargar_elementos_ventas()

        self.ui.btn_agregar_carrito.clicked.connect(self.limpiar_tabla_productos)
        self.ui.btn_agregar_carrito_4.clicked.connect(self.limpiar_tabla_empleados)
        self.ui.btn_agregar_carrito_7.clicked.connect(self.limpiar_tabla_ventas)

        self.show()

    def cargar_elementos_productos(self):
        p_el = 0
        for row in Producto.select():
            p_el = str(row.id)
        self.ui.importe_de_venta_2.setText(str(p_el) + ' datos')

    def cargar_elementos_empleados(self):
        e_el = 0
        for row in Vendedor.select():
            e_el = str(row.id)
        self.ui.importe_de_venta_4.setText(str(e_el) + ' datos')

    def cargar_elementos_ventas(self):
        v_el = 0
        for row in Venta.select():
            v_el = str(row.venta)
        self.ui.importe_de_venta_6.setText(str(v_el) + ' datos')

    def limpiar_tabla_productos(self):
        if Producto.table_exists():
            Producto.truncate_table()
        else:
            Producto.create_table()

    def limpiar_tabla_empleados(self):
        if Vendedor.table_exists():
            Vendedor.truncate_table()
        else:
            Vendedor.create_table()

    def limpiar_tabla_ventas(self):
        if Venta.table_exists():
            Venta.truncate_table()
        else:
            Venta.create_table()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = interfaz_db_helper()
    application.show()
    sys.exit(app.exec_())