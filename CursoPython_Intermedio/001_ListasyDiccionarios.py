"""
Programa para revisar conceptos de listas y diccionarios anidados.
Como ya sabemos, una lista es un conjunto de elementos 'simples' de
tipos variables. Mientras que un diccionario es una colección de
elementos, identificando cada uno de ellos con una llave.
"""

def run():
    my_list = [21, "Día", True, 98.7]
    my_dict = {"firstname": "Oscar", "lastname": "Chaparro"}

    dict_list = [
        {"firstname": "Oscar", "lastname": "Chaparro"},
        {"firstname": "Eduardo", "lastname": "Blancas"},
        {"firstname": "Nahayeli", "lastname": "López"}
    ]

    list_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floatign_nums": [1.1, 5.6, 8.09, 7.002]
    }

    print('Estos son los valores de la lista de diccionarios')
    for key, value in list_dict.items():
        print(key, "tiene el valor", value)

    print('Estos son los valores del diccionario de listas')
    for item in dict_list:
        print('Nombre:',item["firstname"], item["lastname"])


if __name__ == '__main__':
    run()