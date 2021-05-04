# Ejecucion de programa haciendo uso de for. Fue requerido usar internet para encontrar una manera de hacer infinito un loop de FOR
def potencia():
    import itertools
    inicio = 0
    
    for valor in itertools.count(start = 0):
        print("2 elevado a la " + str(valor) + " es igual a " + str(2 ** inicio))
        inicio += 1
        if 2 ** inicio > 1000:
            break



def run():
    print ("""
    Este programa imprime la serie de potencias de 2 necesarias
    para cumplir llegar al número 1000 por medio de un bucle
    
    """)
    potencia()
    print("")

if __name__ == '__main__':
    run()