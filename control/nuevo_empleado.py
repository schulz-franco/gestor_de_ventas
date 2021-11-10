from control.validacion import validacion
from sql.empleados import Vendedor

def agregar_empleado(self):
    codigo = self.ui.input_codigo.text()
    nombre = self.ui.input_desc.text().lower()
    apellido = self.ui.input_precio.text().lower()
    edad = self.ui.input_stock.text()

    if validacion(edad) == True:
        Vendedor.create(
            codigo=codigo,
            nombre=nombre,
            apellido=apellido,
            edad=edad
        )

        clear_inputs(self)
        self.ui.input_codigo.setFocus()
        return True
    else:
        return False

def clear_inputs(self):
    self.ui.input_codigo.setText('')
    self.ui.input_desc.setText('')
    self.ui.input_precio.setText('')
    self.ui.input_stock.setText('')