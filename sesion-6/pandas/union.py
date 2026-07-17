import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", None)

clientes = pd.read_csv("clientes.csv")
ventas = pd.read_csv("ventas.csv")
productos = pd.read_csv("productos.csv")

# union de ventas + clientes
resultado_union = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="inner", # Dentro de la intercepción
)

print(resultado_union)
print("=== Inner join: ventas + clientes ===")

resultado_left = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="left", # Mantener todas las filas de ventas
)
print(resultado_left)
print("=== LEFT join: ventas + clientes ===")

resultado_right = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="right", # Mantener todas las filas de clientes
)
print(resultado_right)
print("=== RIGHT join: ventas + clientes ===")

resultado_outer = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="outer", # Mantener todas las filas de ventas y clientes
)

print(resultado_outer[["id_venta", "fecha", "pais"]])
print("=== OUTER join: ventas + clientes ===")

# Union de 3 archivos
resultado_3_archivos = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="left"
)

resultado_3_archivos = pd.merge(
    resultado_3_archivos,
    productos,
    on="id_producto",
    how="right"
)

print(resultado_3_archivos)

resultado_3_archivos.to_csv("resultado_consolidado.csv", index=False)