from icecream import ic
import pandas as pd
import numpy as np

def run():
    ic(pd.__version__) # comando para encontrar la versión de mi libreria
    """
    Un dataframe es una estructura de datos bidimensional con columnas que 
    a su vez, almacenan diferentes tipos de datos.
    Para generar un dataframe, usamos la funcion de pandas DataFrame.
    En esta utilería tambien podemos hacer reemplazo del nombre del índice, 
    ya que por default, estos se generan de manera numérica

    """

    dict_data = {
    'edad' : [ 10, 9, 13, 14, 12, 11, 12],
    'cm' : [ 115, 110, 130, 155, 125, 120, 125],
    'pais' : [ 'co', 'mx', 'co', 'mx', 'mx', 'ch', 'ch'],
    'genero' : [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'Q1' : [ 5, 10, 8, np.nan, 7, 8, 3],
    'Q2' : [ 7, 9, 9, 8, 8, 8, 9]
    }
    ic(dict_data)
    df = pd.DataFrame(dict_data)
    ic(df)
    df = pd.DataFrame(dict_data, index = ['ana','benito','camilo','daniel','erika','fabian','gabriela'])
    ic(df)

    """
    Con base a lo aprendido previamente, es posible obtener de nuestro
    dataframe los atributos del mismo, como son los indices, las columnas
    y los valores

    """

    ic(df.index)
    ic(df.columns)
    ic(df.values)

    """
    A su vez, podemos extraer la informacion del dataframe utilizando los
    indices que modificamos, teniendo cuidado de llamarlos en las mismas
    caracteristicas en las que fueron escritos. Pära traer mas de un índice,
    estos deben ser representados dentro de una lista

    """

    ic(df['edad'])
    ic(df[['edad', 'pais', 'Q2']])

    """
    Si se desea extraer segmentos de información que involucren tanto
    filas como columnas, usaremos la funcion loc, en donde, partiendo
    del mismo principio de usar corchetes y listas, indicaremos
    primero que indices requerimos para posteriormente seleccionar
    las columnas

    """

    ic(df.loc['camilo', 'Q1'])
    ic(df.loc['camilo', ['Q1', 'pais', 'cm']])
    ic(df.loc[['camilo', 'gabriela'], ['Q1', 'pais', 'cm', 'Q2']])
    ic(df.loc[:, ['Q1', 'pais', 'cm', 'Q2']])

    """
    Ahora bien, la extraccion de información puede llevarse a cabo de igual
    forma bajo el concepto de la posicion, tomando en cuenta la numeriacion
    que inicia en 0 y asciende. Esto se realiza de la misma forma que con
    la funcion loc, sin embargo, para la posicion usaremos iloc

    Usar el simbolo : nos indica que tomaremos todos los elementos, esto
    aplica tanto para loc como para iloc

    """

    ic(df.iloc[2, 4])
    ic(df.iloc[2, [4, 2, 1]])
    ic(df.iloc[[2, 6], [4, 2, 1, 5]])
    ic(df.iloc[:, [4, 2, 1, 5]])

    """
    Dentro de la manejabilidad del dataframe, tambien se pueden pedir valores
    que atiendan a condiciones, mismas que responden a resultados logicos con
    respecto a indices, campos y/o valores evaluados. Estas evaluaciones, a su
    vez, pueden agruparse por medio de operadores lógicos para tener diferentes
    condiciones de consulta.

    Esta composicion de condiciones resulta practica puesto que se ve 
    de manera clara coom se van realizando las agrupaciones.
    
    De cualquier manera, existe una funcion llamada query que tiene la misma
    forma de operar y recibe las condiciones de manera directa.  La diferencia
    radica en que el primer metodo te puede dar la revision booleana, muy util
    para ser usado como comparación en proceso ciclicos y el segundo, no

    Por ultimo, tomado de los comentarios, la funcion info regresa el detalle
    de información del dataframe, mientras que describe, regresa funciones
    de valor para datos numericos de manera general
    
    """

    ic(df['edad'] >= 12)
    ic(df[df['edad'] >= 12])
    ic(df[(df['edad'] >= 12) & (df['genero'] == 'M')])
    ic(df.query('edad >= 12'))
    ic(df.query('(edad >= 12) & (cm < 130) & (genero == "M")'))
    print('')
    ic(df.info())
    ic(df.describe())


if __name__ == '__main__':
    run()

