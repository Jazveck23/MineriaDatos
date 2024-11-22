import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from Data_Limpia import data


# características para el agrupamiento
X = data[['Metric_Tons_Per_Capita', 'Kilotons_CO2']]

# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determinar el número óptimo de clústeres con el método del codo, se prueban de 2 a 12 clusters
inertia = []
for k in range(2, 13):  
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Mostrar los valores de inercia para decidir el número de clústeres
print("Valores de inercia para distintos k:")
print(inertia)

# Entrenar el modelo K-Means con el número óptimo de clústeres (supongamos k=3)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

# Predicciones y evaluación
data['Cluster'] = kmeans.labels_
silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
print(f"\nPuntuacion de Silueta: {silhouette_avg:.3f}")

# Información de los clusters
centroids = kmeans.cluster_centers_
print(f"Centroides de los clústeres:\n{centroids}")
print(f"\nDistribución de datos por clúster:\n{data['Cluster'].value_counts()}")