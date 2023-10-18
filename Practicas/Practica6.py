import pandas as pd
import os 
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import calendar
import statsmodels.api as sm
from statsmodels.formula.api import ols


Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_Cleaned.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)

# Asegurarse de que la columna 'Date' sea de tipo datetime
df_csvChess['Date'] = pd.to_datetime(df_csvChess['Date'])

# Extraer el mes de la columna 'Date' y crear una nueva columna 'Mes'
df_csvChess['Mes'] = df_csvChess['Date'].dt.month

# Se quieren obtener los resultados por mes, para determinar el comportamiento de las victorias blancas
# para eso, hay que agrupar los datos por meses para tener un mejor control de las partidas
results_by_month = df_csvChess.groupby('Mes')['Result'].value_counts(normalize=True).unstack()

X = sm.add_constant(results_by_month.index)
y = results_by_month['1-0'] 

model = sm.OLS(y, X).fit()

print(model.summary())

# Datos del Dataset  
x = results_by_month.index
y_real = results_by_month['1-0']

# Gráfico de dispersión
plt.scatter(x, y_real, label='Datos partidas blancas', color='blue')

# Añadir la línea de regresión
plt.plot(x, model.fittedvalues, label='Regresión lineal', color='red')

plt.xlabel('Mes')
plt.ylabel('Proporción de partidas ganadas por las blancas')
plt.legend()
plt.title('Regresión Lineal de los Resultados de las Partidas de Ajedrez por Mes')
plt.show()

# --------------------------------------------------------------------------------------------------

#ToDo: Hacer que funcione jajaja 

# Utilizar un filtro para saber el comportamiento de las victorias blancas en base a una apertura 

# Primero debemos de agrupar los datos de tal manera para que se junten los del ECO y resultado deseado 
"""""
results_by_eco_WW = df_csvChess.groupby('ECO')['Result'].value_counts(normalize=True).unstack()

apertura_seleccionada = 'C20'
sub_data = df_csvChess[df_csvChess['ECO'] == apertura_seleccionada]

X = sm.add_constant(sub_data.index)
y = results_by_eco_WW.loc[apertura_seleccionada]['1-0']

model = sm.OLS(y, X).fit()

print(model.summary())

"""