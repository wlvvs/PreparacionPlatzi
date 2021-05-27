# Se revisa el concepto de trasposicion
import numpy as np
from icecream import ic

def run():

    '''El proceso de trasponer consiste en cambiar filas por columnas, por lo que
    el concepto no aplica para datos escalares
    '''
    escalar = 3
    ic(escalar)
    '''El proceso de trasponer consiste en cambiar filas por columnas, por lo que
    el concepto no es visible en vectores, excepctuando el proceso de operación de los elementos
    del vector

    Para ejecutar el proceso de vector, se hace uso de la funcion .T
    Y por convencion de entendimiento, las variables que se encuentran bajo el proceso
    de trasposicion, se colocan con el subfijo _t
    '''
    vector = np.array([escalar, escalar + 1, escalar * 4, escalar - 3])
    ic(vector)
    vector_t = vector.T
    ic(vector_t)
    matriz = np.array([vector * 4, vector * 3, vector + 10])
    ic(matriz)
    matriz_t = matriz.T
    matriz_t_t = matriz_t.T
    ic(matriz_t)
    ic(matriz_t_t)
    '''
    El proceso del tensor al ser traspuesto cambia la jerarquia en sus dimensiones

    AL realizar el proceso de trasposicion de una variable previamente traspuesta, regresamos al valor original
    '''
    tensor = np.array([[matriz * 3], [matriz * 2]])
    tensor = tensor.squeeze()
    ic(tensor)
    tensor_t = tensor.T
    tensor_t_t = tensor_t.T
    ic(tensor_t)
    ic(tensor_t_t)


if __name__ == '__main__':
    run()