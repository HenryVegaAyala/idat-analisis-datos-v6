import pandas as pd

# Lectura del archivo CSV
data_csv = pd.read_csv("ventas_enero_csv.csv")

print(data_csv.head()) # Muestra las primeras 5 filas del archivo

# Lectura del archivo xlsx
data_xlsx = pd.read_excel("ventas_enero_excel.xlsx")

print(data_xlsx.head()) # Muestra las primeras 5 filas del archivo