import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from Data_Limpia import data


# Crear una columna de clasificación: "Alta" o "Baja" emisión en de acuerdo a la mediana
threshold = data['Kilotons_CO2'].median()
data['Nivel_Emision'] = np.where(data['Kilotons_CO2'] > threshold, 'Alta', 'Baja')

# Convertir variables categóricas como la region en numéricas
le = LabelEncoder()
data['Region_codificada'] = le.fit_transform(data['Region'])

# Seleccionar las características (X) y la variable objetivo (y)
X = data[['Metric_Tons_Per_Capita', 'Region_codificada']]
y = data['Nivel_Emision']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos para que tengan una escala uniforme
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Creacion y entrenmiento del modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)  # Usamos k=5 vecinos
knn.fit(X_train, y_train)

# Realizar predicciones
y_pred = knn.predict(X_test)

# Evaluacion del modelo
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))