import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Cargar el dataset
data = pd.read_csv('Carbon_(CO2)_Emissions_by_Country.csv')


# Limpieza de datos
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y').dt.year
data.rename(columns={
    'Kilotons of Co2': 'Kilotons_CO2',
    'Metric Tons Per Capita': 'Metric_Tons_Per_Capita'
}, inplace=True)


print("Estadísticas descriptivas generales:")
print("")
print(data.describe())


# Agrupación por región: estadísticas agregadas
region = data.groupby('Region').agg({
    'Kilotons_CO2': ['sum', 'mean', 'max'],
    'Metric_Tons_Per_Capita': ['mean', 'max']
}).reset_index()
region.columns = ['Region', 'Total_CO2', 'Mean_CO2', 'Max_CO2', 'Mean_Per_Capita', 'Max_Per_Capita']
print("\nMuestra de Estadísticas (suma,media,valor maximo) por región:")
print(region.head())



# Agrupación por país: estadísticas agregadas
pais = data.groupby('Country').agg({
    'Kilotons_CO2': ['sum', 'mean', 'max'],
    'Metric_Tons_Per_Capita': ['mean', 'max']
}).reset_index()



pais.columns = ['Country', 'Total_CO2', 'Media_CO2', 'Max_CO2', 'Media_Per_Capita', 'Max_Per_Capita']
print("\nMuestra de Estadísticas (suma,media,valor maximo) por país:")
print(pais.head())

