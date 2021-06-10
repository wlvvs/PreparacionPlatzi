from icecream import ic
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def group_assignment(data,centroids):
    """
    Función de asignación de grupo:
    Aqui se asignan a los vectores mas cerca del grupo representativo
    como integrantes del grupo

    Se revisa toda la información para evaluar la distancia con respecto
    al punto representativo. Se toma la mínima, se asigna su centroide
    y así se forman todos los grupos

    """
    grouping_vec_c = np.zeros(len(data))
    for i in range(len(data)):
        dist = np.zeros(len(centroids))
        for j in range(len(centroids)):
            dist[j] = np.linalg.norm(data[i] - centroids[j])
        min_dist = min(dist)
        for j in range(len(centroids)):
            if min_dist == dist[j]:
                grouping_vec_c[i] = j+1
    return grouping_vec_c


def update_centroid(data, grouping, centroids):
    """
    Función de actualizacoón de centroide.
    El centoride es el punto que se asigna como el central representativo.
    Lo que hace la función es barrer toda la data, evaluando que esta
    pertenezca al grupo en cuestión. Después, para toda la data perteneciente
    al grupo, genera un nuevo universo y lo promedia.
    El valor promedio de dicho universo de datos será el nuevo
    centroide
    
    """
    new_centroids = [];
    for i in range(len(centroids)):
        cent = np.zeros(len(data[0]))
        count = 0
        for j in range(len(data)):
            if grouping[j] == (i+1):
                cent = cent+data[j]
                count += 1
        group_average = cent/count
        new_centroids.append(group_average)
    return new_centroids


def clustering_objective(data, grouping, centroids):
    """
    ESta función calcula las distancias entre los puntos
    referenciados en el centroide, para asi, porder hacer
    la clasificacion
    
    """
    J_obj = 0
    for i in range(len(data)):
        for j in range(len(centroids)):
            if grouping[i] == (j+1):
                J_obj += np.linalg.norm(data[i] - centroids[j])**2
    J_obj = J_obj / len(data)
    return J_obj


def Kmeans_alg(data, centroids):
    """
    Aqui se realiza el ensable de todo el proceso

    """
    iteration = 0
    J_obj_vector = []
    Stop = False
    while Stop == False:
        grouping = group_assignment(data, centroids)
        new_centroids = update_centroid(data, grouping, centroids)
        J_obj = clustering_objective(data, grouping,new_centroids)
        J_obj_vector.append(J_obj)
        iteration += 1
        if np.linalg.norm(np.array(new_centroids) - np.array(centroids)) < 1e-6:
            Stop = True
        else:
            centroids = new_centroids
    return new_centroids, grouping, J_obj_vector, iteration


def run():
    fig, ax = plt.subplots(1, 1, figsize = (7, 7),dpi = 120)
    X = np.concatenate([[0.3 * np.random.randn(2) for i in range(100)],\
                        [[1, 1] + 0.3 * np.random.randn(2) for i in range(100)], \
                        [[1, -1] + 0.3 * np.random.randn(2) for i in range(100)]])
    ax.scatter(X[:,0], X[:,1])
    ax.set_xlim(-1.5, 2.5)
    ax.set_ylim(-2, 2)
    plt.show()

    A = Kmeans_alg(X,X[:3])

    gruping = A[1].reshape(-1,1)
    arr = np.concatenate((X, gruping),axis=1)

    df = pd.DataFrame(arr,columns=['x', 'y', 'group'])

    fig,ax= plt.subplots(1,1,figsize=(7,7),dpi=300)
    sns.scatterplot(x='x',y='y',hue='group',data=df, palette='deep')
    for i in A[0]:
        ax.scatter(i[0],i[1],c='black',linewidths=3)
    plt.show()


if __name__ == '__main__':
    run()