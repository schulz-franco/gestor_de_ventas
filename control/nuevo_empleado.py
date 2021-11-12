from control.validacion import validacion
from sql.empleados import Vendedor


def agregar_empleado(self):
    codigo = self.nuevo_empleado.ui.input_codigo.text().lower()
    nombre = self.nuevo_empleado.ui.input_desc.text().lower()
    apellido = self.nuevo_empleado.ui.input_precio.text().lower()
    edad = self.nuevo_empleado.ui.input_stock.text()

    try:
        if codigo == '' or nombre == '' or apellido == '' or edad == '':
            self.mostrarError('Hay valores en blanco, por favor complete los datos')
            return
        if validacion(edad):
            Vendedor.create(
                codigo=codigo,
                nombre=nombre,
                apellido=apellido,
                edad=edad,
                ventas='0'
            )
            clear_inputs(self)
            self.nuevo_empleado.ui.input_codigo.setFocus()
        else:
            self.mostrarError('Solo se permiten valores numericos')
    except:
        self.mostrarError('Ya existe un empleado que posee ese codigo')


def clear_inputs(self):
    self.nuevo_empleado.ui.input_codigo.setText('')
    self.nuevo_empleado.ui.input_desc.setText('')
    self.nuevo_empleado.ui.input_precio.setText('')
    self.nuevo_empleado.ui.input_stock.setText('')
