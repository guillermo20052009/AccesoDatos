import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

# Cargar el archivo CSV
df = pd.read_csv("all_seasons.csv")

# Seleccionar solo las columnas necesarias
df = df[['pts', 'reb', 'ast', 'usg_pct', 'season']]

# Filtrar los datos donde los puntos sean menores o iguales a 32
df = df[df["pts"] <= 32]

# Filtrar los datos de entrenamiento hasta la temporada 2021-2022
df_train = df[df['season'] <= '2021-22']

# Filtrar los datos de prueba para la temporada 2022-2023
df_test = df[df['season'] == '2022-23']

# Definir las columnas predictoras
columnas_pred = ['reb', 'ast', 'usg_pct']

# Variables de entrenamiento y prueba
x_train = df_train[columnas_pred]
y_train = df_train[['pts']]

x_test = df_test[columnas_pred]
y_test = df_test[['pts']]

# Crear y entrenar el modelo Lasso
modelo_lasso = Lasso(alpha=1.0)
modelo_lasso.fit(x_train, y_train)

# Realizar predicciones
y_pred = modelo_lasso.predict(x_test)

# Calcular el error cuadrático medio (RMSE)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

# Mostrar el RMSE
print(f'RMSE con Regresión Lasso (Predictor: Rebotes, Asistencias y Porcentaje de Uso): {rmse:.2f}')

# Obtener coeficientes y filtrar variables seleccionadas y eliminadas
coeficientes = pd.Series(modelo_lasso.coef_, index=columnas_pred)
variables_seleccionadas = coeficientes[coeficientes != 0].index.tolist()
variables_eliminadas = coeficientes[coeficientes == 0].index.tolist()

print("\nVariables seleccionadas por Lasso:")
print(variables_seleccionadas)

print("\nVariables eliminadas por Lasso:")
print(variables_eliminadas)

# Seleccionar solo 30 datos aleatorios de prueba para graficar
df_test_sample = df_test.sample(n=15, random_state=3)
x_test_sample = df_test_sample[['reb']]
y_test_sample = y_test.loc[df_test_sample.index]

# Obtener predicciones para los datos seleccionados
y_pred_sample = y_pred[df_test_sample.index.to_numpy() - df_test.index[0]]

# Ordenar los datos por rebotes para que la línea de tendencia sea clara
sorted_indices = np.argsort(x_test_sample['reb'].values.flatten())
x_sorted = x_test_sample.iloc[sorted_indices]
y_test_sorted = y_test_sample.iloc[sorted_indices]
y_pred_sorted = y_pred_sample[sorted_indices]

# Gráfica de comparación
plt.figure(figsize=(10, 5))

# Datos reales (azul)
plt.scatter(x_sorted, y_test_sorted, color='blue', marker='o', label='Datos Reales')

# Predicción (naranja)
plt.scatter(x_sorted, y_pred_sorted, color='orange', marker='x', label='Predicción')

# Línea de tendencia ordenada (rojo)
plt.plot(x_sorted, y_pred_sorted, linestyle='--', color='red', label='Tendencia')

# Configuración de la gráfica
plt.title('Regresión Lasso: Puntos vs. Rebotes (Muestra de 30 Datos)')
plt.xlabel('Rebotes')
plt.ylabel('Puntos')
plt.grid(True)
plt.legend()
plt.show()
