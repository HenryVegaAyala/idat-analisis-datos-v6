import pandas as pd

data = pd.read_csv("ventas_enero_csv.csv")

data.rename(columns={"id_venta": "id"}, inplace=True)

print(data)