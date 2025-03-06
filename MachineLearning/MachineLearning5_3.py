import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV
df = pd.read_csv("all_seasons.csv")

# Seleccionar solo las columnas necesarias
df = df[['pts', 'reb','ast','usg_pct', 'season']]

# Filtrar los datos de entrenamiento hasta la temporada 2021-2022
df_train = df[df['season'] <= '2021-22']

# Filtrar los datos de prueba para la temporada 2022-2023
df_test = df[df['season'] == '2022-23']

columnas_pred=['reb','ast','usg_pct']

x_train = df_train[['reb','ast','usg_pct']]
y_train = df_train[['pts']]

x_test = df_test[['reb','ast','usg_pct']]
y_test = df_test[['pts']]

modelo_rf = RandomForestRegressor(n_estimators=50,random_state=42)
modelo_rf.fit(x_train, y_train)

y_pred = modelo_rf.predict(x_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5

print(f'RMSE con Regresión Random Forest (Predictor: Rebotes, Asistencias y Porcenctaje de uso):{rmse:.2f}')


importancias = pd.Series(modelo_rf.feature_importances_,index=columnas_pred).sort_values(ascending=False)

print ("\n Importancia de las variables: ")
print (importancias)


plt.figure(figsize=(200,150))

# Datos reales (azul)
plt.scatter(y_test, df_test['reb'], color='blue', marker='o', label='Datos Reales')

# Predicción (naranja)
plt.scatter(y_pred, df_test['reb'], color='orange', marker='x', label='Predicción')
# Línea de tendencia


# Configuración de la gráfica
plt.title('Regresión Random Forest: Puntos vs. Rebotes')
plt.xlabel('Puntos')
plt.ylabel('Rebotes')
plt.grid(True)
plt.legend()
plt.show()