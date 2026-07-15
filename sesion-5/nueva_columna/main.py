import pandas as pd

data = pd.read_csv("ventas_enero_csv.csv")

print(data.info())

data["total_venta"] = data["cantidad"] * data["precio_unitario"]

print(data.info())

print(data)