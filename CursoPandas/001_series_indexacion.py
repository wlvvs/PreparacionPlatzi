from icecream import ic
import pandas as pd
import numpy as np
from pandas.core.dtypes.missing import isnull

def run():
    """
    Se inicia con la revisión de datos en pandas.
    Una serie es una lista de elementos que tiene adjunto una columna
    de indexacion.
    Sus propiedades son:
    - valores >> indica los elementos que estan contenidos en la
    serie, asi como su tipo de dato de manera explicita
    - indices >> indica las caracteristicas del indice, es decir,
    el valor inicial, el valor final y el incremento o numero de paso
    - dimension >> indica las caracteristicas de composicion de la
    serie en forma integrada

    Nótese al momento de ejecutar las instrucciones, que cuando traemos
    una lista de elementos dentro de la serie, esta regresa el
    registro completo, es decir, tanto el valor explicito como
    el índice y el tipo de dato de los elementos, así también,
    notese que para indicar la lista de elementos que se requieren,
    estos se pasan entre corchetes

    """
    s1 = pd.Series([10, 9, 8, 7, 6, 5])
    ic(s1)
    ic(s1.values)
    ic(s1.index)
    ic(s1.shape)
    print('El valor del cuarto elemento (usando el método de índice [3]) es:')
    ic(s1[3])
    print('La lista de elementos 1, 3 y 5 (usando el método de lista de índices [0, 2, 4]) es:')
    ic(s1[[0, 2, 4]])

    """
    Dentro de la serie, es posible que el indice sea configurado de tal
    manera que tenga los valores que nosotros definamos.
    Y de la misma forma que se hace con el metodo de llamar valores por
    medio de indices, este tambien funciona, recordando que ahora los 
    indices corresponden a valores definidos por nosotros

    """

    s2 = pd.Series([10, 9, 8, 7, 6, 5], index = ['a', 'b', 'c', 'd', 'e', 'f'])
    ic(s2)
    print('El valor del cuarto elemento (usando el método de índice [d]) es:')
    ic(s2['d'])
    print('La lista de elementos 1, 3 y 5 (usando el método de lista de índices [a, c, e]) es:')
    ic(s2[['a', 'c', 'e']])

    """
    Un diccionario es un elemento que permite guardar cualquier tipo de valor.
    Sus atributos son llaves y valores. Una llave funciona como un identificador
    del valor y el valor le da sentido a la llave.
    De igual forma, podemos usar el concepto que ya manejamos para extraer valores
    especificos.

    El formato del diccionario es parecido al formato json, que ayuda al manejo
    y extracción de informacion.

    Ahora, con base a lo aprendido, el concepto de diccionario puede aplicar 
    al de serie, por lo que, podemos generar una serie a partir de un diccionario.
    En tal caso, tendremos una serie con índices establecidos por las
    abreviaturas de los paises y con valores por los enteros asignados.
    A partri de este punto, podemos aplicar lo que ya aprendimos previamente

    """
    d1 = {'CO': 100,
        'MX': 200,
        'AR': 300,}
    ic(d1)
    ic(d1.keys())
    ic(d1.values())
    ic(d1['AR'])

    sdict = pd.Series(d1)
    ic(sdict)

    """
    Al manipular nuestra nueva serie, podemos hacer el proceso de cambio
    de indices de igual forma, sin embargo, un detalle en el comportamiento
    es que, cuando hacemos el proceso y cambiamos el nombre del indice,
    pandas deja de reconocer la referencia del valor, y nos agrega uno nuevo
    con el nulo o vacio.
    El valor nulo, matematicamente, no es operable

    Para revisar si existe algun nulo dentro de nuestra serie, se usara
    la funcion is null. que se puede usar de igual forma de manera inversa,
    dependiendo de la convencion o del contexto de uso

    Por ultimo, haciendo referencia a un aporte en el sistema de comentarios,
    si queremos que de nuestra serie solo se nos den aquellos valores
    que no contengan nulos, se hace usando la misma funcion y, por
    tanto, es posible tambien hacerlo para tener unicamente los elementos
    que tienen nulos
    También podemos generalizar la revision de la información para saber
    de antemano si existe algun elemento nulo en toda la serie con la 
    funcion any

    """

    sdict2 = pd.Series(d1, index = ['CO', 'MX', 'PE'])
    ic(sdict2)
    ic(sdict2.isnull())
    ic(sdict2.notnull())
    ic(sdict2[sdict2.isnull()])
    ic(sdict2[sdict2.notnull()])
    ic(sdict2.isnull().any())


if __name__ == '__main__':
    run()
