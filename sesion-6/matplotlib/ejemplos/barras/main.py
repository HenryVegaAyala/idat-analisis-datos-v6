import matplotlib.pyplot as plt
import numpy as np

ciudades = ["Lima", "Cusco", "Arequipa"]
valores = [500, 300, 450]

barras = plt.bar(ciudades, valores, color=["red", "blue", "green"])

plt.title("Ventas por ciudad", fontsize = 16, fontweight = "bold")
plt.xlabel("Ciudad")
plt.ylabel("Ventas")

# Agregar valores encima de cada barra
for barra in barras:
    altura = barra.get_height()
    plt.text(
        barra.get_x() + (barra.get_width() / 2),
        altura + 5,
        f"{altura}",
        ha="center",
        fontsize = 11,
    )

# Linea de tendencia
x = np.arange(len(ciudades))
coef = np.polyfit(x, valores, 1) # Ajuste lineal
tendencia = np.poly1d(coef)

plt.plot(
    x,
    tendencia(x),
    color="black",
    linestyle="--",
    linewidth=2,
    label="Linea de tendencia"
)

plt.xticks(x, ciudades)

plt.legend()

plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()