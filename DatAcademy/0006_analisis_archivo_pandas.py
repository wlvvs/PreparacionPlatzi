import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    
    df = pd.read_csv('./files/StudentsPerformance.csv')

    print('')
    print('Cabecera de .csv')
    print(df.head())
    print('')
    
    print('Número de registros y columnas')
    print(df.shape)
    print('')

    print('Nombre por columnas')
    print(df.columns)
    print('')

    print('Tipo de dato por columna')
    print(df.dtypes)
    print('')
    

if __name__ == '__main__':
    run()