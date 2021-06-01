'''
Dictionary comprehension
Se trata de una estructura en la cual se pueden trabajar diccionarios.
Consiste en evaluar los valores del diccionario en un rango especifico
y a su vez, condicionando su guardado.
La estructura de dictionary comprehension es la siguiente:

{<key>:<value> <for element in iterable> <if condition>}

No es necesario usar los simbolos mayor y menor, se colocan sólo
para separar los conjuntos.
El conjunto <key>:<value> representa a cada uno de los elementos del
diccionario, a diferencia de las listas, aqui guardaremos esas dos
propiedades de los diccionarios: llave y valor
El conjunto <for element in iterable> representa el ciclo a partir
del cual se extraeran los elementos
El conjunto <if condition> representa un filtro opcional que se
puede aplicar para guardar el diccionario.

La manera de leer dicha estructura es: para cada elemento
en la instrucción iterable, guardaré la llave y el valor en el
diccionario si se cumple alguna condición existente
'''

def run():
    '''
    Bloque que genera un dicionario  con llaves del 1 al 100 y
    revisa si el valor es divisible entre 3. Si el valor no es
    divisible, lo guarda dentro de la lista, usando estructuras
    típicas
    '''
    tipic_dict = {}

    for i in range(1,101):
        if i%3 != 0:
            tipic_dict[i]= i**3
    
    print(tipic_dict)
    print('')

    '''
    Bloque que genera un dicionario  con llaves del 1 al 100 y
    revisa si el valor es divisible entre 3. Si el valor no es
    divisible, lo guarda dentro de la lista, usando dictionary
    comprehension
    '''
    new_dict = {i:i**3 for i in range (1, 101) if i%3 != 0}
    
    print(new_dict)
    print('')

    '''
    Bloque que genera un diccionario para los primeros 1000 numeros
    naturales, en donde se imprime la raiz cuadrada de cada
    valor, usando dictionary comprehension
    '''
    new_dict = {i:round(i**0.5,2) for i in range (1, 1001)}
    
    print(new_dict)
    print('')

if __name__ == '__main__':
    run()