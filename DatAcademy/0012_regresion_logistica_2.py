import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from icecream import ic

TRAIN_SAMPLES = 20000
TEST_SIZE = 10000
RANDOM_ST = 21

def run():
    """
    Se trata del mismo ejercicio en 0011, pero con el universo
    de datos extendido tanto en elementos de información, target
    y dimensiones de las matrices

    """
    data, target = fetch_openml('mnist_784', version = 1, return_X_y = True, as_frame = False)
    ic(data.shape)
    ic(target.shape)
    digit_sample = data[0]
    ic(digit_sample)
    sample_label = target[0]
    ic(sample_label)
    plt.imshow(digit_sample.reshape(28, 28))
    plt.show()

    numbers_sample = list(zip(data[30:35], target[30:35]))
    ic(np.array(numbers_sample).shape)

    plt.figure(figsize = (16,16))
    for index, (image,label) in enumerate(numbers_sample):
        reshaped_image = np.reshape(image, (28,28))
        plt.subplot(1, len(numbers_sample), index + 1)
        plt.imshow(reshaped_image)
        plt.title(f"L: {label}")
    plt.show()

    """
    Para la fase de entrenamiento, se realiza una segmentación de información, entre
    otras cosas, para reducir tiempo. Pero aun mas importante, necesitamos que la prediccion
    reaccione de manera generalizada. Si se toman los sets completos, tendremos resultados
    correctos de entrenamiento pero el modelo estará entrenado para aquellos valores que
    yacen en el universo total que lo alimenta.
    El objetivo de un modelo y su entrenamiento, es que dicho entrenamiento funcione
    para valores diferentes.
    Cuando el modelo se ajusta completamente a los datos de entrenamiento, se produce
    overfitting, es decir, que el proceso de clasificación funciona de manera optima
    pero para la información que tenemos en entrenamiento.
    Caso contrario, cuando el modelo no se ajusta para nada a los datos de entrenamiento,
    tenemos underfitting. El mundo funciona en equilibrio y aqui aplica lo mismo

    """
    x_train, x_test, y_train, y_test = train_test_split(data, target,
    train_size = TRAIN_SAMPLES, test_size = TEST_SIZE,
    random_state = RANDOM_ST)
    
    print(f'Tamaño de datos de entrenamiento: {len(x_train)}')
    print(f'Tamaño de datos de prueba: {len(x_test)}')

    """
    El solver es un optimizador, esto para encontrar el valor mínimo.
    Funciona en data sets largos y con datos escalados. La tolerancia (tol)
    es que tan lejos en distancia el solver parará la busqueda del mínimo.
    Al colocar ese valor de tolerancia, aseguramos que nuestro proceso de
    entretamiento sea mas rápido y efectivo

    """
    clf = LogisticRegression(solver = 'saga', tol = 0.01)
    pipe = make_pipeline(StandardScaler(), clf)

    pipe.fit(x_train,y_train)
    ic(pipe.fit(x_train,y_train))
    score = pipe.score(x_test, y_test)
    ic(score)

    guinea_pig = x_test[781]
    ic(guinea_pig)
    guinea_pig = guinea_pig.reshape(1, -1)
    ic(guinea_pig)
    ic(pipe.predict(guinea_pig))
    guinea_pig = guinea_pig.reshape(28, 28)
    ic(guinea_pig.reshape(28, 28))
    plt.imshow(guinea_pig)
    plt.show()

    predictions = pipe.predict(x_test)
    ic(predictions)
    ic(len(predictions))

    cm = metrics.confusion_matrix(y_test, predictions)
    ic(cm)
    plt.figure(figsize = (9, 9))
    plt.title(f'Puntaje de precisión: {score}', fontsize = 15)
    plt.xlabel("Valor de predicción")
    plt.ylabel("Valor de actual")
    sns.heatmap(cm, annot = True, linewidths = 0.5, square = True, cmap = "Blues_r")
    plt.show()


if __name__ == '__main__':
    run()