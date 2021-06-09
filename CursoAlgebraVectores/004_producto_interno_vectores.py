from icecream import ic
import numpy as np

def p(x):
    '''
    Se revisa la generación de un polinomio a partir de vectores.
    Teniendo

    c = [1, 2] y x = [1, x]
    Entonces

    p(x) = 1 + 2x
    '''
    return np.array([1, 2]).dot(np.array([1, x]))


def run():
    a = np.array([1, 0, 0, 0])
    b = np.array([0, 0, 1, 0])

    ic(a.dot(b))
    ic(a@b)
    ic(p(0))
    ic(p(1))
    ic(p(2))
    ic(p(-1))


if __name__ == '__main__':
    run()