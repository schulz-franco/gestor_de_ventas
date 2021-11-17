import shutil
import openpyxl as xl
import datetime
import easygui as eg
from sql.datos import Producto, N_factura, Facturas
import os

class Factura:
    def __init__(self):
        self.hoja = ''
        self.datos = []
        self.codigos = []
        self.unidades = []
        self.plantilla = xl.load_workbook('plantilla_factura.xlsx')
        self.hoja = self.plantilla.active

    def cargar_datos_cliente(self, modelo):
        self.nombre = str(modelo.ventana_datos_cliente.ui.input_nombre.text().capitalize())
        self.apellido = str(modelo.ventana_datos_cliente.ui.input_apellido.text().capitalize())

        try:
            self.dni = int(modelo.ventana_datos_cliente.ui.input_dni.text())
            self.telefono = int(modelo.ventana_datos_cliente.ui.input_telefono.text())
        except:
            modelo.mostrarError('Solo valores numericos')
            return 'error'

        self.direccion = str(modelo.ventana_datos_cliente.ui.input_direccion.text().lower())
        self.datos = [self.nombre, self.apellido, self.dni, self.telefono, self.direccion]

        for i in range(5):
            if self.datos[i] == '':
                modelo.mostrarError('Complete el formulario')
                return 'error'

    def insertar_datos_cliente(self):
        self.hoja["B10"] = f'{self.datos[0]} {self.datos[1]}'
        self.hoja["B11"] = self.datos[2]
        self.hoja["B12"] = self.datos[4]
        self.hoja["B13"] = self.datos[3]

    def insertar_fecha(self):
        fecha = datetime.date.today()
        self.hoja["F10"] = str(fecha)
        self.hoja["F11"] = ''

    def insertar_fecha_vencimiento(self):
        fecha = datetime.date.today()
        divido = str(fecha).split('-')
        if divido[1] == '12':
            sumo_año = str(int(divido[0]) + 1)
            fecha_final = f'{sumo_año}-{divido[1]}-{divido[2]}'
        else:
            sumo_mes = str(int(divido[1]) + 1)
            fecha_final = f'{divido[0]}-{sumo_mes}-{divido[2]}'
        self.hoja["F11"] = fecha_final

    def insertar_numero_factura(self):
        fecha = datetime.date.today()
        divido = str(fecha).split('-')
        for row in N_factura.select():
            self.numero = f'{divido[0]}{divido[1]}{divido[2]}{row.numero}'
            row.numero = str(int(row.numero) + 1)
            row.save()
        self.hoja["F9"] = self.numero

    def obtener_codigos_venta(self, modelo):
        filas = int(modelo.ui.carrito.rowCount())
        self.codigos = []
        self.unidades = []
        for i in range(filas):
            self.codigos.append(modelo.ui.carrito.item(i, 0).text().lower())
            self.unidades.append(modelo.ui.carrito.item(i, 1).text())
        self.datos = [self.codigos, self.unidades]

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

    def exportar(self, modelo):
        directorio_guardado = eg.diropenbox('Seleccionar directorio', 'Generando excel', 'C://')
        nombre = 'factura'
        if directorio_guardado is not None:
            if not os.path.exists(f'{directorio_guardado}\{nombre}.xlsx'):
                self.cargar_factura(modelo)
                shutil.move('factura.xlsx', directorio_guardado)
            else:
                self.cargar_factura(modelo)
                os.remove(f'{directorio_guardado}\{nombre}.xlsx')
                shutil.move('factura.xlsx', directorio_guardado)
            return 1
        else:
            os.remove('factura.xlsx')
            return 0

    def cargar_factura(self, modelo):
        importe = 0
        for cont in range(modelo.ui.carrito.rowCount()):
            importe = importe + int(modelo.ui.carrito.item(cont, 5).text()[2:])

        Facturas.create(
            numero=str(self.numero),
            nombre_cliente=self.nombre,
            apellido_cliente=self.apellido,
            dni_cliente=str(self.dni),
            telefono_cliente=str(self.telefono),
            direccion_cliente=str(self.direccion),
            importe_total=f'$ {importe}'
        )

def exportar_factura(self):
    facturacion = Factura()
    if facturacion.cargar_datos_cliente(self) != 'error':
        facturacion.insertar_datos_cliente()
        facturacion.insertar_fecha()
        facturacion.insertar_fecha_vencimiento()
        facturacion.insertar_numero_factura()
        facturacion.obtener_codigos_venta(self)
        facturacion.insertar_datos_productos(self)
        facturacion.guardar()
        if facturacion.exportar(self) == 1:
            self.mostrarError('Factura creada con exito')
    else:
        return 'invalido'