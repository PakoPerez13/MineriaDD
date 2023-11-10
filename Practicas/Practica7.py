# K vecino más cercano - Programa 7 Minería de Datos 
# Francisco Alejandro Pérez Garza

import pandas as pd
import os 
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import calendar
import statsmodels.api as sm
from statsmodels.formula.api import ols
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder


Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_Cleaned.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)

# Obtener muestras aleatorias para simular los datos (limitado a un tamaño para la visualización)
data_subset = df_csvChess.sample(n=1000, random_state=42)

# Definir los ejes X e Y para el gráfico de dispersión
X = data_subset['WhiteElo']
Y = data_subset['BlackElo']

# Crear ruido aleatorio para efecto de dispersión
X += np.random.normal(0, 100, len(X))
Y += np.random.normal(0, 100, len(Y))

# Gráfico de dispersión simulado
plt.figure(figsize=(8, 6))
plt.scatter(X, Y, alpha=0.5)
plt.title('Simulación de Partidas de Ajedrez (ELO de Blancas vs ELO de Negras)')
plt.xlabel('ELO de Blancas')
plt.ylabel('ELO de Negras')
plt.grid(True)
plt.show()


data = pd.DataFrame({'WhiteElo': X, 'BlackElo': Y})  # Utilizando los datos simulados X e Y


data['Result'] = np.where(data['WhiteElo'] > data['BlackElo'], 1, 0)


X = data[['WhiteElo', 'BlackElo']]  
y = data['Result']  # Etiquetas

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar el clasificador KNeighbors
knn = KNeighborsClassifier(n_neighbors=5)  # Puedes ajustar el número de vecinos

# Entrenar el modelo
knn.fit(X_train, y_train)

# Predecir las etiquetas para los puntos
predicted = knn.predict(X)

# Colorear los puntos según su clasificación
plt.figure(figsize=(8, 6))
plt.scatter(X['WhiteElo'], X['BlackElo'], c=predicted, cmap='viridis', alpha=0.5)
plt.title('Clasificación de Partidas de Ajedrez')
plt.xlabel('ELO de Blancas')
plt.ylabel('ELO de Negras')
plt.colorbar(label='Grupo clasificado')
plt.grid(True)
plt.show()