# Se hace uso de funciones anidadas y del enter point. Se habla de la importancia del espaciado para aplicar buenas practicas de código

def palindromo(cadena):
    if cadena.lower().replace(' ','') == cadena.lower().replace(' ','')[::-1]:
        print ("La frase (" + cadena + ") es un palíndromo")
    else:
        print ("La frase (" + cadena + ") no es un palíndromo")


def run():
    cadena = input ("""
    Escribe una frase para evaluar si es palíndromo
    
    """)
    palindromo(cadena)    


if __name__ == '__main__':
    run()   