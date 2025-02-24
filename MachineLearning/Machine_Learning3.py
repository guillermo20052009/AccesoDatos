import pandas as pd
import matplotlib.pyplot as plt

# ---------Grafico de lineas-----------
print("---------Grafico de lineas: Tendencia temporal-----------\n")
# Lectura del CSV
df = pd.read_csv("all_seasons.csv")

puntos = df.groupby("season")["ast"].max()

puntos.plot(title="Tendencia de máximo de asistencias por temporada", xlabel="Temporada", ylabel="Asistencias", color="red", figsize=(10, 25))
plt.show()
# ---------Grafico de dispersión: Rebotes defensivos vs ofensivos-----------
print("---------Grafico de dispersión: Rebotes defensivos vs ofensivos-----------\n")

df.plot.scatter(x="oreb_pct", y="dreb_pct", color="green", figsize=(10, 6))
plt.title("Relación entre Rebotes Ofensivos y Defensivos")
plt.show()

# ---------Grafico de barras: Puntos medios por temporada-----------
print("---------Grafico de barras: Puntos medios por temporada-----------\n")

puntos_medios = df.groupby("season")["pts"].sum()
puntos_medios.plot(kind="bar", title="Puntos medios por temporada", xlabel="Temporada", ylabel="Puntos", color="blue", figsize=(20, 10))
plt.show()

# ---------Histograma: Distribución de asistencias-----------
print("---------Histograma: Distribución de asistencias-----------\n")

df["ast"].plot(kind="hist", bins=30, color="purple", figsize=(10, 6))
plt.title("Distribución de asistencias")
plt.xlabel("Asistencias")
plt.ylabel("Frecuencia")
plt.show()


# ---------Diagrama de caja: Distribución de puntos-----------
print("---------Diagrama de caja: Distribución de puntos-----------\n")

df.boxplot(column="pts", figsize=(10, 6))
plt.title("Diagrama de caja de los puntos")
plt.ylabel("Puntos")
plt.show()