from sql.productos import Producto
from control.validacion import validacion


def cargar(self):
    datos_fila = []
    for i in range(5):
        datos_fila.append(self.gestion_productos.ui.tablaProductos.selectedIndexes()[i].data())
    self.editar_producto.ui.input_codigo.setText(datos_fila[1])
    self.editar_producto.ui.input_codigo.setEnabled(False)
    self.editar_producto.ui.input_desc.setText(datos_fila[2])
    precio = datos_fila[3][2:]
    self.editar_producto.ui.input_precio.setText(precio)
    self.editar_producto.ui.input_stock.setText(datos_fila[4])


def editar_producto(self):
    codigo = self.editar_producto.ui.input_codigo.text().lower()
    for row in Producto.select().where(Producto.codigo == codigo):
        if validacion(self.editar_producto.ui.input_precio.text()) == True and validacion(
                self.editar_producto.ui.input_stock.text()) == True:
            row.descripcion = self.editar_producto.ui.input_desc.text()
            row.precio = self.editar_producto.ui.input_precio.text()
            row.stock = self.editar_producto.ui.input_stock.text()
            row.save()
            self.editar_producto.close()
        else:
            self.mostrarError('Solo se permiten valores numericos')
