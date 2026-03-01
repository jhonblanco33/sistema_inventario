# test_almacen.py
from typing import List, Dict, Union

class Almacen:
    def __init__(self):
        
        self.articulos: List[Dict[str, Union[str, int, float]]] = []

    def agregar_item(self, descripcion: str, stock: int, costo: float) -> bool:
       
        if stock < 0 or costo < 0:
            return False
            
        item = {
            "descripcion": descripcion,
            "stock": stock,
            "costo": costo
        }
        self.articulos.append(item)
        return True

