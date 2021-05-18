import numpy as np
import matplotlib.pyplot as plt

# Se pasa el dominio (x)
def f(x):
    # Se regresa la ejecución de la función
    return (2 * x**10) + (x**6) - (2 * x**4) - (x**2) + (18 * x) - 3


def run():
    #  Resolución de gráfica, los puntos a mostrar
    res = 100    
    
    '''Se genera un vector que determina puntos
    Los parametros que recibe son punto inicial, punto final y número
    de puntos (mismos que especificamos anteriormente en la resolucion)'''

    x = np.linspace (-10.0, 10.0, num = res)
    # Se llama a la función que ejecutará la tabulación
    y = f(x)

    # Definicion de ejes
    fig, ax = plt.subplots()
    # Se indica que dibuje x y y
    ax.plot (x, y)
    # Se indica que coloque la cuadrícula
    ax.grid()
    '''Se indica que dibuje eje x y y, ambos en el punto 0 con
    respecto a su orientacion'''

    ax.axhline(y = 0, color = 'r')
    ax.axvline(x = 0, color = 'r')
    
    # Se realiza la graficacion
    plt.show()

if __name__ == '__main__':
    run()
