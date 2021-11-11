from sql.productos import Producto
from sql.ventas import Venta
from sql.empleados import Vendedor


def iniciar_db():
    if not Producto.table_exists():
        Producto.create_table()
    if not Venta.table_exists():
        Venta.create_table()
    if not Vendedor.table_exists():
        Vendedor.create_table()
