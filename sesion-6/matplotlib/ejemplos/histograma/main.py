import matplotlib.pyplot as plt

edades = [18, 19, 21, 25, 26, 30, 34, 38, 40, 50]

plt.hist(edades, bins=5, edgecolor="black")

plt.title("Histograma de edades")
plt.xlabel("Edades")
plt.ylabel("Frecuencia")

plt.show()
