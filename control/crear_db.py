from sql.datos import Producto, Venta, Vendedor, N_factura

def iniciar_db():
    if not Producto.table_exists():
        Producto.create_table()
    if not Venta.table_exists():
        Venta.create_table()
    if not Vendedor.table_exists():
        Vendedor.create_table()
    if not N_factura.table_exists():
        N_factura.create_table()
        N_factura.create(numero='1')
