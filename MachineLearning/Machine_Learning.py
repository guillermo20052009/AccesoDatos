import pandas as pd

# Lectura del CSV
df = pd.read_csv("all_seasons.csv")

# ---------APARTADO 2-----------
print("---------APARTADO 2-----------\n")
print("Ejecutando comando para ver la estructura del DataFrame...\n")
print("\nEjecutamos el comando .shape\n")
print(df.shape)  # Muestra la forma del DataFrame (filas, columnas)
print("\nEjecutamos el comando .head()\n")
print(df.head())  # Muestra las primeras 5 filas
print("\nEjecutamos el comando .info()\n")
print(df.info())  # Información general sobre el DataFrame
print("\nEjecutamos el comando .describe()\n")
print(df.describe())  # Estadísticas descriptivas

# ---------APARTADO 3-----------
print("\n---------APARTADO 3-----------\n")
print("Seleccionando columnas relevantes: 'player_name', 'age', 'pts', 'ast'...\n")
puntos = df[["player_name", "age", "pts", "ast"]]
print(puntos.head())  # Muestra las primeras 5 filas de jugadores con puntuación y asistencias

# ---------APARTADO 4-----------
print("\n---------APARTADO 4-----------\n")
print("Calculando la eficiencia utilizando 'usg_pct' y 'ts_pct'...\n")
df['Eficiencia'] = (df['usg_pct'] * df['ts_pct']) / 2
Eficiencia = df[["player_name", "age", "pts", "ast", "Eficiencia"]]
print(Eficiencia.head())  # Muestra las primeras 5 filas con eficiencia calculada

# ---------APARTADO 5-----------
print("\n---------APARTADO 5-----------\n")
print("Filtrando jugadores con más de 25 puntos por partido...\n")
mas_de_25_pts = df[df["pts"] > 25]
anotadores = mas_de_25_pts[["player_name", "age", "pts", "ast"]]
print(anotadores.head())  # Muestra las primeras 5 filas de jugadores con más de 25 puntos

# ---------APARTADO 6-----------
print("\n---------APARTADO 6-----------\n")
print("Eliminando filas con valores nulos...\n")
df_limpio = df.dropna()
print(df.shape)  # Muestra la forma original del DataFrame
print(df_limpio.shape)  # Muestra la forma después de eliminar valores nulos

# ---------APARTADO 7-----------
print("\n---------APARTADO 7-----------\n")
print("Identificando y reemplazando valores nulos en 'college'...\n")
df_null = df[pd.isnull(df["college"])]
print(df_null.head())  # Muestra las primeras 5 filas con valores nulos en la columna 'college'
df["college"] = df["college"].fillna("ERA NULO")
df_arreglado = df[df["college"] == "ERA NULO"]
print(df_arreglado.head())  # Muestra las primeras 5 filas después de reemplazar valores nulos por "ERA NULO"

# ---------APARTADO 8-----------
print("\n---------APARTADO 8-----------\n")
print("Agrupando jugadores por equipo y contando puntos promedio...\n")
print("\nSolo agrupamos\n")
conteo_por_equipos = df.groupby("team_abbreviation").size()
print(conteo_por_equipos)  # Cuenta los jugadores por cada equipo
print("\nAgrupamos y sacamos promedio\n")
conteo_por_equipos_puntos = df.groupby("team_abbreviation")[["pts"]].mean()
print(conteo_por_equipos_puntos)  # Promedio de puntos por cada equipo


