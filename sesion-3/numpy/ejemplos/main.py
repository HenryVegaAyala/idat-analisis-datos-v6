import numpy as np

# lista de variables numéricas
ventas_diarias = [1500, 2300, 2100, 2500]

sumatoria_total = np.sum(ventas_diarias)
promedio = np.mean(ventas_diarias)
maximo_valor = np.max(ventas_diarias)

print(f"Sumatoria total: {sumatoria_total}")
print(f"Promedio: {promedio}")
print(f"Maximo valor: {maximo_valor}")