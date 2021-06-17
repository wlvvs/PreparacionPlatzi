from icecream import ic
import sqlalchemy as sql
import pandas as pd

"""
Se define una constante con el archivo de configuraciones para generar la conexion.
En este caso, se hace uso de pandas para que dicho archivo sea un csv

"""
CONFIG = './files/database_conf.csv'

def connect():

    """
    Se lee el archivo de configuraciones y se extraen los valores, mismos
    con los que se genera la cadena de conexión que se le pasará a sqlalchemy

    """
    df = pd.read_csv(CONFIG)
    database_type = df.iloc[5, 1]
    user = df.iloc[0, 1]
    password = df.iloc[1, 1]
    host = df.iloc[2, 1]
    database = df.iloc[3, 1]
    port = df.iloc[4, 1]

    conn_string = '{}://{}:{}@{}:{}/{}'.format(database_type, user, password, host, port, database)

    """
    El origen de datos es una base en postgres. Pese a que se usa la 
    libreria de sqlalchemy, manda un error debido a que no encuentra un driver
    valido de conexión, por lo que es necesario instalar psycopg2
    Esta libreria contiene los drivers de conexion, por lo que, si se 
    requiere, en este caso no es necesario instalar sqlalchemy, basta
    con psycopg2 y en tal caso, usar la plantilla de conexión que nos
    proporciono el profesor en el documento de clase

    """
    conn = sql.create_engine(conn_string)
    query_sql = 'SELECT * FROM plan_ocb po ORDER BY id'
    query_result = pd.read_sql(query_sql, conn)
    
    ic(query_result)
    
    dir_pandas = './files/{}'.format('select_from_postgresql.csv')
    query_result.to_csv(dir_pandas, index = False)


if __name__ == '__main__':
    connect()