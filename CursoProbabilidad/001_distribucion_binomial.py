# Implementación de distribución binomial siguiente la secuencia de eventos de Bernoulli

import numpy as np # Manejo de matrices y arreglos de números en general
from numpy.random import binomial # Se importa un generador aleatorio de números basado en distribución binomial
from scipy.stats import binom # Se importa para implementar funcion binomial
from math import factorial
import matplotlib.pyplot as plt # Graficación
from icecream import ic # Libreria para el test

# Recibe k (numero de exitos), n (numero de lanzamientos) y p (probabilidad de exito)
def my_binomial(k, n, p):
    return factorial(n) / (factorial(k) * factorial (n -k)) * pow(p, k) * pow(1 -p, n -k)


def plot_hist(num_trials):
    values = [0, 1, 2, 3]
    arr = []
    p = 0.5 # Se define probabilidad equilibrada como constante
    n = 3 #Se definen lanzamientos 

    for _ in range(num_trials):
        arr.append(binomial(n, p))

    # Aqui se generan los hits unicos que corresponden a cada uno de los valores de la vaariable values, generados por el proceso aleatorio
    sim = np.unique(arr, return_counts = True)[1]/len(arr)
    ic(sim)

    # Aqui se generan los mismos valores del caso anterior, pero en definitiva, no con aproxiumaciones aleatorias
    teorica = [binom(3, 0.5).pmf(k) for k in values]
    ic(teorica)

    plt.bar(values, sim, color = 'red') # Se grafican en m  odo barras los valores de la simulacion
    plt.bar(values, teorica, color = 'blue', alpha = 0.5) # Se grafican en modo barras los valores reales, con transparencia
    plt.title('{} experimentos'.format(num_trials)) # Se deja un argumento para colocar el número de intentos requeridos para el lanzado de monedas
    plt.show()



def run():
    ic(my_binomial(2, 3, 0.5))
    
    dist = binom(3, 0.5) # Esta línea realiza la misma actividad que la definición de la funcion binomial, pasando los mismos parámetros
    ic(dist.pmf(2)) # Probability Mass Function - Densidad de probabilidad

    # Obtener la probabilidad de obtener 2 o  menos caras dados 3 lanzamientos con probabilidad de exito de 0.5
    ic(dist.cdf(2)) # Aca se calcula con base a la variable inicial, la distribucion acumulada

    # Aqui se realizan pruebas con aleatoriedad de valores
    p = 0.5 # Se define probabilidad equilibrada como constante
    n = 3 #Se definen lanzamientos 
    ic(binomial(n, p)) # Se usa para la generación aleatoria con respecto a lo que se indicó

    # Se guardan los valoires de la ejecución aleatoria del tirado de monedas
    arr = []
    for _ in range(100):
        arr.append(binomial(n, p))
    
    rep = input ('Indica las repeticiones: ')
    plot_hist(int(rep))


if __name__ == '__main__':
    run()
