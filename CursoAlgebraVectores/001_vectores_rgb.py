from icecream import ic
import numpy as np

ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
NEGRO = [0, 0, 0]

def run():
    ic(ROJO)
    ic(len(ROJO))
    ic(VERDE)
    ic(len(VERDE))
    ic(AZUL)
    ic(len(AZUL))
    ic(NEGRO)
    ic(len(NEGRO))
    print('')
    ic(ROJO + VERDE)
    ic('Suma de vectores:', np.array(ROJO) + np.array(VERDE))
    print('\nEjemplos de subvectores por medio del índice.\nCada vector esta representado por una lista')
    ic('Concatenación de listas: ', NEGRO + AZUL)
    ic('Subvector <negro> de <negro + azul>: ', (NEGRO + AZUL)[0:3])
    ic('Subvector <azul> de <negro + azul>: ', (NEGRO + AZUL)[3:])


if __name__ == '__main__':
    run()