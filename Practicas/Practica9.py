import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

def filter_and_analyze_by_day(df, day_name):
    # Filtrar por el día de la semana deseado
    df_filtered = df[df['Date'].dt.day_name() == day_name]

    # Realizar el análisis de regresión lineal
    results_by_day = df_filtered.groupby('Date')['Result'].value_counts(normalize=True).unstack()

    X = sm.add_constant(results_by_day.index.dayofyear)
    y = results_by_day['1-0']

    model = sm.OLS(y, X).fit()

    # Obtener predicciones y intervalos de confianza
    predictions = model.get_prediction(X)
    pred_means = predictions.predicted_mean
    conf_int = predictions.conf_int()

    # Datos del Dataset
    x = results_by_day.index
    y_real = results_by_day['1-0']

    # Gráfico de dispersión
    plt.scatter(x, y_real, label=f'Datos partidas blancas ({day_name})', color='blue')

    # Añadir la línea de regresión
    plt.plot(x, model.fittedvalues, label='Regresión lineal', color='red')

    # Añadir franjas de confianza
    plt.fill_between(x, conf_int[:, 0], conf_int[:, 1], color='red', alpha=0.2, label='Intervalo de confianza (95%)')

    plt.xlabel(day_name)
    plt.ylabel('Proporción de partidas ganadas por las blancas')
    plt.legend()
    plt.title(f'Regresión Lineal de los Resultados de las Partidas de Ajedrez por {day_name} con Intervalo de Confianza')
    plt.show()

# Cargar el DataFrame desde el archivo CSV
Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_Cleaned.csv')
df_csvChess = pd.read_csv(csv_path)

# Convertir la columna 'Date' a tipo datetime
df_csvChess['Date'] = pd.to_datetime(df_csvChess['Date'])

# Llamar a la función con el día de la semana deseado (por ejemplo, 'Saturday')
filter_and_analyze_by_day(df_csvChess, 'Monday')
filter_and_analyze_by_day(df_csvChess, 'Saturday')
filter_and_analyze_by_day(df_csvChess, 'Sunday')
