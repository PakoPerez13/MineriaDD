# Aplicar la estadistica descriptiva que nos ayudará a obtener datos que nos ayudarán a encontrar 
# patrones que nos llamen la atención de las partidas de ajedrez jugadas. 

import pandas as pd
import os 
import numpy as np
from tabulate import tabulate

# Se debe de obtener el Dataset que modificaremos
Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess_cleaned.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)


#Haremos funciones para determinar la cantida de partidas que ganaron las blancas, negras e hicieron tablas/empates
def Calculate_Win_Draw_Counts(df: pd.DataFrame) -> pd.DataFrame:
    white_wins = df[df['Result'] == '1-0'].shape[0]
    black_wins = df[df['Result'] == '0-1'].shape[0]
    draws = df[df['Result'] == '1/2-1/2'].shape[0]
    VT = draws + white_wins + black_wins
    
    # Uso de counts para poder obtener las estadisticas de victorias o tablas/empates
    result_counts = pd.DataFrame({
        'Victorias Blancas': [white_wins],
        'Victorias Negras': [black_wins],
        'Empates': [draws], 
        'Victorias Totales': [VT]
    })
    
    return result_counts 

def Calculate_Sicilian_Wins(df: pd.DataFrame) -> pd.DataFrame:
    Sicilian_Wins = df[(df['Result'] == '0-1') & (df['ECO'] == 'B23')].shape[0]
       
    results_counts = pd.DataFrame({
        'Victorias con la Siciliana': [Sicilian_Wins]
    })
    return results_counts

# def Calculate_most_played(df: pd.DataFrame) -> pd.DataFrame :


# Calcular la cantidad de victorias y empates/tablas
resultados_Wins = Calculate_Win_Draw_Counts(df_csvChess)
resultados_sicilian = Calculate_Sicilian_Wins(df_csvChess)

# Darle forma a la tabla con tabulate -> Para que se vea bonito claro que si
table = tabulate(resultados_Wins, headers='keys', tablefmt='pretty', showindex=False)
table_sicilian = tabulate(resultados_sicilian, headers='keys', tablefmt='pretty', showindex=False)

# Imprimir todon -> Para verificar los resultados
print(table)
print(table_sicilian)

df_resultados_Wins = pd.DataFrame(resultados_Wins)
df_resultados_Sicilian = pd.DataFrame(resultados_sicilian)

# Guarda la tabla de datos en formato CSV
df_resultados_Wins.to_csv(os.path.join(Carpeta_Trabajo, '..', 'Chess_WinsGenerales.csv'), index=False)
df_resultados_Sicilian.to_csv(os.path.join(Carpeta_Trabajo, '..', 'Chess_SicilianWins.csv'), index=False)


