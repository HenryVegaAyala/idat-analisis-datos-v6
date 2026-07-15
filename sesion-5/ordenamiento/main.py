import pandas as pd

# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# pd.set_option("display.width", None)

data = pd.read_excel("ventas_enero_2026_excel.xlsx")

# print(data.info())

# ordenamiento de menor a mayor
orden_data_1 = data.sort_values("vendedor")
print(orden_data_1)

print("*" * 200)

# ordenamiento de mayor a menor
orden_data_2 = data.sort_values("vendedor", ascending=False)
print(orden_data_2)

print("-" * 200)

orden_multiple = data.sort_values(["vendedor", "producto"], ascending=[False, True])
print(orden_multiple)