archivos = [
    'control/cargar_cbo_empleados.py',
    'control/carrito.py',
    'control/crear_db.py',
    'control/editar_producto.py',
    'control/gestion_empleados.py',
    'control/gestion_facturas.py',
    'control/gestion_productos.py',
    'control/gestion_ventas.py',
    'control/nuevo_empleado.py',
    'control/nuevo_producto.py',
    'control/operaciones_productos.py',
    'control/operaciones_ventas.py',
    'control/validacion.py',
    'sql/datos.py',
    'admin_db.py',
    'exportar_excel.py',
    'generar_factura.py',
    'main.py',
]

def contar_lineas():
    cont = 0
    for i in range(len(archivos)):
        f = open(archivos[i], "r")
        for linea in f:
            cont += 1
        f.close()
    print(f'Total de {cont} lineas de codigo')

if __name__ == '__main__':

    contar_lineas()
