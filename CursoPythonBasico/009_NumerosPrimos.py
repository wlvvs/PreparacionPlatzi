# Obtener si un número es primo por medio del Teorema de Wilson
def calcula_factorial(numero):
    fac = 1
    if int(numero) >= 1:
        for i in range (1, int(numero) + 1):
            fac = fac * i
            return fac
    else:
        return 0


def es_primo(numero, factorial):
    if int(factorial) + 1 % int(numero) == 0:
        return True
    else:
        return False


def run():
    
    factorial = 0
    
    print("")
    numero = input ("Ingrese un número para determinar si es o no primo:   ")
    factorial = calcula_factorial(numero)
    if factorial ==0:
        print("El número 0 no es número primo")
    else:
        if es_primo(numero, factorial):
            print("El número " + str(numero) + " es un número primo")
        else:
            print("El número " + str(numero) + " no es un número primo")


if __name__ == '__main__':
    run()