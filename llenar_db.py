from sql.empleados import Vendedor
from sql.productos import Producto

for i in range(15):
    Vendedor.create(
        codigo='1c' + str(i),
        nombre='example' + str(i),
        apellido='example' + str(i),
        edad='30',
        ventas='0'
    )