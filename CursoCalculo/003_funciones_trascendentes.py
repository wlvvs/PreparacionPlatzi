import numpy as np
import matplotlib.pyplot as plt

res = 100    

def f(x, opcion):
    try:
        if opcion == 1:
            m = 2
            b = 2
            return (m * x) + b
        elif opcion == 2:
            return (-2 * x**7) + (4 * x**2) - 9
        elif opcion == 3:
            return np.sin(x)
        elif opcion == 4:
            return np.cos(x)
        elif opcion == 5:
            return np.tan(x)
        elif opcion == 6:
            return np.e**x
        elif opcion == 7:
            return np.log10(x)
        elif opcion == 8:
            y = np.zeros(len(x))
            for idx, x in enumerate(x):
                if x>=0:
                    y[idx] = 1.0
            return y + 1
        else:
            raise ValueError
    except ValueError:
        raise ValueError


def run():
    try:
        x = np.linspace (-10.0, 10.0, num = res)
        opcion = int(input('''
        Elige la opción de función que quieres ver en gráfica:
        (1) Lineal
        (2) Polinomial

        Trascendental
        (3) Seno
        (4) Coseno
        (5) Tangente
        (6) Exponencial
        (7) Logaritmo
        (8) Seccionada
                        '''))
        y = f(x, opcion)
        
        fig, ax = plt.subplots()
        ax.plot (x, y)
        ax.grid()
        ax.axhline(y = 0, color = 'r')
        ax.axvline(x = 0, color = 'r')
        
        plt.show()

    except ValueError:
        print('')
        print('   Valor no soportado')

if __name__ == '__main__':
    run()
