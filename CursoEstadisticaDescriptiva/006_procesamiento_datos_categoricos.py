from icecream import ic
import pandas as pd
import sklearn.preprocessing as preprocessing

dir_pandas = './files/{}'

def run():
    df = pd.read_csv(dir_pandas.format('cars.csv'))
    ic(df.info())
    ic(df.sample(5))
    """
    Al usar la funcion de pandas get_dummies, se genera una columna nueva por
    cada una de las categorias del campo que indicamos a la conversion. En el 
    caso practico del ejemplo, son 3 categorias y en coincidencia de cada una
    de ellas, se guardara en la columna un 1, mientras que en donde no haya
    coincidencia, se guardara un 0.
    De manera resumida y funcional, esto tiene el mismo comportamiento que
    One-Hot, con la diferencia de que no hay una opción de excepcion
    
    """
    ic(pd.get_dummies(df['engine_type']))

    """
    Ahora, usando las funciones de preprocesamiento de sklearn, se usa la 
    funcion one hot encoder, en donde se especifica ademas que, cuando se 
    obtengan valores que no corresponden a la categoria inicial de la
    columna, se ignoren estos valores.

    Primero se inicializa el proceso del encoder con las caracteristicas 
    que vamos a usar.
    Despues, se ajusta el encoder con respecto a los valores del campo dentro
    del dataframe que vamos a usar, en este caso, el tipo de combustible.
    Por ultimo, se realiza la transformacion con respecto a las categorias.
    En este ultimo punto, se coloca una categoria no existente para verificar
    los resultados arrojados y se aprecia que para este punto, tenemos el
    arreglo de ceros, es decir, un valor fuera de nuestras categorias y que,
    por la realizacion de dicha conversion, no genera errores dentro del
    flujo de ejecucion
    
    """
    encoder = preprocessing.OneHotEncoder (handle_unknown = 'ignore')
    encoder.fit(df[['engine_type']].values)
    ic(encoder.transform([['gasoline'], ['diesel'], ['aceite']]).toarray())

    """
    Los campos no categoricos tambien pueden ser tomados, a su vez, como
    categorias.
    Y en este punto justamente es en donde se aprecia una de las desventajas
    del metodo one hot, y esto es que, como parte de la categorizacion de
    valores en columnas, las columnas adheridas a nuestro dataframe crecen
    a razon del numero de categorias distintas en nuestra columna.
    Lo que abre las puertas a un nuevo tema que es la reducción de valores
    
    """
    encoder.fit(df[['year_produced']].values)
    ic(encoder.transform([[2006], [2010], [3000]]).toarray())


if __name__ == '__main__':
    run()
