# Implementación de distribución normal por metodo de Gauss
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm
from icecream import ic

'''
mu: valor de la media de distribución
sigma: valor de la desviación estandar de la distribución
x: variable aleatoria
Ambas aluden al literal griego usado en la formula de la distribución normal
'''

def gaussian(x, mu, sigma):
    # Se define la formula general
    return 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * pow((x - mu) / sigma, 2))


def run():
    # Se define x como una lista que va de -4 a 4 separados con un intervalo de 0.1
    x = np.arange(-4, 4, 0.1)
    ic(x)
    # Se define y como la ejecución de la función Gaussiana, con una media de distribucion igual a 0.0 y una desviacion estandar de 1.0
    y = gaussian(x, 1.0, 1.2)
    ic(y)
    
    '''
    Cuando la mdedia de distribución incrementa o disminuye, la funcion se desplaza sobre el eje x
    Cuando el valor de la desviación estandar crece o decrece, la campana engrosao adelgaza, respectivamente
    '''
    plt.plot(x, y, color = 'red')

    # Se define una variable para almacenar la distribución normal desde scipy, con el cual no usamos la funcion, se hace directamente
    # Los valores de entrada son los mismos definidos para mu y sigma
    dist = norm(0, 1)
    # pdf se refiere a funcion de densidad de probablidad y se cicla con respecto al valor de x que defiimos previamente
    y = [dist.pdf(value) for value in x]
    # Los valores de y pasan como un lista, no como un array que en el paso anterior
    ic(y)
    plt.plot(x, y, color = 'green')
    
    # cdf se refiere a densidad de probabilidad acumulada. En este paso, internamente se hace un proceso de calculo integral para obtener el área bajo la curva
    # Se toman los mismos valores previamente definidos
    y = [dist.cdf(value) for value in x]
    ic(y)
    plt.plot(x, y, color = 'blue')
    plt.show()


if __name__ == '__main__':
    run()