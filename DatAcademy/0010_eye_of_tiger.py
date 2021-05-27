'''
Aquí se crea el modelo de regresión lineal
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import psycopg2 as pg2
import numpy as np
from configparser import ConfigParser
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def config(filename='./files/database.ini', section='postgresql'):
    # Se crea un parser, que analiza sintácticamente, en este caso, un archivo
    parser = ConfigParser()
    # La función de parser lee el archivo de configuraciones
    parser.read(filename)

    # Se busca y obtiene la sección de la conexión en postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('La sección {0} no fue encontrada en el archivo de configuracion {1}'.format(section, filename))

    return db


def connect():
    """ Se establece la conexión a la BD """
    conn = None
    try:
        # Se lee la configuración establecida vía archivo
        params = config()
        # Se realiza la conexión a la BD
        conn = pg2.connect(**params)
        # Se crea un cursor con la conexión configurada
        cur = conn.cursor()
        # Se ejecuta una consulta
        cur.execute('SELECT id, peso FROM plan_ocb po ORDER BY id')

        # Se guarda la salida en la variable de manejo del cursor
        all_rows = cur.fetchall()
        # Se crea un ciclo para generar con la salid del query, un diccionario
        query = []
        for row in all_rows:
            query_tmp = {"id":row[0], "peso":row[1]}
            query.append(query_tmp)
        return query
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, pg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # Se cierra la conexión, buena práctica
            conn.close()


def run():
    
    query = connect()
    df = pd.DataFrame.from_dict(query)
    X = df['id'].values
    Y = df['peso'].values
    X = X.reshape(-1, 1)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
    reg = LinearRegression()
    reg.fit(X_train, Y_train)
    ## Convierte la vista en lista, tipo arreglo
    x_flat = X_train.flatten()
    
    '''
    Se realiza el cálculo de la prediccion, para determinar cual es la recta que pasa por los hits de modelo
    Estos valores se calculan para observar gráficamente los resultados en la muestra de entrenamiento'
    '''
    y_hat = reg.predict(X_train)
    # Se usa para incluir en el mismo entorno gráfico dos elementos
    fig, ax = plt.subplots()
    # Se grafican los puntos aislados del entrenamiento
    sns.scatterplot(x = x_flat, y = Y_train)

    # Se calcula el ECM
    # Se realiza el cálculo de la prediccion
    # Estos valores se calculan para observar gráficamente los resultados en la muestra de prueba
    y_pred = reg.predict(X_test)
    
    '''El cálculo del error cuadrático medio puede variar entre cada ejemplo, esto es porque las muestras
    rabajadas para el entrenamiento y prueba las conjunta python de manera aleatoria
    El profesor obtuvo 20.13
    '''
    m = reg.coef_
    b = reg.intercept_

    print('')
    print('El valor del error cuadrático medio es de : ',mean_squared_error(Y_test, y_pred))
    values = pd.DataFrame({'Actual_test': Y_test.flatten(), 'Predict': y_pred.flatten()})
    print('')
    print('La extraccion de los registros para ver el error cuadrático medio')
    print(values)
    print('')
    print('La pendiente es: ',m)
    print('El bias es: ', b)
    print('')
    # Se grafica la recta de prediccion
    plt.plot(X_train, y_hat, color = 'r')
    plt.show()
    

if __name__ == '__main__':
    run()