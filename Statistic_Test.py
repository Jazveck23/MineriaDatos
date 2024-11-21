from Data_Limpia import data
import scipy.stats as stats


# Análisis de varianza (ANOVA) para comparar emisiones entre diferentes regiones
anova_data = data[['Region', 'Kilotons_CO2']]

# Agrupar la data por región
data_region = [anova_data[anova_data['Region'] == region]['Kilotons_CO2'].dropna() 
                     for region in anova_data['Region'].unique()]

#ANOVA
#Si el p-value es menor que 0.05, podemos rechazar la hipótesis nula, indicando que las medias son diferentes entre regiones.
anova_resultado = stats.f_oneway(*data_region)
print("ANOVA resultado por emisiones de CO2 por region")
print("F-statistic:", anova_resultado.statistic)
print("P-value:", anova_resultado.pvalue)



# T-test: Comparación de emisiones de CO2 entre dos países (por ejemplo, China vs Mexico)
data_pais = data[data['Country'].isin(['China', 'Mexico'])][['Country', 'Kilotons_CO2']]
chin_data = data_pais [data_pais ['Country'] == 'China']['Kilotons_CO2']
Mexico_data = data_pais[data_pais ['Country'] == 'Mexico']['Kilotons_CO2']

# Realizar el T-test
# Si el p-value es menor que 0.05, podemos rechazar la hipótesis nula, indicando que las medias son diferentes entre los paises.
t_test_result = stats.ttest_ind(chin_data, Mexico_data)
print("\nT-test entre China y Mexico")
print("T-statistic:", t_test_result.statistic)
print("P-value:", t_test_result.pvalue)



# Kruskal-Wallis Test: Comparar las emisiones entre diferentes regiones sin asumir normalidad
kruskal = [anova_data[anova_data['Region'] == region]['Kilotons_CO2'].dropna() 
                for region in anova_data['Region'].unique()]

# Realizar el Kruskal-Wallis test
kruskal_result = stats.kruskal(*kruskal)
print("\nKruskal-Wallis Resultado para las emisiones de CO2 por region")
print("H-statistic:", kruskal_result.statistic)
print("P-value:", kruskal_result.pvalue)