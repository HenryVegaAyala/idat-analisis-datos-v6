import pandas as pd

# Configuración de ventana
pd.set_option("display.max_columns", None) # Va a mostrar todas las columnas
pd.set_option("display.max_rows", None) # Va a mostrar todas las filas
pd.set_option("display.width", None) # Se va autoajustar cada columna

data = pd.read_excel("ventas_enero_2026_excel.xlsx")

filtro = data["precio_unitario"] > 1000 # Filtro de resultados

resultado = data[filtro] # Resultado Filtrado

print(resultado)