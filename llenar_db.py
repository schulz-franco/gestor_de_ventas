from sql.empleados import Vendedor
from sql.productos import Producto

for i in range(350):
    Vendedor.create(
        codigo='1c' + str(i),
        nombre='example' + str(i),
        apellido='example' + str(i),
        edad='30'
    )
    Producto.create(
        codigo='1f' + str(i),
        descripcion='example' + str(i),
        precio='50',
        stock='50'
    )