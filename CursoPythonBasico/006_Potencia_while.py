# Ejecucion de programa haciendo uso de while
def potencia():

    inicio = 0
    valor = 2 ** inicio 
    while valor < 1000:
        print("2 elevado a la " + str(inicio) + " es igual a " + str(valor))
        inicio = inicio + 1
        valor = 2 ** inicio 
        

def run():
    print ("""
    Este programa imprime la serie de potencias de 2 necesarias
    para cumplir llegar al número 1000 por medio de un bucle
    
    """)
    potencia()


if __name__ == '__main__':
    run()