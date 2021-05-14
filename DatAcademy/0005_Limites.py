'''

Python Cardio - Reto 5

Dado un limite inferior y uno superior, determinar si un tercer valor
esta dentro del rango. Si no está, repetir el proceso

'''
import os
import time

def evaluacion(lim_inf, lim_sup, valor):
    
    if (float(lim_inf) < 0 and float(lim_sup) < 0) or float(lim_sup) < 0:
        valor = abs(float(valor))
        tmp = abs(float(lim_sup))
        lim_sup = abs(float(lim_inf))
        lim_inf = abs(float(tmp))

    if float(lim_inf) <= float(valor) <= float(lim_sup):
        return True
    else:
        return False


def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def run():
    corte = 0

    while True:
        try:
            print('''

            Programa para determinar si un número esta dentro
            de un rango preestablecido.

            Deberas ingresar la información con la siguiente máscara:
            
               inicio || fin || valor a evaluar
            
            Cada uno de los valores deberá estar separado por un espacio.
            Sólo puedes ingresar números (enteros, decimales, con signo)

            ''')
            lim_inf, lim_sup, valor = input('Escribe los valores:   ').split()

            if evaluacion(lim_inf, lim_sup, valor):
                print('')
                print(' El valor', valor, 'se encuentra entre', lim_inf, 'y', lim_sup)
                print('')
                print('    Good bye!')
                corte = 1
            else:
                print('')
                print(' El valor', valor, 'no está entre', lim_inf, 'y', lim_sup)
                print('')
                print('    Intentalo de nuevo!! ')
                time.sleep(4)
                clearenv()

        except ValueError:
            print('')
            print('  Haz ingresado un valor incorrecto. Reintenta  ')
            time.sleep(2)
            clearenv()
        
        if corte == 1:
            break


if __name__ == '__main__':
    run()