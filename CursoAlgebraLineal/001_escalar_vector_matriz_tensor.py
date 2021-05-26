import numpy as np
import matplotlib.pyplot as plt
from icecream import ic

ic.configureOutput(includeContext=True)

def run():
    # Un escalar es técnicamente una variable simple en python, matemáticamente es un número
    escalar = 2
    ic(escalar)

    # Un vector es una composición de dos o mas escalares en forma unidimensional
    vector = np.array([escalar, escalar + 1, escalar + 5])
    ic(vector)

    # Una matriz es una composicion de dos o mas vectores en forma bidimensional
    matriz = np.array([vector * 4, vector * 3, vector * 2])
    ic(matriz)

    # Un tensro es una composicion de dos o mas matrices en forma tridimensional
    tensor = np.array([[matriz * 3], [matriz * 2], [matriz * 4]])
    ic(tensor)
    # Fue necesario agregar esta instruccion debido a que, al momento de conformar los datos, me estaba llevando espacios entre matrices
    tensor = tensor.squeeze()
    ic(tensor)

    # La interpolacion es omo se unen los espacios entre dos numeros
    plt.imshow(tensor, interpolation='nearest')
    plt.show()



if __name__ == '__main__':
    run()