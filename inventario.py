# test_almacen.py
class Almacen:
    def __init__(self):
        self.articulos = []

    def agregar_item(self, descripcion, stock, costo):
        item = {
            "descripcion": descripcion,
            "stock": stock,
            "costo": costo
            
        }
        self.articulos.append(item)
        return True

