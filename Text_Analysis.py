from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from Data_Limpia import data



# Unir datos de texto en una sola cadena como la columna 'Region' contiene texto
text_data = " ".join(str(region) for region in data['Region'].dropna())

# Opcional: Añadir palabras irrelevantes (conocidas como stop words) adicionales
stop_words = set(STOPWORDS)
stop_words.update(["ejemplo", "pais", "region", "palabra"])  # Agregar palabras irrelevantes

# Crear la nube de palabras
wordcloud = WordCloud(
    width=800, 
    height=400, 
    background_color='white', 
    stopwords=stop_words, 
    colormap='viridis', 
    max_words=200
).generate(text_data)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Eliminar ejes
plt.title("Word Cloud de Regiones", fontsize=16)
plt.show()

# Guardar la nube de palabras en un archivo
wordcloud.to_file("wordcloud.png")