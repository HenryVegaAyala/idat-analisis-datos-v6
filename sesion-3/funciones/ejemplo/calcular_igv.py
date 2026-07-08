def calcular_precio_final(precio_base: float):
    igv = 0.18
    impuesto = precio_base * igv
    return impuesto + precio_base


producto_a = calcular_precio_final(100)
print(f"Precio final del producto A: {producto_a}")

# Lista de precios de base
precios = [120, 150, 200, 500, 100000]

for precio in precios:
    resultado = calcular_precio_final(precio)
    print(f"Precio final del producto con precio base {precio} es igual a {resultado}")