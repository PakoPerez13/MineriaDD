import kaggle 
import os

def get_csv_kaggle ():
    kaggle.api.authenticate()
    kaggle.api.dataset_download_files('https://www.kaggle.com/datasets/medaxone/fics-chess-dataset-2021')

df= get_csv_kaggle()