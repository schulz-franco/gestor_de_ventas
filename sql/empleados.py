from peewee import *

db = SqliteDatabase('db.sqlite')


class Vendedor(Model):
    codigo = CharField(unique=True)
    nombre = CharField()
    apellido = CharField()
    edad = CharField()
    ventas = CharField()

    class Meta:
        database = db
        db_table = 'vendedores'


def cargar_comboVendedor(self):
    lista = []
    lista.append('Empleado')
    self.ui.comboVendedor.clear()
    for el in Vendedor.select():
        lista.append(el.nombre.capitalize())
    self.ui.comboVendedor.addItems(lista)
