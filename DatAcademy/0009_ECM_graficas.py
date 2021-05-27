'''
Aquí se crea el modelo de regresión lineal
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    
    df = pd.read_csv('./files/StudentsPerformance.csv')
    
    X = df['reading score'].values
    Y = df['writing score'].values

    X = X.reshape(-1, 1)

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
    
    from sklearn.linear_model import LinearRegression
    
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

    '''Se calcula el ECM
    Se importa de la libreria la funcion que realiza ese cálculo
    '''
    from sklearn.metrics import mean_squared_error
    
    # Se realiza el cálculo de la prediccion
    # Estos valores se calculan para observar gráficamente los resultados en la muestra de prueba
    y_pred = reg.predict(X_test)
    
    '''El cálculo del error cuadrático medio puede variar entre cada ejemplo, esto es porque las muestras
    rabajadas para el entrenamiento y prueba las conjunta python de manera aleatoria
    El profesor obtuvo 20.13
    '''
    print('')
    print('El valor del error cuadrático medio es de : ',mean_squared_error(Y_test, y_pred))
    values = pd.DataFrame({'Actual_test': Y_test.flatten(), 'Predict': y_pred.flatten()})
    print('')
    print('La extraccion de 5 regisros para ver el error cuadrático medio')
    print(values.head(5))
     
    # Se grafica la recta de prediccion
    plt.plot(X_train, y_hat, color = 'r')
    plt.show()
    

if __name__ == '__main__':
    run()