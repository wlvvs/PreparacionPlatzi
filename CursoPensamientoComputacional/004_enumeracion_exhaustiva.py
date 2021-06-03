'''
Consiste en realizar las iteraciones una por una y validar cada uno de los casos.
Computacionalmente podría significar un problema de tiempo y recursos debido a que
las operaciones deben repetirse hasta determinar la solución.
Sólo hay dos respuestas, si o no
'''

from icecream import ic

def run():
    
    objetivo = int(input('\nIngresa un número entero: '))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        ic(respuesta, respuesta ** 2, objetivo)
        respuesta += 1

    if respuesta ** 2 == objetivo:
        ic(respuesta, respuesta ** 2, objetivo)
        print(f'\nLa raiz cuadrada de {objetivo} es {respuesta}')
    else:
        ic(respuesta, respuesta ** 2, objetivo)
        print(f'\n{objetivo} no tiene raíz cuadrada exacta')


if __name__ == '__main__':
    run()