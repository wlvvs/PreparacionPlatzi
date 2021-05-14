'''

Python Cardio - Reto 3

Convierte millas a kilometros, donde 1 milla = 1.609344 Km

Bonus: Permite elegir la operación

'''
import os
import time

def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def operacion(selector, valor):
    
    print('')
    if selector == 1:
        print('   ', 1.609344 * valor, 'millas son', valor, 'kilometros')
        corte = 1
    elif selector == 2:
        print('   ', valor/1.609344, 'kilometros son', valor, 'millas')
        corte = 1
    return corte


def run():

    corte = 0
    while True:
        clearenv()
        try:
            selector = input('''
        
        Programa de cálculo de distancia.
        Elige el tipo de conversión que quieres realizar:
        
        (1) Millas a kilometros
        (2) Kilometros a millas   ''')
            
            if int(selector) <= 2:
                valor = input('''
        
        Ahora, indicame la distancia que quieras que convierta   ''')
            else:
                raise ValueError
            
            if float(valor):
                corte = operacion(int(selector), float(valor))
                print('')
                print('')
            else:
                raise ValueError

        except ValueError:
            print('')
            print('   Opcion ingresada no válida')
            time.sleep(2)

        if corte == 1:
            break

if __name__ == '__main__':
    run()