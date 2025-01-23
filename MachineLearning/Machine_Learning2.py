import pandas as pd

# ---------APARTADO 1-----------
print("---------APARTADO 1-----------\n")
print("Identificando y eliminando outliers en la columna 'pts' utilizando el método IQR...\n")
# Lectura del CSV
df = pd.read_csv("all_seasons.csv")
print(df.shape)  # Muestra la forma original del DataFrame

# Cálculo del IQR y límites
q1 = df["pts"].quantile(0.25)
q3 = df["pts"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print(f'lower_bound: {lower_bound} y upper_bound: {upper_bound}')  # Muestra los límites inferior y superior
df_outliers = df[(df["pts"] >= lower_bound) & (df["pts"] <= upper_bound)]
print(df_outliers.shape)  # Muestra la forma del DataFrame sin los outliers

# ---------APARTADO 2-----------
print("\n---------APARTADO 2-----------\n")
minimo = df_outliers["pts"].min()
maximo = df_outliers["pts"].max()

print(f'El mínimo es: {minimo} y el máximo es: {maximo}')  # Muestra el mínimo y máximo de la columna 'pts'

df_outliers["pts"] = (df_outliers["pts"] - minimo) / (maximo - minimo)
print(df_outliers[["player_name", "pts"]].head())  # Muestra los primeros valores normalizados de 'player_name' y 'pts'


# ---------APARTADO 3-----------
print("\n---------APARTADO 3-----------\n")


def rondaDraft(valor):
    if valor == "2":
        return "ronda 2"
    elif valor == "1":
        return "ronda 1"
    else: 
        return "undrafted"

df["draft_round"] = df["draft_round"].apply(rondaDraft)


print(df[["draft_round", "player_name"]].head(10))

df_encoded = pd.get_dummies(df, columns=["draft_round"],drop_first=False)
print(
    df_encoded[
        ["player_name", "draft_round_ronda 1", "draft_round_ronda 2", "draft_round_undrafted"]
    ].head(10)
)

# ---------APARTADO 4-----------
print("\n---------APARTADO 4-----------\n")

x=df[["pts","draft_number","age"]]
y=df["Pts_Partido"]

x=pd.get_dummies(x,columns=["draft_number"],drop_first=True)


# ---------APARTADO 5-----------
print("\n---------APARTADO 5-----------\n")


# ---------APARTADO 6-----------
print("\n---------APARTADO 6-----------\n")


# ---------APARTADO 7-----------
print("\n---------APARTADO 7-----------\n")

