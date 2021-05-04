# Se usan módulos internos de Python, en este caso, el módulo random
import random

def run():
    num_random = random.randint(1,100)
    print('')
    num_elegido = int(input ('Elige un número del 1 al 100:   '))
    while num_elegido != num_random:
        if num_elegido < num_random:
            print('El numero elegido ('+ str(num_elegido) + ') debe ser mas grande')
        else:
            print('El numero elegido ('+ str(num_elegido) + ') debe ser mas pequeño')
        print('')
        num_elegido = int(input ('Elige otro número:   '))
    print ('')
    print('¡Ganaste!')
    print ('')


if __name__ == '__main__':
    run()