# Hacer uso de las gráficas para poder detectar patrones o información 
# relevante 
# Francisco Alejandro Pérez Garza 1896612


import pandas as pd
import os 
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import calendar

# Se debe de obtener el Dataset que modificaremos
Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_Cleaned.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)

csv_path2 = os.path.join(Carpeta_Trabajo, '..', 'Chess_WinsGenerales.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess_victorias = pd.read_csv(csv_path2)

# Asegurarse de que la columna 'Date' sea de tipo datetime
df_csvChess['Date'] = pd.to_datetime(df_csvChess['Date'])

# Extraer el mes de la columna 'Date' y crear una nueva columna 'Mes'
df_csvChess['Mes'] = df_csvChess['Date'].dt.month

# Calcular la media del campo 'WhiteElo' por mes
estadisticas_por_mes_White = df_csvChess.groupby('Mes')['WhiteElo'].mean()
# Calcular la media del campo 'WhiteElo' por mes
estadisticas_por_mes_Black = df_csvChess.groupby('Mes')['BlackElo'].mean()

# Crear un gráfico de barras para mostrar las estadísticas por mes
estadisticas_por_mes_White.plot(kind='line', figsize=(10, 6), color='red')
estadisticas_por_mes_Black.plot(kind='line', figsize=(10, 6), color= 'blue')
plt.xlabel('Mes')
plt.ylabel('Media del Elo ')
plt.title('Media del Elo por Mes')
plt.xticks(range(1, 13), calendar.month_abbr[1:])  # Etiquetas de los meses
plt.show()

