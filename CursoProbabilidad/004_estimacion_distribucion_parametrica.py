'''
Estimación de densidad con distribucion paramétrica
Conforme se agranda el tamaño del muestreo, la campana de Gauss es mas acotada a la gráfica de
probabilidades
'''
import numpy as np
from matplotlib import pyplot 
from numpy.random import normal
from scipy.stats import norm
from icecream import ic

def run():
    # Se crea un conjunto de datos a partir de muestreos aleatorios, en distribucion normal
    # loc corresponde a mu y scale a sigma (promedio y desviacion estandar)
    sample = normal(loc = 50, scale = 5, size = 100000)
    ic(sample)
    mu = sample.mean()
    ic(mu)
    sigma = sample.std()
    ic(sigma)

    dist = norm(mu, sigma)
    values = [value for value in range(30, 70)]
    probabilidades = [dist.pdf(value) for value in values]
    # bins se usa para definir el numero de barras a mostrar
    # density es que normalice conteos para que me den probabilidades y no números grandes
    pyplot.hist(sample, bins =30, density = True)
    pyplot.plot(values, probabilidades)
    pyplot.show()


if __name__ == '__main__':
    run()