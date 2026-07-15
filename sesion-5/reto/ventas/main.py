import pandas as pd

data = pd.read_excel("ventas_enero_2026_excel.xlsx")

filtro = data["precio_unitario"] > 1000 # Filtro de resultados

resultado = data[filtro] # Resultado Filtrado

print(resultado)