# Hacer uso de la podersa ANOVA 
# Francisco Alejandro Pérez Garza 1896612


import pandas as pd
import os 
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import calendar
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Declaración de archivo de trabajo
Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_Cleaned.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)

filtro = (df_csvChess['WhiteElo'] >= 1500) & (df_csvChess['WhiteElo'] <= 2000) & (df_csvChess['ECO'] == 'A04')
datos_filtrados = df_csvChess[filtro]

# Agregar otro filtro para utilizarlo adecuadamente

# Crear un rango de datos para aplicarlo

# Crear el boxplot con los datos filtrados
datos_filtrados.boxplot('WhiteElo', by='ECO')

# Mostrar el gráfico
plt.show()

new = ols('WhiteElo ~ ECO', data=datos_filtrados).fit()
an = sm.stats.anova_lm(new, type = 2)

print(an)
