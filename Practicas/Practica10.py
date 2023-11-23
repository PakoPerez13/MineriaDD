# Hacer una nube con todos los jugadores de las piezas blancas

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Nombre del archivo CSV
csv_file = 'Chess_cleaned.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(csv_file)

# Seleccionar la columna 'White' y unir los elementos en un solo string
all_words = " ".join(str(white) for white in df['White'])

# Crear la nube de palabras
wordcloud = WordCloud(
    background_color="white",
    width=1000,
    height=1000,
    max_font_size=100
).generate(all_words)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 10), facecolor=None, dpi=360)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)

# Guardar la nube de palabras como imagen
plt.savefig('../word_cloud.png', format='png', bbox_inches='tight', pad_inches=0, dpi=300)

plt.show()
