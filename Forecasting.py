import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from Data_Limpia import data

# Asegurarse de que la columna Date sea numérica
data['Date'] = pd.to_numeric(data['Date'], errors='coerce')
data.dropna(subset=['Date'], inplace=True)

# Seleccionar las columnas necesarias
X = data[['Date']]  # Año como característica
y = data['Kilotons_CO2']  # Emisiones como objetivo

# Dividir en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Puntiacion de R2: {r2:.3f}")
print(f"Error Medio Cuadrático (MSE): {mse:.3f}")

# Predicción de nuevos datos (por ejemplo, años futuros)
años_futuros = pd.DataFrame({'Date': [2025, 2030, 2035, 2040]})
predicciones = model.predict(años_futuros)

print("\nPredicciones para años futuros:")
for year, pred in zip(años_futuros['Date'], predicciones):
    print(f"Año {year}: {pred:.2f} kilotoneladas de CO2")