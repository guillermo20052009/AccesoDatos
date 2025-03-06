import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV
df = pd.read_csv("all_seasons.csv")

# Seleccionar solo las columnas necesarias
df = df[['pts', 'reb', 'season']]

# Filtrar los datos de entrenamiento hasta la temporada 2021-2022
df_train = df[df['season'] <= '2021-22']

# Filtrar los datos de prueba para la temporada 2022-2023
df_test = df[df['season'] == '2022-23']

x_train = df_train[['reb']]
y_train = df_train[['pts']]

x_test = df_test[['reb']]
y_test = df_test[['pts']]

modelo_lineal = LinearRegression()
modelo_lineal.fit(x_train, y_train)

y_pred = modelo_lineal.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f'RMSE con Regresión Lineal Simple (Predictor: Rebotes):{rmse:.2f}')

plt.figure(figsize=(10, 5))

# Datos reales (azul)
plt.scatter(df_test['reb'], y_test, color='blue', marker='o', label='Datos Reales')

# Predicción (naranja)
plt.scatter(df_test['reb'], y_pred, color='orange', marker='x', label='Predicción')

# Línea de tendencia
plt.plot(df_test['reb'], y_pred, linestyle='--', color='red', label='Tendencia')

# Configuración de la gráfica
plt.title('Regresión Lineal: Puntos vs. Rebotes')
plt.xlabel('Rebotes')
plt.ylabel('Puntos')
plt.grid(True)
plt.legend()
plt.show()