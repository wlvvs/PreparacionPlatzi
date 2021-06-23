from ntpath import join
from icecream import ic
import pandas as pd
import numpy as np

"""
Estas expresiones son homologas y nos permiten indicar la precision numerica
de nuestros datos como una configuracion default. La primera usa elementos
propios de pandas y la segunda, de numpy

"""
pd.options.display.float_format = '{:.2f}'.format
np.set_printoptions(precision = 2)

def run():
    """
    Dentro de numpy, se generan dos matrices aleatorias para trabajar
    con el concepto de concatenacion

    """
    x1 = np.random.rand(2, 5) * 10
    x2 = np.random.rand(2, 5) * -1
    
    ic(x1)
    ic(x1.shape)
    ic(x2)
    ic(x2.shape)
    """
    Con el comando concatenate, unimos las matrices previamente creadas.
    Es importante recalcar que, para cambiar el sentido de la concatenacion,
    lo que se tiene que hacer es indicar el eje sobre el cual se
    requiere trabajar

    """
    ic(np.concatenate([x1, x2]))
    ic(np.concatenate([x1, x2]).shape)
    ic(np.concatenate([x1, x2], axis = 1))
    ic(np.concatenate([x1, x2], axis = 1).shape)

    """
    Partiendo de pandas, se definen dos series con indices diferentes de
    manera intencional, de tal forma que, la hacer el proceso de 
    concatenacion, veamos que los indices forman parte importante
    del proceso, ya que se usan como parte de los parametros para
    unir la informacion.
    De igual forma, para cambiar el sentido de la concatenacion, estamos
    en posibilidad de elegir el eje base y algo importante, es que 
    tambien podemos hacer un reinicio de indices para que estos
    no sean tomados en cuenta y la concatenacion se de de manera
    completa

    """
    s1 =  pd.Series(x1[0], index = ['a', 'b', 'c', 'd', 'e'])
    ic(s1)
    s2 =  pd.Series(x2[0], index = ['c', 'd', 'e', 'f', 'g'])
    ic(s2)
    ic(pd.concat([s1, s2]))
    ic(pd.concat([s1, s2], axis = 1))
    ic(pd.concat([s1, s2], axis = 1))
    ic(s1.reset_index(drop = True))
    ic(pd.concat([s1.reset_index(drop = True), s2.reset_index(drop = True)], axis = 1))

    """
    Los mismos conceptos en series aplican de manera similar para dataframes, 
    en donde ademas se introduce el concepto de uniones tipo consulta de sql,
    ya que podemos usar uniones tipo inner y outer, aunque esto se vera mas
    adelante y de forma explicita con los merges.
    
    Tambien podemos usar el concepto de trasposicion de matrices para hacer 
    un giro completo de ejes y tener la información de los dataframes
    de la manera que mas nos convenga

    Esto es muy util debido a que al momento de almancenar informacion, es
    posible que esta se encuentre en diferentes origenes y de forma segmentada,
    lo que nos brinda la posibilidad de unir esa informacion en un dataframe
    unico para poder trabajarlo

    """
    df1 = pd.DataFrame(np.random.rand(3, 2) * 10, columns=['a', 'b'])
    df2 = pd.DataFrame(np.random.rand(3, 2) * -1, columns=['a', 'b'], index = [2, 3, 4])
    ic(df1)
    ic(df2)
    ic(pd.concat([df1, df2]))
    ic(pd.concat([df1, df2], axis = 1))
    ic(pd.concat([df1, df2], axis = 1, join = 'inner'))
    ic(pd.concat([df1, df2], axis = 1, join = 'outer')) # Este es el join default
    ic(pd.concat([df1, df2], axis = 1))
    ic(pd.concat([df1.reset_index(drop = True), df2.reset_index(drop = True)], axis = 1))
    ic(df1.append(df2).append(df1))
    ic(df1.T.append(df2.T).append(df1.T).T)


if __name__ == '__main__':
    run()