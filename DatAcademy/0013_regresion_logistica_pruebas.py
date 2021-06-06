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
    data, target = fetch_openml('mnist_784', version = 1, return_X_y = True, as_frame = False)
    
    x_train, x_test, y_train, y_test = train_test_split(data, target,
    train_size = TRAIN_SAMPLES, test_size = TEST_SIZE,
    random_state = RANDOM_ST)
    
    clf = LogisticRegression(solver = 'saga', tol = 0.01)
    pipe = make_pipeline(StandardScaler(), clf)

    pipe.fit(x_train,y_train)
    score = pipe.score(x_test, y_test)

    predictions = pipe.predict(x_test)
    
    cm = metrics.confusion_matrix(y_test, predictions)
    ic(cm)
    plt.figure(figsize = (9, 9))
    plt.title(f'Puntaje de precisión: {score}', fontsize = 15)
    plt.xlabel("Valor de predicción")
    plt.ylabel("Valor de actual")
    sns.heatmap(cm, annot = True, linewidths = 0.5, square = True, cmap = "ocean_r")
    plt.show()


if __name__ == '__main__':
    run()