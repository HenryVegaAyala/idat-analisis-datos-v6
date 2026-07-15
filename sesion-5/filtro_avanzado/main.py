import pandas as pd

data = pd.read_csv("dataset.txt")

# filtros condicionales
filtrado_por_tienda = data["Store ID"] == 8091
filtrado_por_unidades_vendidad = data["Units Sold"] > 100
filtrado_por_precio_total = data["Total Price"] >= 200

# Filtrar por 2 variables
resultado_filtrado = data[filtrado_por_tienda & filtrado_por_precio_total]
print(resultado_filtrado.info())

# Filtrar por 3 variables
resultado_filtrado_otros = data[filtrado_por_tienda & (filtrado_por_unidades_vendidad | filtrado_por_precio_total)]
print(resultado_filtrado_otros.info())