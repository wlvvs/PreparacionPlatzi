'''

Python Cardio - Reto 1

Escribe un programa que tome la base y la altura como parámetros y
calcule el área del triángulo.

Bonus: el programa debe determinar si el triángulo es isósceles,
equilátero o escaleno.

'''
import os
import time
import re


def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def calcula_area(base, altura):
    area = (base * altura)/2
    return area


def calcula_triangulo(base, altura):
    equilatero = float(base) * ((3**1/2)/2)
    hipotenusa = (((float(base)**2)/4) + (float(altura)**2))**0.5
    isoceles = (float(base) * float(hipotenusa))/2

    if equilatero == float(altura):
        print('')
        print('Tu triángulo es equilatero')
    elif isoceles == (float(base) * float(altura))/2:
        print('')
        print('Tu triángulo es isoceles')
    else:
        print('')
        print('Tu triángulo es escaleno')
        print('')
        print('Con la información dada, tu triángulo sería EQUILATERO si la altura fuera de', equilatero)
        print('Con la información dada, tu triángulo seria ISOSCELES si la altura fuera de', hipotenusa)


def valida_dato(dato):
    try:
        patron = ('^[^A-Za-z--]*$')

        if re.match(dato, patron):
            print('    El valor insertado es incorrecto :(    ')
            return False
        
    except ValueError:
        time.sleep(1)
        clearenv()
    
    return True


def run():
    corte = 0

    while True:
        try:
            print('''
    Este programa calculará el área de un triángulo con respecto
    a las características que proporciones.

    Los valores que necesito para calcular el área son:

    a) La medida de la base
    b) La medida de la altura

    Los valores a ingresar deben ser numéricos positivos

            ''')
            base = input('    Ingresa el valor de la base:   ')
            
            if float(base) < 0:
                raise ValueError

            if valida_dato(base) == True:
                altura = input('    Ingresa el valor de la altura:   ')
                if float(altura) < 0:
                    raise ValueError
            else:
                raise ValueError
                
            if valida_dato(altura) == True:
                corte = 1
                area = calcula_area(float(base), float(altura))
                print('')
                print('    El area del triángulo es: ', area)
                calcula_triangulo(base, altura)
            else:
                raise ValueError
                time.sleep(2)
                clearenv()
                corte = 0
        
        except ValueError:
            print('    El valor insertado es incorrecto :(    ')
            time.sleep(2)
            clearenv()
            corte = 0
        
        if corte == 1:
            break


if __name__ == '__main__':
    run()