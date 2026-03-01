

from inventario import Almacen

def test_agregar_item():
    mi_almacen = Almacen()
    

    assert mi_almacen.agregar_item("Monitor 24 pulgadas", 12, 450.0) == True
    assert len(mi_almacen.articulos) == 1
    

    assert mi_almacen.agregar_item("Teclado Dañado", -5, 20.0) == False