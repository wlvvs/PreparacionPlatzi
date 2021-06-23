from icecream import ic
import pandas as pd

def run():
    """
    Dentro de los datos, es importante saber como localizar y controlar la 
    presencia de datos duplicados.
    La funcion duplicated indica en modo booleano que combinacion de datos
    dentro del dataframe se encuentran duplicados.
    Para marcar con respecto al orden de revision, dentro de la funcion 
    duplicated se indica el parametro keep

    La virgulilla representa el caso negado y la usamos en los ejemplos
    para traer los datos del dataframe en donde no tenemos duplicidad.
    Se marcan los casos first y last para que, por medio de los indices
    del dataframe, veamos que valores son los que se preservan y cuales 
    se discriminan. Esto es importante, por ejemplo, en temas de base
    de datos por el manejo de identificadores

    Dentro de duplicated, cuando usamos el valor False como valor al
    atributo keep, tendremos por respuesta los casos duplicados. 
    Anteriormente los estabamos quitando

    Con la funcion drop duplicates eliminaremos la seleccion de 
    duplicados regidos por el keep default (first), a menos que lo
    cambiemos a last y, de igual forma, podemos basarnos en una columna
    especifica del dataframe para realizar la eliminación de valores
    duplicados

    Recordar que inplace hace efectivo el cambio dentro del dataframe
    base

    """
    df = pd.DataFrame({
        'a': ['w'] * 4 + ['x'] * 3 + ['y'] * 2 + ['z'] + ['v'],
        'b': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4, 5]
        })
    ic(df)
    ic(df.duplicated()) # El keep por default es first
    ic(df.duplicated(keep = 'first'))
    ic(df.duplicated(keep = 'last'))
    ic(df[~ df.duplicated(keep = 'first')])
    ic(df[~ df.duplicated(keep = 'last')])
    ic(df.duplicated(keep = False))
    ic(df[df.duplicated(keep = False)])
    ic(df.drop_duplicates(keep = 'first'))
    ic(df.drop_duplicates(keep = 'last'))
    ic(df.drop_duplicates(['a'], keep ='last'))
    ic(df.drop_duplicates(['a'], keep ='first', inplace = True))
    ic(df)



if __name__ == '__main__':
    run()