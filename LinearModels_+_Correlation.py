import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from Data_Limpia import data


# Eliminar valores nulos (NaN) en las columnas de interés
data_clean = data.dropna(subset=['Kilotons_CO2', 'Metric_Tons_Per_Capita'])

# Seleccionar las variables independientes (X) y dependiente (y)
X = data_clean[['Metric_Tons_Per_Capita']]  # Variable independiente
y = data_clean['Kilotons_CO2']  # Variable dependiente

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular el R² (coeficiente de determinación)
r2 = r2_score(y_test, y_pred)

# Calcular el error cuadrático medio (opcional)
mse = mean_squared_error(y_test, y_pred)

# Mostrar el R² y el MSE
print("R² (Coeficiente de determinación):", r2)
print("Mean Squared Error (MSE):", mse)

# Graficar la recta de regresión
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Datos reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Recta de regresión')
plt.title('Regresión Lineal: Emisiones de CO₂ vs Emisiones per Cápita')
plt.xlabel('Emisiones per Cápita (Metric Tons)')
plt.ylabel('Emisiones de CO₂ (Kilotons)')
plt.legend()
plt.savefig('Grafica_Regresion_Lineal.png')  
plt.show()

# Graficar la distribución de residuos
residuals = y_test - y_pred
plt.figure(figsize=(8, 6))
sns.histplot(residuals, kde=True, color='green', bins=20)
plt.title('Distribución de los Residuos (Errores)')
plt.xlabel('Residuos')
plt.ylabel('Frecuencia')
plt.savefig('Distribucion_Residual.png')  
plt.show()