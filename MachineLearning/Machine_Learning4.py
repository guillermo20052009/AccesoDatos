import pandas as pd
import matplotlib.pyplot as plt

# El dataset seguiremos usando el mismo ya que considero que tiene la información necesaria para realizar las operaciones
# predicciones que se requieren en este caso.
# Lectura del CSV
df = pd.read_csv("all_seasons.csv")

# La variable objetivo es "pts" (puntos), por lo que se debe separar del resto de variables.
correlation = df.corr(numeric_only=True)["pts"]
print(correlation.sort_values(ascending=False))

# Vamos a elegir como predictoras udg_pct, ast, reb.

# Identificar valores faltantes
print(df.isnull().sum())

# Identificar los valores erróneos
plt.figure(figsize=(12, 6))
plt.hist(df["ast"], bins=10, edgecolor="black", alpha=0.7)
plt.xlabel("Asistencias (AST)")
plt.ylabel("Frecuencia")
plt.title("Distribución de Asistencias en el Dataset de la NBA")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.yscale("log")
plt.annotate("Valor erróneo en 34", xy=(34, 1), xytext=(25, 10),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=12, color="red")
plt.show()

# Eliminar el valor erróneo en 'ast'
df_cleaned = df[df["ast"] != 34]

# Diagrama de caja de 'pts'
plt.figure(figsize=(8, 5))
plt.boxplot(df['pts'], vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.ylabel("Puntos (PTS)")
plt.title("Diagrama de Caja de Puntos en el Dataset de la NBA")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Eliminar valores de 'pts' mayores a 32
df_cleaned = df_cleaned[df_cleaned["pts"] <= 32]

# Guardar el dataset limpio
df_cleaned.to_csv("all_seasons_cleaned.csv", index=False)

# Verificar que se han eliminado los valores
print("Se han eliminado los valores mayores a 32 en la columna 'pts'.")
print(df_cleaned["pts"].describe())

# Nuevo diagrama de caja de 'pts' después de eliminar outliers
plt.figure(figsize=(8, 5))
plt.boxplot(df_cleaned['pts'], vert=True, patch_artist=True, boxprops=dict(facecolor="lightblue"))
plt.ylabel("Puntos (PTS)")
plt.title("Diagrama de Caja de Puntos en el Dataset Limpio")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
