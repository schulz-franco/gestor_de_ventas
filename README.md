# sistema_gestion_comercial

Gestion de inventario, empleados, ventas y facturas

Practica de manejo de datos, se uso SQLite y Peewe como ORM. Tomar este proyecto solo como ejemplo de codigo.
Los paquetes requeridos son solicitados al momento de ejecutar.

Interfaz principal:

- Consulta de productos
- Filtrar por descripcion de producto
- Seleccion de un producto mediante doble click
- Ingreso de unidades a vender
- Ingreso de porcentaje de descuento a la venta del producto especifico
- Marcador para aplicar o no el impuesto al valor agregado (IVA)
- Agregar al carrito
- Limpiar el carrito
- Generar y registrar factura en base a los productos del carrito
- Importe total por producto en base a precio unitario, unidades, descuento y IVA
- Importe total de venta
- Seleccion del empleado que realiza la venta (carga mediante tabla de empleados)
- Cerrar y registrar la venta
- Descuento de stocks tras venta
- Carga de ventas realizadas por cada empleado
- Validaciones y trata de errores

Interfaz gestion de productos:

- Consulta de productos
- Filtrar por codigo o descripcion
- Añadir nuevo producto
- Seleccionar un producto
- Editar seleccionado
- Remover seleccionado
- Cargar stock indicado al producto seleccionado
- Exportar tabla de productos completa a un archivo Excel
- Validaciones y trata de errores

Interfaz gestion de empleados:

- Consulta de empleados
- Filtrar por codigo, nombre o apellido
- Añadir nuevo empleado
- Seleccionar empleado
- Remover seleccionado
- Ver mas informacion del seleccionado
- Exportar tabla de empleados a un archivo Excel
- Validaciones y trata de errores

Interfaz consulta de ventas:

- Consulta de ventas
- Filtrar por codigo de empleado o fecha (año, mes, dia o todos)
- Exportar registro de ventas a un archivo Excel

Interfaz consulta de facturas:

- Consulta de facturas
- Filtrar por nombre de cliente, apellido o fecha de emision (año, mes, dia o todos)
- Exportar registro de facturas a un archivo Excel
