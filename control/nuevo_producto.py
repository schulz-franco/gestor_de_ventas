from control.validacion import validacion
from sql.productos import Producto

def agregar_producto(self):
    codigo = self.ui.input_codigo.text()
    descripcion = self.ui.input_desc.text()
    precio = self.ui.input_precio.text()
    stock = self.ui.input_stock.text()

    if validacion(precio) == True and validacion(stock) == True:
        Producto.create(
            codigo=codigo,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )

        clear_inputs(self)
        self.ui.input_codigo.setFocus()

def clear_inputs(self):
    self.ui.input_codigo.setText('')
    self.ui.input_desc.setText('')
    self.ui.input_precio.setText('')
    self.ui.input_stock.setText('')