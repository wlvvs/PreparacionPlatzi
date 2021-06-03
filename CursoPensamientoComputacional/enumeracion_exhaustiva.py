'''
Consiste en realizar las iteraciones una por una y validar cada uno de los casos.
Computacionalmente podría significar un problema de tiempo y recursos debido a que
las operaciones deben repetirse hasta determinar la solución.
Sólo hay dos respuestas, si o no
'''

from icecream import ic

def run(val):
    
    objetivo = val
    respuesta = 0

    while respuesta ** 2 < objetivo:
        respuesta += 1
        # ic(respuesta, ' ', respuesta ** 2, ' ',  objetivo)

    if respuesta ** 2 == objetivo:
        print(f'\n  La raiz cuadrada de {objetivo} es {respuesta}\n')
        # ic(respuesta, ' ', respuesta ** 2, ' ',  objetivo)
    else:
        print(f'\n  {objetivo} no tiene raíz cuadrada exacta\n')
        # ic(respuesta, ' ', respuesta ** 2, ' ',  objetivo)


if __name__ == '__main__':
    run(val)