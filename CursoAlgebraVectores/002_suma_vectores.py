from icecream import ic
import numpy as np

ROJO = [255, 0, 0]
VERDE = [0, 255, 0]
AZUL = [0, 0, 255]
NEGRO = [0, 0, 0]
A = [0, 255, 0]

def run():
    ic(ROJO)
    ic(len(ROJO))
    ic(np.array(ROJO))
    ic(np.array(ROJO).shape)
    ic(VERDE)
    ic(len(VERDE))
    ic(np.array(VERDE))
    ic(np.array(VERDE).shape)
    ic(AZUL)
    ic(len(AZUL))
    ic(np.array(AZUL))
    ic(np.array(AZUL).shape)
    ic(NEGRO)
    ic(len(NEGRO))
    ic(np.array(NEGRO))
    ic(np.array(NEGRO).shape)
    print('')
    ic([i + j for i, j in zip(ROJO, AZUL)])
    ic(np.array(ROJO) + np.array(AZUL))

    color1 = np.array(ROJO) + np.array(VERDE) + np.array(A)
    ic(color1)
    color2 = np.array(ROJO) + np.array(VERDE)
    ic(color2)
    color3 = np.array(NEGRO) + np.array(A)
    ic(color3)


if __name__ == '__main__':
    run()