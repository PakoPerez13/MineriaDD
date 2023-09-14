# Limpiar los datos del DataSet 
# Francisco Alejandro Pérez Garza 

#El Dataset es de partidas de ajedrez

# Se eliminarán las columnas de movimientos repetidos, ya que no son necesarios 

import pandas as pd
import os 

# Se debe de obtener el Dataset que modificaremos
Carpeta_Trabajo = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(Carpeta_Trabajo, '..', 'Chess2021.csv') #El archvio debe de estar en el mismo nivel de la carpeta de "Practicas"
df_csvChess = pd.read_csv(csv_path)

# Eliminar las columnas con un movimiento individual
contador = 1
def delete_columns(df: pd.DataFrame) -> pd.DataFrame:
    global contador
    while contador <= 100:
           column_White = 'W' + str(contador)
           column_Black = 'B' + str(contador)
           try:
                df = df.drop(column_White, axis=1)
                df = df.drop(column_Black, axis=1)
           except KeyError:
                # Capturar la excepción si la columna no existe y continuar
                pass
           contador += 1
    return df

tupla = ['B', 'K', 'N', 'O', 'Q', 'R']
# Eliminar columnas de movimientos de piezas por color 
def delete_columns_pieces(df: pd.DataFrame) -> pd.DataFrame:
     global tupla
     for letra in tupla:
        column_White = 'W_' + letra + '_moves'
        column_Black = 'B_' + letra + '_moves'

        if column_White in df.columns:
            df.drop(columns=column_White, inplace=True)
        if column_Black in df.columns:
            df.drop(columns=column_Black, inplace=True)

     return df

# Se llaman las funcionalidadaes que se utilizarán y modificarán el dataset 
df_csvChess = delete_columns(df_csvChess)
df_csvChess = delete_columns_pieces(df_csvChess)

# Se guardará una copia en nuestra dataset limpia en la dirección que hagamos
df_csvChess.to_csv(os.path.join(Carpeta_Trabajo, '..', 'Chess_cleaned.csv'), index=False)
#Se adjunta tan la dataset limpia como la original 

#Solo se eliminaron datos repetidos, ya que es información redundante que se puede obtener de las columnas normalizadas.

