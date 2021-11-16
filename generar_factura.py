import shutil
import openpyxl as xl
import datetime
import easygui as eg
from sql.datos import Producto
from os import remove

hoja = ''
datos = ''

class Factura:
    def __init__(self):
        self.hoja = ''
        self.datos = []
        self.codigos = []
        self.unidades = []
        self.plantilla = xl.load_workbook('plantilla_factura.xlsx')
        self.hoja = self.plantilla.active

    def cargar_datos_cliente(self, modelo):
        nombre = str(modelo.ventana_datos_cliente.ui.input_nombre.text().capitalize())
        apellido = str(modelo.ventana_datos_cliente.ui.input_apellido.text().capitalize())
        dni = int(modelo.ventana_datos_cliente.ui.input_dni.text())
        telefono = int(modelo.ventana_datos_cliente.ui.input_telefono.text())
        direccion = str(modelo.ventana_datos_cliente.ui.input_direccion.text().lower())
        self.datos = [nombre, apellido, dni, telefono, direccion]

    def insertar_datos_cliente(self):
        self.hoja["B10"] = f'{self.datos[0]} {self.datos[1]}'
        self.hoja["B11"] = self.datos[2]
        self.hoja["B12"] = self.datos[4]
        self.hoja["B13"] = self.datos[3]

    def insertar_fecha(self):
        fecha = datetime.date.today()
        self.hoja["F10"] = str(fecha)
        self.hoja["F11"] = ''

    def obtener_codigos_venta(self, modelo):
        filas = int(modelo.ui.carrito.rowCount())
        self.codigos = []
        self.unidades = []
        for i in range(filas):
            self.codigos.append(modelo.ui.carrito.item(i, 0).text().lower())
            self.unidades.append(modelo.ui.carrito.item(i, 1).text())
        self.datos = [self.codigos, self.unidades]
        return self.datos

    def insertar_datos_productos(self, modelo):
        cantidad = len(self.datos[0])
        celda_inicio = 16
        for i in range(cantidad):
            for row in Producto.select().where(Producto.codigo == self.datos[0][i]):
                self.hoja[f"B{celda_inicio}"] = row.descripcion.lower()
                self.hoja[f"D{celda_inicio}"] = self.datos[1][i]
                self.hoja[f"E{celda_inicio}"] = int(row.precio)
                celda_inicio += 1

    def guardar(self):
        self.plantilla.save('factura.xlsx')

    def exportar(self):
        directorio_guardado = eg.diropenbox('Seleccionar directorio', 'Generando excel', 'C://')
        if directorio_guardado is not None:
            shutil.move('factura.xlsx', directorio_guardado)
            return 1
        else:
            remove('factura.xlsx')
            return 0

def exportar_factura(self):
    facturacion = Factura()
    facturacion.cargar_datos_cliente(self)
    facturacion.insertar_datos_cliente()
    facturacion.insertar_fecha()
    facturacion.obtener_codigos_venta(self)
    facturacion.insertar_datos_productos(self)
    facturacion.guardar()
    if facturacion.exportar() == 1:
        self.mostrarError('Factura creada con exito')