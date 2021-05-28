# Se genera un script para crear vectores aleatorios para usar script graficador
import numpy as np
import random
import importlib.util
from icecream import ic
import matplotlib.pyplot as plt

v_escalar1 = int(random.choice((1, 3, 5)))
v_escalar2 = int(random.choice((1, 2, 4, 5)))

def run():

    
    '''
    Como no pude usar el metodo del profesor, lo hice por medio la libreria de importar librerias
    Se define la cabecera indicando nombre y ruta con extensión
    Luego se inportan los módulos y al final se ejecutan
    '''
    spec = importlib.util.spec_from_file_location('graficarVectores', './utils/graficarVectores.py')
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    
    vector1 = np.array([v_escalar1, v_escalar1 + v_escalar2])
    vector2 = np.array([v_escalar2 + v_escalar1, v_escalar2])
    ic(vector1)
    ic(vector2)


    foo.graficarVectores([vector1, vector2], ['blue', 'black'])
    plt.xlim(-1, 12)
    plt.ylim(-1, 12)
    plt.show()


if __name__ == '__main__':
    run()