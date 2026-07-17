import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2, figsize=(12, 8)) # Configuración base
fig.suptitle("Ejemplo de subplots con Matplotlib", fontsize=16)

# ----- Grafico 1: Lineal ------
ventas = [10, 20, 30, 50]
axs[0, 0].plot(ventas)
axs[0, 0].set_title("Ventas")

# ----- Grafico 2: Barras ------
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
ventas = [150, 200, 180, 220, 170]

axs[0, 1].bar(dias, ventas, color="orange", edgecolor="black")
axs[0, 1].set_title("Ventas del día")
axs[0, 1].set_xlabel("Día")
axs[0, 1].set_ylabel("Ventas")

# ----- Grafico 3: Barras ------
ventas = [150, 200, 180, 220, 170]

axs[1, 0].hist(ventas, bins=50, color="red", edgecolor="black")
axs[1, 0].set_title("Histograma de Ventas")
axs[1, 0].set_xlabel("Ventas")
axs[1, 0].set_ylabel("Frecuencia")


plt.grid(True, linestyle="--", alpha=0.5)

# plt.show()
plt.savefig("cuadro de reporte.png")