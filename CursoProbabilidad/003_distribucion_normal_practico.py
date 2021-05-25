# Implementación de distribución normal por metodo de Gauss caso practico
from numpy.lib import unique
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
from icecream import ic


def run():
    # Se lee de formato excel el archivo indicado. Me pidió bajar la libería xlrd
    df = pd.read_excel('./files/s057.xls')
    ic(df)
    # Se crea un arreglo en donde extraemos una columna en general y se le borran los valores del encabezado
    arr = df['Normally Distributed Housefly Wing Lengths'].values[3:]
    ic(arr)
    # La asignación de valores de mu y sigma a partir de los valores de nuestra muestra, es conocido como el proceso de estimación paramétrica
    # Se calcula el valor de la media de distribución
    mu = arr.mean()
    ic(mu)
    # Se calcula el valor de la desviacion estandar
    sigma = arr.std()
    ic(sigma)
    # Se define un arreglo de valores similar a los contenidos en mi grafica
    x = np.arange(30, 60, 0.1)
    ic(x)
    # Se define una campana de Gauss con los valores de la muestra
    dist = norm(mu, sigma)
    # Se calcula la densidad de probabilidad para los valores de x
    y = [dist.pdf(value) for value in x]
    ic(y)
    plt.plot(x, y, color = 'red')

    # La funcion de numpy unique da el conteo de valores unicos para mi muestra, pero lo da en dos listas, la primera con los indices de mi muestra
    # y la segunda con el conteo de valores encontrados
    values, dist = np.unique(arr, return_counts = True)
    ic(values, dist)
   # Como la campana de Gauss toma valores entre cero y uno, la forma de normalizar mis barras es dividiendo cada elemento
    # entre la longitud del valor de mi arreglo
    plt.bar(values, dist / len(arr), color = 'blue')

    plt.show()


if __name__ == '__main__':
    run()