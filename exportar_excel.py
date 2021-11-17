import openpyxl as xl
import easygui as eg
import shutil
import os

from sql.datos import Producto, Venta, Vendedor, Facturas

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
        elif self.nombre_hoja.lower() == 'facturas':
            self.hoja.append(('ID', 'Numero de factura', 'Nombre', 'Apellido', 'DNI', 'Telefono', 'Direccion', 'Importe', 'Fecha de emision'))
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
        elif modelo is Facturas:
            for row in modelo.select():
                self.hoja.append((str(row.id), row.numero, row.nombre_cliente, row.apellido_cliente, row.dni_cliente, row.telefono_cliente, row.direccion_cliente, row.importe_total, row.fecha_emision))
        else:
            print('Modelo de datos invalido')

    def ajustar_columnas(self, modelo):
        if modelo is Producto:
            self.hoja.column_dimensions["A"].width = 8
            self.hoja.column_dimensions["B"].width = 10
            self.hoja.column_dimensions["C"].width = 40
            self.hoja.column_dimensions["D"].width = 8
            self.hoja.column_dimensions["E"].width = 8
        elif modelo is Vendedor:
            self.hoja.column_dimensions["A"].width = 8
            self.hoja.column_dimensions["B"].width = 10
            self.hoja.column_dimensions["C"].width = 14
            self.hoja.column_dimensions["D"].width = 14
            self.hoja.column_dimensions["E"].width = 6
            self.hoja.column_dimensions["F"].width = 8
        elif modelo is Venta:
            self.hoja.column_dimensions["A"].width = 8
            self.hoja.column_dimensions["B"].width = 14
            self.hoja.column_dimensions["C"].width = 8
            self.hoja.column_dimensions["D"].width = 14
            self.hoja.column_dimensions["E"].width = 13
        elif modelo is Facturas:
            self.hoja.column_dimensions["A"].width = 8
            self.hoja.column_dimensions["B"].width = 20
            self.hoja.column_dimensions["C"].width = 14
            self.hoja.column_dimensions["D"].width = 14
            self.hoja.column_dimensions["E"].width = 14
            self.hoja.column_dimensions["F"].width = 14
            self.hoja.column_dimensions["G"].width = 25
            self.hoja.column_dimensions["H"].width = 12
            self.hoja.column_dimensions["I"].width = 16
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
    excel.ajustar_columnas(modelo)
    excel.guardar()
    if excel.mover() == 1:
        self.mostrarError('Se exporto el archivo con exito')

