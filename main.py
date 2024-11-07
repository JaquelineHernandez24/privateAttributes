from classVenta import Venta

venta = Venta()

venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente(" Jaqueline ")

# Diccionario de productos con cantidad y precio unitario
productos = {
    "Producto A": {"cantidad": 3, "precio": 12.00},
    "Producto B": {"cantidad": 4, "precio": 60.00},
    "Producto C": {"cantidad": 5, "precio": 45.00}
}

venta.set_productos(productos)

# Muestra el detalle de la venta
venta.mostrar_detalle()