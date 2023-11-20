# Practica K means, aprendizaje no supervisado. 
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
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_Cleaned.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)

def get_cmap(n, name="hsv"):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name."""
    return plt.cm.get_cmap(name, n)

def data_dispersion_kmeans(df_csvChess, n_clusters=3):
    # Seleccionar las características relevantes para el clustering
    features = ['WhiteElo', 'BlackElo']
    data = df_csvChess[features]

    # Normalizar los datos
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Aplicar K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_csvChess['Cluster'] = kmeans.fit_predict(data_scaled)

    # Visualizar los resultados
    cmap = get_cmap(n_clusters)
    plt.figure(figsize=(12, 6))

    for i in range(n_clusters):
        cluster_subset = df_csvChess[df_csvChess['Cluster'] == i][:100]
        plt.scatter(cluster_subset['WhiteElo'], cluster_subset['BlackElo'], label=f"Cluster {i}", color=cmap(i), alpha=0.5)

    # Centroides
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='black', label='Centroids')

    plt.legend()
    plt.title(f'K-Means Clustering (primeras 100 filas, {n_clusters} clusters)')
    plt.xlabel('ELO Blancas')
    plt.ylabel('ELO Negras')
    plt.grid(True)
    plt.show()

# Llama a la función con tu conjunto de datos y el número deseado de clusters
data_dispersion_kmeans(df_csvChess, n_clusters=3)

# Filtrar datos para la primera semana de octubre
start_date = '2021.10.01'
end_date = '2021.10.07'
mask = (df_csvChess['Date'] >= start_date) & (df_csvChess['Date'] <= end_date)
df_october_week = df_csvChess[mask]

def get_cmap(n, name="hsv"):
    """Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name."""
    return plt.cm.get_cmap(name, n)

def data_dispersion_kmeans(df_csvChess, n_clusters=3):
    # Seleccionar las características relevantes para el clustering
    features = ['WhiteElo', 'BlackElo']
    data = df_csvChess[features]

    # Normalizar los datos
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Aplicar K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df_csvChess['Cluster'] = kmeans.fit_predict(data_scaled)

    # Visualizar los resultados
    cmap = get_cmap(n_clusters)
    plt.figure(figsize=(12, 6))

    for i in range(n_clusters):
        cluster_subset = df_csvChess[df_csvChess['Cluster'] == i][:100]
        plt.scatter(cluster_subset['WhiteElo'], cluster_subset['BlackElo'], label=f"Cluster {i}", color=cmap(i), alpha=0.5)

    # Centroides
    centroids = scaler.inverse_transform(kmeans.cluster_centers_)
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=200, color='black', label='Centroids')

    plt.legend()
    plt.title(f'K-Means Clustering (primeras 100 filas, {n_clusters} clusters)')
    plt.xlabel('ELO Blancas')
    plt.ylabel('ELO Negras')
    plt.grid(True)
    plt.show()

# Llama a la función con tu conjunto de datos filtrado y el número deseado de clusters
data_dispersion_kmeans(df_october_week, n_clusters=3)
