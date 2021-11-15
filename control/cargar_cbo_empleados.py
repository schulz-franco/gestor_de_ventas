from sql.datos import Vendedor

def cargar_comboVendedor(self):
    lista = []
    lista.append('Empleado')
    self.ui.comboVendedor.clear()
    for el in Vendedor.select():
        lista.append(el.nombre.capitalize())
    self.ui.comboVendedor.addItems(lista)