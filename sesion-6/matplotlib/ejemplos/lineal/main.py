import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("kilometros.csv")

semana = df["semana"]
kilometros = df["km"]

plt.plot(semana, kilometros)
plt.title("Progreso de Juan")
plt.xlabel("Semanas")
plt.ylabel("Kilómetros")

plt.show()