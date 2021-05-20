'''
Aquí se generan gráficas de revisión
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    
    '''
    Se carga el csv usando pandas
    '''
    df = pd.read_csv('./files/StudentsPerformance.csv')
    
    '''
    Se invoca la construcción de un histograma, teniendo en el 
    eje de las X la calificación del writing, clasificados por
    la condicion de toma de test de preparacion del curso, con
    los valores de ambas evaluaciones sobrepuestos en la misma columna
    '''
    sns.histplot(data = df, x = 'writing score', hue = 'test preparation course', multiple = 'stack')
    plt.show()

    '''
    Se invoca la construcción de una gráfica de dispersion, misma que nos
    servirá para poder obtener la regresion lineal
    '''
    sns.scatterplot(data = df, x = 'reading score', y = 'writing score')
    plt.show()
    

if __name__ == '__main__':
    run()