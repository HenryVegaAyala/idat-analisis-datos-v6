import numpy as np

edades = np.array([10, 30, 15, 40, 45, 17, 55, 16])

# Filtrado por edad mayor o igual a 18
mayor_de_edad = edades >= 18
print(mayor_de_edad)

# Resultado es:
resultado = edades[mayor_de_edad] # Convertimos a una nueva lista filtrada
print(f"Edades mayores o iguales a 18: {resultado}")