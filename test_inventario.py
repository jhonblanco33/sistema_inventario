

from inventario import Almacen


def test_agregar_item():
    mi_almacen = Almacen()
    resultado = mi_almacen.agregar_item("Monitor 24 pulgadas", 12, 450.0)

    assert resultado == True
    assert mi_almacen.articulos[0]["descripcion"] == "Monitor 24 pulgadas"
    assert mi_almacen.articulos[0]["stock"] == 12
    assert mi_almacen.articulos[0]["costo"] == 450.0