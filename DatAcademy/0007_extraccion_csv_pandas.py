'''
Aquí se genera una tabla de frecuencias
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    
    df = pd.read_csv('./files/StudentsPerformance.csv')
    print(df.head())

    freq = df['writing score'].value_counts()
    print('')
    print('Se crea una lista a partir del csv usando calificacion y conteo, ambos agrupados')
    print('Para manipular sólo la informacion de calificacion de writing')
    print('')
    print(freq.head())

    df_freq = freq.to_frame()
    print('')
    print('Se convierte la salida de modo lista')
    print('Por una en modo frame, tipo excel. Nótese la cabecera de las columnas')
    print('')
    print(df_freq.head())

    df_freq.reset_index(inplace = True)
    print('')
    print('Se realiza limpieza de información')
    print('Para reiniciar los indices y que los valores del frame se asocien al indice')
    print('En lenguaje de base de datos, se agrega llave primaria. Notese la cabecera')
    print('')
    print(df_freq.head())

    df_freq = df_freq.rename(columns = {'index':'writing score', 'writing score':'number of students'})
    print('')
    print('Se renombran las cabeceras para colocarlas acorde a la información')
    print('')
    print(df_freq.head())


if __name__ == '__main__':
    run()