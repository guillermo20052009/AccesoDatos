# Importando las bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split

# ---------APARTADO 1-----------
# Sección 1: Identificación y eliminación de outliers en la columna 'pts' utilizando el método IQR
print("---------APARTADO 1-----------\n")
print("Identificando y eliminando outliers en la columna 'pts' utilizando el método IQR...\n")

# Lectura del archivo CSV
df = pd.read_csv("all_seasons.csv")
print("Forma original del DataFrame:", df.shape)  # Mostrar la forma original del DataFrame

# Cálculo del IQR y límites
q1 = df["pts"].quantile(0.25)
q3 = df["pts"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f'Limite inferior: {lower_bound} y limite superior: {upper_bound}')  # Mostrar los límites inferior y superior
df_outliers = df[(df["pts"] >= lower_bound) & (df["pts"] <= upper_bound)]
print("Forma del DataFrame sin outliers:", df_outliers.shape)  # Mostrar la forma del DataFrame sin outliers

# ---------APARTADO 2-----------
# Sección 2: Normalización de la columna 'pts'
print("\n---------APARTADO 2-----------\n")
minimo = df_outliers["pts"].min()
maximo = df_outliers["pts"].max()

print(f'El mínimo es: {minimo} y el máximo es: {maximo}')  # Mostrar el mínimo y máximo de la columna 'pts'

df_outliers["pts"] = (df_outliers["pts"] - minimo) / (maximo - minimo)
print("Primeros valores normalizados de 'player_name' y 'pts':")
print(df_outliers[["player_name", "pts"]].head())  # Mostrar los primeros valores normalizados de 'player_name' y 'pts'

# ---------APARTADO 3-----------
# Sección 3: Codificación de la columna 'draft_round'
print("\n---------APARTADO 3-----------\n")

# Función para categorizar las rondas del draft
def rondaDraft(valor):
    if valor == "2":
        return "ronda 2"
    elif valor == "1":
        return "ronda 1"
    else: 
        return "undrafted"

df["draft_round"] = df["draft_round"].apply(rondaDraft)

print("Primeros 10 valores de 'draft_round' y 'player_name':")
print(df[["draft_round", "player_name"]].head(10))  # Mostrar los primeros 10 valores de 'draft_round' y 'player_name'

# Codificación one-hot de la columna 'draft_round'
df_encoded = pd.get_dummies(df, columns=["draft_round"], drop_first=False)
print("Primeros 10 valores de las columnas codificadas:")
print(
    df_encoded[
        ["player_name", "draft_round_ronda 1", "draft_round_ronda 2", "draft_round_undrafted"]
    ].head(10)
)  # Mostrar los primeros 10 valores de las columnas codificadas

# ---------APARTADO 4-----------
# Sección 4: Selección de características y variable objetivo
print("\n---------APARTADO 4-----------\n")

x = df[["usg_pct", "age"]]  # Características
y = df["pts"]  # Variable objetivo
print("Primeras 5 filas de las características:")
print(x.head())  # Mostrar las primeras 5 filas de las características
print("Primeras 5 filas de la variable objetivo:")
print(y.head())  # Mostrar las primeras 5 filas de la variable objetivo

# ---------APARTADO 5-----------
# Sección 5: División de los datos en conjuntos de entrenamiento y prueba
print("\n---------APARTADO 5-----------\n")

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Primeras 5 filas de las características de entrenamiento:")
print(x_train.head())  # Mostrar las primeras 5 filas de las características de entrenamiento
print("\nPrimeras 5 filas de las características de prueba:")
print(x_test.head())  # Mostrar las primeras 5 filas de las características de prueba
print("\nPrimeras 5 filas de la variable objetivo de entrenamiento:")
print(y_train.head())  # Mostrar las primeras 5 filas de la variable objetivo de entrenamiento
print("\nPrimeras 5 filas de la variable objetivo de prueba:")
print(y_test.head())  # Mostrar las primeras 5 filas de la variable objetivo de prueba

# ---------APARTADO 6-----------
# Sección 6: Creación de una nueva columna 'Gran_Anotador' basada en 'pts'
print("\n---------APARTADO 6-----------\n")

# Función para determinar si un jugador es un gran anotador
def gran_anotador(valor):
    if valor > 30:
        return "Anotador elite"
    elif valor > 20:
        return "Anotador Bueno"
    elif valor > 10:
        return "Anotador Promedio"
    else: 
        return "Anotador bajo"

df["Nivel_Anotador"] = df["pts"].apply(gran_anotador)

print("Primeros 10 valores de 'player_name', 'pts' y 'Gran_Anotador':")
print(df[["player_name", "pts", "Nivel_Anotador"]].head(10))  # Mostrar los primeros 10 valores de 'player_name', 'pts' y 'Gran_Anotador'

# ---------APARTADO 7-----------
# Sección 7: Filtrado y concatenación de datos para jugadores específicos
print("\n---------APARTADO 7-----------\n")

df_carmelo = df[df["player_name"] == "Carmelo Anthony"]
df_lebron = df[df["player_name"] == "LeBron James"]

print("DataFrame de Carmelo Anthony:")
print(df_carmelo.head())  # Mostrar las primeras 5 filas de los datos de Carmelo Anthony

print("\nDataFrame de LeBron James:")
print(df_lebron.head())  # Mostrar las primeras 5 filas de los datos de LeBron James

df_concatenated = pd.concat([df_carmelo, df_lebron])
print("\nDataFrame concatenado:")
print(df_concatenated.head())  # Mostrar las primeras 5 filas del DataFrame concatenado

df_concatenated = df_concatenated[["player_name", "season", "pts", "ast"]]
print("\nDataFrame concatenado con columnas seleccionadas:")
print(df_concatenated.head())  # Mostrar las primeras 5 filas de las columnas seleccionadas
print(df_concatenated.tail())  # Mostrar las últimas 5 filas de las columnas seleccionadas