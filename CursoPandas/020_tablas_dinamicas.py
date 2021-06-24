from icecream import ic
import numpy as np
import pandas as pd
import seaborn as sns

pd.options.display.float_format = '{:,.3f}'.format

def run():
    df = sns.load_dataset('tips')
    df['prct_tip'] = (df['tip'] / df['total_bill']) * 100
    df['ones'] = 1
    df['bin_total'] = pd.cut(df['total_bill'], bins = [3, 18, 35, 60])
    ic(df.describe(include = 'all'))
    ic(df.sample(10))

    """
    Se crea un dataframe por medio de un agrupamiento de datos con respecto
    al promedio de las cuentas, agrupadas por genero y hora de comida

    """
    df_gp = df.groupby(['sex', 'time'])[['total_bill']].mean().reset_index()
    ic(df_gp)

    """
    Se crea una tabla pivote tomando como valores el monto total de la cuenta, como
    indice el genero y como columna la hora de comida, dando como resultados indices multiples

    """
    ic(df_gp.pivot_table(values = 'total_bill', index = 'sex', columns = 'time'))
    """
    La funcion de agregacion por default es el prome

    """
    df_pivot = df.pivot_table(values = 'total_bill', index = 'sex', columns = 'time', aggfunc = [np.median, np.std])
    ic(df.pivot_table(values = 'total_bill', index = 'sex', columns = 'time', aggfunc = [np.median, np.std]))
    ic(df_pivot.unstack())
    ic(df_pivot.unstack().reset_index())


if __name__ == '__main__':
    run()