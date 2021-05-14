'''

Python Cardio - Reto 4

Calculadora de volumen para cilindro

Bonus: Permite elegir entre mas figuras geométricas

'''
import math
import os
import time
from functools import reduce

def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def formula(list_values, choice):
    result = 0

    if choice in (1, 6):
        if choice ==1:
            result = list_values ** 3
        else:
            result = (4/3) * (math.pi) * (list_values ** 3)

    elif choice in (2, 3):
        if choice == 2:
            result = reduce(lambda a, b: a * b, list_values)
        else:
            result = (1/3) * reduce(lambda a, b: a * b, list_values)

    elif choice in (4, 5):
        if choice == 4:
            result = math.pi * reduce(lambda a, b: (a**2) * b, list_values)
        else:
            result = (1/3) * math.pi * reduce(lambda a, b: (a**2) * b, list_values)
        
    if result < 0:
        raise ValueError

    return float(result)


def run():
    corte = 0

    while True:
        try:
            choice = int(input('''
            
            Programa que permite el cálculo del volúmen para diversas figuras geométricas.
            Para elegir una opción, deberás ingresar un número entero.
            Para ingresar los valores a calcular, deberas ingresar números positivos, los decimales están permitidos.

            Elige del siguiente menú que operación quieres realizar:
            
            ________________________________
                Volumen del cubo (1)
                Volumen del ortoedro (2)
                Volumen de la pirámide (3)
                Volumen del cilindro (4)
                Volumen del cono (5)
                Volumen de la esfera (6)
            ________________________________     
            
            '''))
            if choice == 1:
                print('')
                list_values = input('    Dame la longitud del lado:   ') 
                print('')
                if float(list_values) < 0:
                    raise ValueError
                else:
                    final = formula(float(list_values), choice)
                    print('El volumen del cubo es', final)
                    corte = 1

            elif choice == 2:
                print('')
                v1, v2, v3 = input('''    Dame la latitud, la longitud y la altura, separados por un espacio
                Por ejemplo >>   0 0 0   :   ''').split()
                list_cond = [float(v1) > 0, float(v2) > 0, float(v3) > 0]

                if (all(list_cond)):
                    list_values = [float(v1), float(v2), float(v3)]
                    print('')
                    final = formula(list_values, choice)
                    print('El volumen del ortoedro es',final)
                    corte = 1
                else:
                    raise ValueError

            elif choice ==3:
                print('')
                v1, v2 = input('''    Dame el área de la base y la altura, separados por un espacio
                Por ejemplo >>   0 0   :   ''').split()
                list_cond = [float(v1) > 0, float(v2) > 0]

                if (all(list_cond)):
                    list_values = [float(v1), float(v2)]
                    print('')
                    final = formula(list_values, choice)
                    print('El volumen de la pirámide es',final)
                    corte = 1
                else:
                    raise ValueError

            elif choice in (4, 5):
                print('')
                v1, v2 = input('''    Dame el radio y la altura, separados por un espacio
                Por ejemplo >>   0 0   :   ''').split()
                list_cond = [float(v1) > 0, float(v2) > 0]

                if (all(list_cond)):
                    list_values = [float(v1), float(v2)]
                    print('')
                    final = formula(list_values, choice)
                    if choice ==4:
                        print('El volumen del cilindro es',final)
                    else:
                        print('El volumen del cono es',final)
                    corte = 1
                else:
                    raise ValueError

            elif choice == 6:
                print('')
                list_values = input('    Dame el valor del radio:   ') 
                print('')

                if float(list_values) < 0:
                    raise ValueError
                else:
                    final = formula(float(list_values), choice)
                    print('El volumen de la esfera es', final)
                    corte = 1
            else:
                raise ValueError
        
        except ValueError:
            print('')
            print('    El valor o valores insertados no están soportados. Reintentar ')
            time.sleep(2)
            clearenv()
        
        if corte == 1:
            break


if __name__ == '__main__':
    run()