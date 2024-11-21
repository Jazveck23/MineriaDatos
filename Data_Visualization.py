import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from Data_Limpia import data


# Se nos pide utilizar los siguientes graficos
plot_types = ['pie', 'histogram', 'boxplot', 'lineplot', 'scatterplot']



# Grafica de Pastel: Emisiones por Región
def pie():
    region_emissions = data.groupby('Region')['Kilotons_CO2'].sum().sort_values(ascending=False)
    plt.figure(figsize=(6, 6))
    region_emissions.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title('Distribución de Emisiones de CO2 por Región')
    plt.ylabel('')
    plt.savefig('Grafica de Pastel: Emisiones CO2 por Region.png')
    plt.show()
    plt.close()


# Histograma: Distribución de Emisiones Totales
def histogram():
    plt.figure(figsize=(8, 6))
    sns.histplot(data['Kilotons_CO2'], kde=True, color='skyblue', bins=20)
    plt.title('Distribución de Emisiones Totales de CO2')
    plt.xlabel('Kilotons de CO2')
    plt.ylabel('Frecuencia')
    plt.savefig('Histograma de total de Emisiones de CO2.png')
    plt.show()
    plt.close()


# Diagrama de Caja: Emisiones per cápita por Región
def box():
    plt.figure(figsize=(11, 7))
    sns.boxplot(x='Region', y='Metric_Tons_Per_Capita', data=data, palette='Set2')
    plt.title('Distribución de Emisiones per Cápita por Región')
    plt.xlabel('Región')
    plt.ylabel('Emisiones per Cápita')
    plt.xticks(rotation=45)
    plt.savefig('Diagrama de Caja: Emisiones CO2 per Capita.png')
    plt.show()
    plt.close()


# Grafico de Lineas: Emisiones Totales de CO2 por Año
def lineas():
    emissions_by_year = data.groupby('Date')['Kilotons_CO2'].sum()
    plt.figure(figsize=(11, 7))
    sns.lineplot(x=emissions_by_year.index, y=emissions_by_year.values, marker='o', color='darkgreen')
    plt.title('Emisiones Totales de CO2 por Año')
    plt.xlabel('Año')
    plt.ylabel('Kilotons de CO2')
    plt.savefig('Grafica de Lineas: Emisiones CO2 por año.png')
    plt.savefig('Grafica de Lineas: Emisiones CO2 por año.png')
    plt.show()
    plt.close()

# Diagrama de Dispersion: Relación entre Emisiones Totales y Emisiones per Cápita
def disper():
    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='Kilotons_CO2', y='Metric_Tons_Per_Capita', data=data, color='orange')
    plt.title('Relación entre Emisiones Totales y Emisiones per Cápita')
    plt.xlabel('Kilotons de CO2')
    plt.ylabel('Emisiones per Cápita (Metric Tons)')
    plt.savefig('Diagrama de Dispersion: Emisiones per Capita.png')
    plt.show()
    plt.close()

# Generar todos los gráficos usando un loop
for plot in plot_types:
    if plot == 'pie':
        pie()
    elif plot == 'histogram':
        histogram()
    elif plot == 'boxplot':
        box()
    elif plot == 'lineplot':
        lineas()
    elif plot == 'scatterplot':
        disper()