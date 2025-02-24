import pandas as pd

#El dataset seguiremos usando el mismo ya que considero que tiene la información necesaria para realizar las operaciones
#predicciones que se requieren en este caso.
#Lectura del CSV
df = pd.read_csv("all_seasons.csv")



# La variable objetivo es "pts" (puntos), por lo que se debe separar del resto de variables.
correlation = df.corr(numeric_only=True)["pts"]
print(correlation.sort_values(ascending=False))
#Vamos a elegir como predictoras udg_pct,ast,reb.

#Identificar valores faltantes
print(df.isnull().sum())

#Identificar los valores erróneos

