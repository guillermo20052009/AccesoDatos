import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import pandas as pd
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV
df = pd.read_csv("all_seasons.csv")

# Seleccionar solo las columnas necesarias
df = df[['pts', 'reb','ast','usg_pct', 'season']]
df = df[df["pts"] <= 32]

# Filtrar los datos de entrenamiento hasta la temporada 2021-2022
df_train = df[df['season'] <= '2021-22']

# Filtrar los datos de prueba para la temporada 2022-2023
df_test = df[df['season'] == '2022-23']

columnas_pred=['reb','ast','usg_pct']

x_train = df_train[['reb','ast','usg_pct']]
y_train = df_train[['pts']]

x_test = df_test[['reb','ast','usg_pct']]
y_test = df_test[['pts']]

modelo_lasso = Lasso(alpha=1.0)
modelo_lasso.fit(x_train, y_train)

y_pred = modelo_lasso.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f'RMSE con Regresión Lasso (Predictor: Rebotes, Asistencias y Porcenctaje de uso):{rmse:.2f}')

coeficientes = pd.Series(modelo_lasso.coef_,index=columnas_pred)
variables_seleccionadas = coeficientes[coeficientes!=0].index.tolist()
variables_eliminadas = coeficientes[coeficientes==0].index.tolist()
print("\nVariables seleccionadas por lasso:")
print(variables_seleccionadas)

print("\nVariables eliminadas por lasso:")
print(variables_eliminadas)

plt.figure(figsize=(50,30))

# Datos reales (azul)
plt.scatter(df_test['reb'], y_test, color='blue', marker='o', label='Datos Reales')

# Predicción (naranja)
plt.scatter(df_test['reb'], y_pred, color='orange', marker='x', label='Predicción')

# Línea de tendencia
plt.plot(df_test['reb'], y_pred, linestyle='', color='red', label='Tendencia')

# Configuración de la gráfica
plt.title('Regresión Lasso: Puntos vs. Rebotes')
plt.xlabel('Rebotes')
plt.ylabel('Puntos')
plt.grid(True)
plt.legend()
plt.show()