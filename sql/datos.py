from peewee import *
import datetime

db = SqliteDatabase('db.sqlite')

class Venta(Model):
    venta = AutoField(unique=True)
    codigo_vendedor = CharField()
    importe = CharField()
    fecha_registro = DateField(default=datetime.datetime.now())
    hora_registro = TimeField(default=datetime.datetime.now().time())

    class Meta:
        database = db
        db_table = 'ventas'

class Producto(Model):
    codigo = CharField(unique=True)
    descripcion = CharField()
    precio = CharField()
    stock = CharField()

    class Meta:
        database = db
        db_table = 'productos'

class Vendedor(Model):
    codigo = CharField(unique=True)
    nombre = CharField()
    apellido = CharField()
    edad = CharField()
    ventas = CharField()

    class Meta:
        database = db
        db_table = 'vendedores'

class N_factura(Model):
    numero = CharField()

    class Meta:
        database = db
        db_table = 'numero_facturas'

class Facturas(Model):
    numero = CharField()
    nombre_cliente = CharField()
    apellido_cliente = CharField()
    dni_cliente = CharField()
    telefono_cliente = CharField()
    direccion_cliente = CharField()
    importe_total = CharField()
    fecha_emision = CharField(default=datetime.date.today())

    class Meta:
        database = db
        db_table = 'facturas_emitidas'