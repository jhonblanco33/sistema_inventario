# test_almacen.py
from typing import List, Dict, Union

class Almacen:
    def __init__(self):
        self.articulos: List[Dict[str, Union[str, int, float]]] = []

    def agregar_item(self, descripcion: str, stock: int, costo: float) -> bool:
        if stock < 0 or costo < 0:
            return False
        item = {"descripcion": descripcion, "stock": stock, "costo": costo}
        self.articulos.append(item)
        return True

    def modificar_stock(self, descripcion: str, nuevo_stock: int) -> bool:
        # Validación: No permitir stock negativo
        if nuevo_stock < 0:
            return False
            
        # Buscar el artículo real y actualizarlo
        for item in self.articulos:
            if item["descripcion"] == descripcion:
                item["stock"] = nuevo_stock
                return True
                
    
        return False

