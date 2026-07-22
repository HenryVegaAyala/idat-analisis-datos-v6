import pandas as pd
import numpy as np
import scipy.stats as st

df = pd.read_csv("tiempos_de_entrega.csv")

# Paso 1: Filtrado de datos en grupos
vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]

# Paso 2: Cálculo de la desviación estándar de cada grupo

# tradicional
promedio_tradicional = vehiculo_tradicional.mean()

ic_tradicional = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_tradicional) - 1,
    loc=promedio_tradicional,
    scale=st.sem(vehiculo_tradicional)
)

print(f"Rangos el intervalo de confianza con vehiculo tradicional")
print(f"Rango del vehiculo tradicional: {ic_tradicional[0]:.2f} - {ic_tradicional[1]:.2f}")
print(f"Promedio del vehiculo tradicional: {(ic_tradicional[0] + ic_tradicional[1]) / 2:.2f}")

print("-" * 100)

# eléctrico
promedio_electrico = vehiculo_electrico.mean()

ic_electrico = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_electrico) - 1,
    loc=promedio_electrico,
    scale=st.sem(vehiculo_electrico)
)

print(f"Rangos el intervalo de confianza con vehiculo eléctrico")
print(f"Rango del vehiculo eléctrico: {ic_electrico[0]:.2f} - {ic_electrico[1]:.2f}")
print(f"Promedio del vehiculo eléctrico: {(ic_electrico[0] + ic_electrico[1]) / 2:.2f}")

print("-" * 100)

# Paso 3: Prueba Test A/B
resultado = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)
print(f"Resultado del Test A/B: p-valor={resultado.pvalue:.4f}")

# Paso 4: Interpretación del resultado
if resultado.pvalue < 0.05:
    print(f"Existe una diferencia significativa entre ambos vehículos")
else:
    print(f"No existe una diferencia significativa entre ambos vehículos")
