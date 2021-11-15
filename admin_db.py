from PyQt5.QtWidgets import QApplication, QDialog

from interfaces.interfazAdmin import Ui_admin_db

from sql.datos import Producto, Venta, Vendedor


import sys

class interfaz_db_helper(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = Ui_admin_db()
        self.ui.setupUi(self)

        self.mostrar_elementos(Producto, self.ui.importe_de_venta_2)
        self.mostrar_elementos(Vendedor, self.ui.importe_de_venta_4)
        self.mostrar_elementos(Venta, self.ui.importe_de_venta_6)

        self.ui.btn_agregar_carrito.clicked.connect(self.limpiar_tabla_productos)
        self.ui.btn_agregar_carrito_4.clicked.connect(self.limpiar_tabla_empleados)
        self.ui.btn_agregar_carrito_7.clicked.connect(self.limpiar_tabla_ventas)

        self.ui.btn_agregar_carrito_2.clicked.connect(self.cargar_productos)
        self.ui.btn_agregar_carrito_6.clicked.connect(self.cargar_empleados)
        self.ui.btn_agregar_carrito_9.clicked.connect(self.cargar_ventas)

        self.show()

    def cargar_productos(self):
        try:
            for i in range(int(self.ui.input_productos.text())):
                Producto.create(
                    codigo='1c' + str(i),
                    descripcion='texto_de_descripcion' + str(i),
                    precio='200',
                    stock='50'
                )
            self.mostrar_elementos(Producto, self.ui.importe_de_venta_2)
        except:
            pass

    def cargar_empleados(self):
        try:
            for i in range(int(self.ui.input_empleados.text())):
                Vendedor.create(
                    codigo='1f' + str(i),
                    nombre='example' + str(i),
                    apellido='example' + str(i),
                    edad='25',
                    ventas='0'
                )
            self.mostrar_elementos(Vendedor, self.ui.importe_de_venta_4)
        except:
            pass

    def cargar_ventas(self):
        try:
            for i in range(int(self.ui.input_ventas.text())):
                Venta.create(
                    codigo_vendedor='example' + str(i),
                    importe='250',
                )
            self.mostrar_elementos(Venta, self.ui.importe_de_venta_6)
        except:
            pass

    def mostrar_elementos(self, modelo, objeto):
        p_el = 0
        for row in modelo.select():
            try:
                p_el = str(row.id)
            except:
                p_el = str(row.venta)
        objeto.setText(str(p_el) + ' datos')

    def limpiar_tabla_productos(self):
        if Producto.table_exists():
            Producto.truncate_table()
        else:
            Producto.create_table()
        self.mostrar_elementos(Producto, self.ui.importe_de_venta_2)

    def limpiar_tabla_empleados(self):
        if Vendedor.table_exists():
            Vendedor.truncate_table()
        else:
            Vendedor.create_table()
        self.mostrar_elementos(Vendedor, self.ui.importe_de_venta_4)

    def limpiar_tabla_ventas(self):
        if Venta.table_exists():
            Venta.truncate_table()
        else:
            Venta.create_table()
        self.mostrar_elementos(Venta, self.ui.importe_de_venta_6)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    application = interfaz_db_helper()
    application.show()
    sys.exit(app.exec_())