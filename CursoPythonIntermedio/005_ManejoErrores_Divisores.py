import os
import time

def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def divisors(num_div):
    div_list = [b for b in range (1, num_div + 1) if num_div % b == 0]
    return div_list
    

def run():
    corte = 0
    while True:
        try:
            print('')
            num_div = int(input('Escribe un número positivo al cual se le calcularán sus divisores:   '))
            if num_div < 0:
                raise ValueError
            print(divisors(num_div))
            corte = 1
        except ValueError:
            print('Recuerda ingresar un número positivo, el valor insertado es incorrecto')
            time.sleep(2)
            clearenv()
        if corte == 1:
            break


if __name__ == '__main__':
    run()