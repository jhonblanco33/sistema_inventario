# test_almacen.py
from typing import List, Dict, Optional, Union

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
    
    def consultar_item(self, descripcion: str) -> Optional[Dict[str, Union[str, int, float]]]:
        # Búsqueda real del artículo
        for item in self.articulos:
            if item["descripcion"] == descripcion:
                return item
        
        # Si termina el ciclo y no lo encuentra, retorna None
        return None
    
    def obtener_catalogo(self) -> List[Dict[str, Union[str, int, float]]]:
        return self.articulos