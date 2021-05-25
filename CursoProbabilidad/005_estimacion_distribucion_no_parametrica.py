'''
Estimación de densidad con distribucion no paramétrica
No se forza en este caso los paramtetros de distribucion Gaussiana
Esta representacion cuenta con una funcion de suavizado y una funcion base
'''
import numpy as np
from matplotlib import pyplot 
from numpy.random import normal
from scipy.stats import norm
from numpy import hstack # Libreria para unir arreglos
from sklearn.neighbors import KernelDensity # Proceso de suavizado por medio de 'kernels' de la librería
from icecream import ic

def run():
    # Se construye distribucion bimodal con dos samples
    sample2 = normal(loc = 20, scale = 5, size = 3000)
    sample1 = normal(loc = 50, scale = 5, size = 7000)
    # Se unen ambos samples con hstack
    sample = hstack((sample2, sample1))
    

    # Se crea modelo
    # bandwith es el parametro de suavizado y el kernel para determinar el tipo de funciones a usar para el proceso de suavizado
    model = KernelDensity(bandwidth = 2, kernel = 'gaussian')
    
    # Se arregla la estructura de datos
    sample = sample.reshape(len(sample), 1)
    
    # Se realiza proceso de ajustado de datos, por lo que no importará el orden de los samples, aqui los reacomoda
    model.fit(sample)

    # Proceso de reajuste de probabilidades
    values = np.asarray([value for value in range(1, 70)])
    values = values.reshape((len(values), 1))

    # Se generan probabilidades en modo logaritmico para mejor manejo por parte de la computadora
    probabilidades = model.score_samples(values) #probabilidad logarítmica
    probabilidades = np.exp(probabilidades)  # inversión de probabilidad

    pyplot.hist(sample, bins =60, density= True)
    pyplot.plot(values, probabilidades)
    pyplot.show()


if __name__ == '__main__':
    run()