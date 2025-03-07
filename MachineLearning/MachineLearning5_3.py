import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np

# Cargar el archivo CSV
df = pd.read_csv("all_seasons.csv")

# Seleccionar solo las columnas necesarias
df = df[['pts', 'reb', 'ast', 'usg_pct', 'season']]

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

# Crear y entrenar el modelo Random Forest
modelo_rf = RandomForestRegressor(n_estimators=50, random_state=42)
modelo_rf.fit(x_train, y_train.values.ravel())  # Ajuste para evitar advertencias

# Realizar predicciones
y_pred = modelo_rf.predict(x_test)

# Calcular el error cuadrático medio (RMSE)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

# Mostrar el RMSE
print(f'RMSE con Regresión Random Forest (Predictor: Rebotes, Asistencias y Porcentaje de Uso): {rmse:.2f}')

# Obtener la importancia de las variables
importancias = pd.Series(modelo_rf.feature_importances_, index=columnas_pred).sort_values(ascending=False)

print("\nImportancia de las variables:")
print(importancias)

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
plt.title('Regresión Random Forest: Puntos vs. Rebotes (Muestra de 30 Datos)')
plt.xlabel('Rebotes')
plt.ylabel('Puntos')
plt.grid(True)
plt.legend()
plt.show()
