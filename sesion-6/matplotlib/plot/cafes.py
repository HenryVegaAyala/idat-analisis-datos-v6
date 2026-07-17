import matplotlib.pyplot as plt
from pycparser import ply

horas = [1, 2, 3, 4]
cantidad = [10, 20, 25, 30]

plt.plot(horas, cantidad)
plt.title("Ventas de cafés por hora")
plt.xlabel("Hora del día")
plt.ylabel("Cantidad de cafés vendidos")
plt.show()
