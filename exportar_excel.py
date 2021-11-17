import openpyxl as xl
import easygui as eg
import shutil
import os

from sql.datos import Producto, Venta, Vendedor

class Excel:
    def __init__(self, nombre_hoja):
        self.nombre_hoja = nombre_hoja

    def crear(self):
        self.archivo_excel = xl.Workbook()
        self.hoja = self.archivo_excel.active
        self.hoja.title = self.nombre_hoja.capitalize()

        if self.nombre_hoja.lower() == 'productos':
            self.hoja.append(('ID', 'Codigo', 'Descripcion', 'Precio', 'Stock'))
        elif self.nombre_hoja.lower() == 'empleados':
            self.hoja.append(('ID', 'Codigo', 'Nombre', 'Apellido', 'Edad', 'Ventas'))
        elif self.nombre_hoja.lower() == 'ventas':
            self.hoja.append(('ID', 'Cod. Empleado', 'Importe', 'Fecha de venta', 'Hora de venta'))
        else:
            print('Nombre de hoja invalido')

    def cargar(self, modelo):
        if modelo is Producto:
            for row in modelo.select():
                self.hoja.append((row.id, row.codigo.upper(), row.descripcion, row.precio, row.stock))
        elif modelo is Vendedor:
            for row in modelo.select():
                self.hoja.append((row.id, row.codigo.upper(), row.nombre.capitalize(), row.apellido.capitalize(), row.edad, row.ventas))
        elif modelo is Venta:
            for row in modelo.select():
                self.hoja.append((row.venta, row.codigo_vendedor.upper(), row.importe, row.fecha_registro, row.hora_registro))
        else:
            print('Modelo de datos invalido')

    def guardar(self):
        self.archivo_excel.save(f'{self.nombre_hoja.lower()}.xlsx')

    def mover(self):
        directorio_guardado = eg.diropenbox('Seleccionar directorio', 'Generando excel', 'C://')
        if directorio_guardado is not None:
            if not os.path.exists(f'{directorio_guardado}\{self.nombre_hoja.lower()}.xlsx'):
                shutil.move(f'{self.nombre_hoja.lower()}.xlsx', directorio_guardado)
            else:
                os.remove(f'{directorio_guardado}\{self.nombre_hoja.lower()}.xlsx')
                shutil.move(f'{self.nombre_hoja.lower()}.xlsx', directorio_guardado)
            return 1
        else:
            os.remove(f'{self.nombre_hoja.lower()}.xlsx')
            return 0

def generar_excel(self, nombre, modelo):
    excel = Excel(nombre)
    excel.crear()
    excel.cargar(modelo)
    excel.guardar()
    if excel.mover() == 1:
        self.mostrarError('Se exporto el archivo con exito')

