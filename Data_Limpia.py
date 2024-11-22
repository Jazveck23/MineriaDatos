import pandas as pd

#Archivo de Datalimpia para usarla posteriormente 
data = pd.read_csv('Carbon_(CO2)_Emissions_by_Country.csv')

data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y').dt.year
data.rename(columns={
    'Kilotons of Co2': 'Kilotons_CO2',
    'Metric Tons Per Capita': 'Metric_Tons_Per_Capita'
}, inplace=True)

# Eliminar valores nulos (NaN) en las columnas de interés
data_clean = data.dropna(subset=['Kilotons_CO2', 'Metric_Tons_Per_Capita'])