

from inventario import Almacen

def test_agregar_item():
    mi_almacen = Almacen()
    

    assert mi_almacen.agregar_item("Monitor 24 pulgadas", 12, 450.0) == True
    assert len(mi_almacen.articulos) == 1
    

    assert mi_almacen.agregar_item("Teclado Dañado", -5, 20.0) == False

def test_modificar_stock():
    mi_almacen = Almacen()
    mi_almacen.agregar_item("Teclado Mecánico", 15, 80.0)
    mi_almacen.agregar_item("Mouse Inalámbrico", 10, 25.0)

    # Prueba de éxito
    assert mi_almacen.modificar_stock("Teclado Mecánico", 30) == True
    assert mi_almacen.articulos[0]["stock"] == 30
    
    # Pruebas de refactor (fallos intencionales)
    assert mi_almacen.modificar_stock("Teclado Mecánico", -5) == False 
    assert mi_almacen.modificar_stock("Pantalla Rota", 5) == False

def test_consultar_item():
    mi_almacen = Almacen()
    mi_almacen.agregar_item("Silla Ergonómica", 5, 120.5)
    mi_almacen.agregar_item("Escritorio de Madera", 2, 250.0)

    
    articulo_encontrado = mi_almacen.consultar_item("Silla Ergonómica")
    assert articulo_encontrado is not None
    assert articulo_encontrado["descripcion"] == "Silla Ergonómica"
    
   
    articulo_no_encontrado = mi_almacen.consultar_item("Lámpara LED")
    assert articulo_no_encontrado is None