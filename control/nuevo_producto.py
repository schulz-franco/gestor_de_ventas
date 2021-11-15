from control.validacion import validacion
from sql.datos import Producto


def agregar_producto(self):
    codigo = self.nuevo_producto.ui.input_codigo.text().lower()
    descripcion = self.nuevo_producto.ui.input_desc.text().lower()
    precio = self.nuevo_producto.ui.input_precio.text()
    stock = self.nuevo_producto.ui.input_stock.text()
    if codigo == '' or descripcion == '' or precio == '' or stock == '':
        self.mostrarError('Hay valores en blanco, por favor complete los datos')
        return
    try:
        if validacion(precio) == True and validacion(stock) == True:
            Producto.create(
                codigo=codigo,
                descripcion=descripcion,
                precio=precio,
                stock=stock
            )
            clear_inputs(self)
            self.nuevo_producto.ui.input_codigo.setFocus()
        else:
            self.mostrarError('Solo valores numericos en precio y stock')
    except:
        self.mostrarError('Ya existe un producto que posee ese codigo')


def clear_inputs(self):
    self.nuevo_producto.ui.input_codigo.setText('')
    self.nuevo_producto.ui.input_desc.setText('')
    self.nuevo_producto.ui.input_precio.setText('')
    self.nuevo_producto.ui.input_stock.setText('')
