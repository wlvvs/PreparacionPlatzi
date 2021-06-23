from icecream import ic
import pandas as pd

def run():
    df_left = pd.DataFrame(
        {'X': ['x0', 'x1', 'x2', 'x3'],
        'W': ['w0', 'w1', 'w2', 'w3'],
        'Y': ['y0', 'y1', 'y2', 'y3'],
        'Mix': ['y2', 'y3', 'a2', 'a3']
        }, index=[0, 1, 2, 3])

    df_left_2 = pd.DataFrame(
        {'X': ['x0', 'x1', 'x2', 'x3'],
        'W': ['w0', 'w1', 'w2', 'w3'],
        'Y': ['y0', 'y1', 'y2', 'y3']
        }, index=[0, 1, 2, 3])

    df_left_3 = pd.DataFrame(
        {'X': ['x0', 'x1', 'x2', 'x3'],
        'W': ['w0', 'w1', 'w2', 'w3'],
        'Y': ['y0', 'y1', 'y2', 'y3'],
        'A': ['a0', 'a1', 'a2', 'a3']
        }, index=[0, 1, 2, 3])

    df_right = pd.DataFrame(
        {'Z': ['z2', 'z3', 'z4', 'z5'],
        'A': ['a2', 'a3', 'a4', 'a5'],
        'Y': ['y2', 'y3', 'y4', 'y5']
        }, index=[2, 3, 4, 5])
    
    ic(df_left)
    ic(df_left_2)
    ic(df_left_3)
    ic(df_right)
    """
    El merge funciona como lo haria el cruce de consultas en una base de datos.
    De la misma manera, se puede determinar si se realiza el cruce por izquierda,
    por derecha y que campos son los que indexaran la busqueda.
    Por defecto, pandas identifica el sufijo como x y y para el analisis de
    datos por izquierda y derecha respectivamente, pero nosotros podemos
    hacer el reajuste para que sea mas conveniente a nuestro entendimiento.

    El merge es muy importante para poder integrar y optimizar los 
    universos de datos bajo los cuales estaremos trabajando

    """
    ic(pd.merge(df_left, df_right))
    ic(pd.merge(df_left, df_right, how = 'inner', on = 'Y'))
    ic(pd.merge(df_left, df_right, how = 'inner', left_on = 'Mix', right_on = 'Y'))
    ic(pd.merge(df_left, df_right, how = 'inner', left_on = 'Mix', right_on = 'A'))

    ic(pd.merge(df_left_2, df_right, how = 'inner', on = 'Y'))
    ic(pd.merge(df_left_2, df_right, how = 'left', on = 'Y'))
    ic(pd.merge(df_left_2, df_right, how = 'right', on = 'Y'))
    ic(pd.merge(df_left_2, df_right, how = 'outer', on = 'Y'))

    ic(pd.merge(df_left_3, df_right, how = 'outer', on = ['Y', 'A']))
    ic(pd.merge(df_left_3, df_right, how = 'outer'))
    ic(pd.merge(df_left_3, df_right, how = 'outer', on = 'A'))
    ic(pd.merge(df_left_3, df_right, how = 'outer', on = 'A', suffixes=['_left', '_right']))


if __name__ == '__main__':
    run()