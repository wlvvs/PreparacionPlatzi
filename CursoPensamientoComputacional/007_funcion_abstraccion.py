from timeit import default_timer as timer # Extrae el tiempo actual del equipo
from enumeracion_exhaustiva import run as enex
from aproximacion_soluciones import run as apsol
from busqueda_binaria import run as busbin

def run():
    valor = int(input('''
    Programa para calcular la raíz cuadrada de un número.
    Puedo calcular la raíz cuadrada de un número por alguno de estos 3 métodos
        
    1. Por método de enumeración exhaustiva
    2. Por método de aproximación de soluciones
    3. Por método de búsqueda binaria
    4. Comparación de tiempo y resultados por todos los métodos

    Elige alguna de las siguientes opciones para realizar el cálculo: '''))

    val = int(input('\n\n    Ingresa un número: '))

    if valor == 1:
        start = timer()
        enex(val)
        end = timer()
        print('\nEl tiempo transcurrido fue de',end - start,'\n')
    elif valor == 2:
        start = timer()
        apsol(val)
        end = timer()
        print('\nEl tiempo transcurrido fue de',end - start,'\n')
    elif valor == 3:
        start = timer()
        busbin(val)
        end = timer()
        print('\nEl tiempo transcurrido fue de',end - start,'\n')
    elif valor == 4:
        start = timer()
        print('\nEnumeracion exhaustiva')
        enex(val)
        end = timer()
        print('\nEl tiempo transcurrido fue de',end - start,'\n')
        start = timer()
        print('\nAproximación de soluciónes')
        apsol(val)
        end = timer()
        print('\nEl tiempo transcurrido fue de',end - start,'\n')
        start = timer()
        print('\nBúsqueda binaria')
        busbin(val)
        end = timer()
        print('\nEl tiempo transcurrido fue de',end - start,'\n')
    else:
        print(f'\n La opción {valor} no corresponde al menu')


if __name__ == '__main__':
    run()