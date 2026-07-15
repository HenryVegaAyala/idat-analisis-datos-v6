import pandas as pd

data = pd.read_csv("ventas_enero_csv.csv")

# Eliminar por columna
data.drop("vendedor", axis=1, inplace=True)
print(data)

# Eliminar por fila
data.drop(0, axis=0, inplace=True)
print(data)