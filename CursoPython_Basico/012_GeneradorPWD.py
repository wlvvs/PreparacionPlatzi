import random

def genera_pwd():
    
    altas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    bajas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    especial = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    cadena = altas + bajas + numeros + especial

    passwd = []

    longitud = random.randint(10,18)

    for i in range(longitud):
        caracter_random = random.choice(cadena)
        passwd.append(caracter_random)
    
    passwd = ''.join(passwd)
    return passwd


def run():
    pwd = genera_pwd()
    print('')
    print ('Tu nueva contraseña es: '+ pwd)
    print('')


if __name__ == '__main__':
    run()