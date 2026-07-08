def calcular_precio_final(precio_base):
    igv = 0.18
    impuesto = precio_base * igv
    return impuesto + precio_base


producto_a = calcular_precio_final(100)
print(f"Precio final del producto A: {producto_a}")

# Lista de precios de base
lista = [120, 150, 200, 500, 100000]

for item in lista:
    producto = calcular_precio_final(item)
    print(f"Precio final del producto con precio base {item}: {producto}")