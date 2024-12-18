import pandas as pd

df=pd.read_csv("all_seasons.csv")

# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.describe())

# puntos=df[["player_name","age","pts","ast"]]
# print(puntos.head())

# df['Eficiencia'] = (df['usg_pct'] * df['ts_pct']) / 2
# Eficiencia=df[["player_name","age","pts","ast","Eficiencia"]]
# print(Eficiencia.head())

# mas_de_25_pts = df[df["pts"] > 25 ]
# anotadores=mas_de_25_pts[["player_name","age","pts","ast"]]
# print(anotadores.head())

# df_limpio = df.dropna()
# print(df.shape)
# print(df_limpio.shape)

# df_null = df[pd.isnull(df["college"])]
# print(df_null.head())
# df["college"] = df["college"].fillna("ERA NULO")
# df_arreglado = df[df["college"] == "ERA NULO"]
# print(df_arreglado.head())



