from icecream import ic
import numpy as np

def run():
    x = np.array([1, -1, 1])
    a = 3.1
    b = 1
    ic(a, b, x)
    ic(a * x)
    ic(x * a)
    ic((b + a) * x)
    ic((b * x) + (a * x))


if __name__ == '__main__':
    run()