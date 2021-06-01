'''
List comprehension
Se trata de una estructura en la cual se pueden trabajar las listas.
Consiste en evaluar los valores de la lista en un rango especifico
y a su vez, condicionando su guardado.
La estructura de list comprehension es la siguiente:

[<element> <for element in iterable> <if condition>]

No es necesario usar los simbolos mayor y menor, se colocan sólo
para separar los conjuntos.
El conjunto <element> representa a cada uno de los elementos de 
la lista
El conjunto <for element in iterable> representa el ciclo a partir
del cual se extraeran los elementos
El conjunto <if condition> representa un filtro opcional que se
puede aplicar para guardar la lista.

La manera de leer dicha estructura es: para cada elemento
en la instrucción iterable, guardaré dicho elemento en la 
lista si se cumple alguna condición existente
'''

def run():
    '''
    Bloque que genera una lista de valores del 1 al 100 y evalua si
    el valor es divisible entre 3. Si el valor no es divisible,
    lo guarda dentro de la lista, usando estructuras típicas
    '''
    tipic_list = []

    for i in range(1,101):
        if i % 3 != 0:
            tipic_list.append(i**2)
    
    print(tipic_list)
    print('')
    
    '''
    Bloque que genera una lista de valores del 1 al 100 y evalua si
    el valor es divisible entre 3. Si el valor no es divisible,
    lo guarda dentro de la lista, usando list comprehension
    '''
    new_list = [i**2 for i in range (1, 101) if i%3 != 0]
    
    print(new_list)
    print('')

    '''
    Bloque que genera una lista de valores con un máximo de longitud
    5 en donde guarda en la lista aquellos que sean divisibles
    entre 4, 6 y 9, usando list comprehension
    '''
    new_list = [i for i in range (1, 100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]

    print(new_list)
    print('')


if __name__ == '__main__':
    run()