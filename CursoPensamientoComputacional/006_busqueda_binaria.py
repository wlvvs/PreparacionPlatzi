'''
Este algoritmo requiere que el universo de datos se encuentre ordenado.
Despues de eso, dentro del universo, lo divide en dos partes iguales y
pregunta en que parte se encuentra el valor. Realiza esta actividad
de manera recurrente hasta dar con la respuesta
'''

from icecream import ic

def run():
    objetivo = int(input('Elige un numero: '))
    # Razon de revisión o iteración de pasos
    epsilon = 0.0001
    # Es el límite inferior de mi busqueda
    bajo = 0.0
    # Límite superior que dará el valor mas alto
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        if respuesta ** 2 < objetivo:
            bajo = respuesta
            ic(bajo, alto, respuesta)
        else:
            alto = respuesta
            ic(bajo, alto, respuesta)
        respuesta = (alto + bajo) / 2
    
    print(f'\nLa raíz cuadrada de {objetivo} es {respuesta}')
    ic(bajo, alto, respuesta)


if __name__ == '__main__':
    run()