from icecream import ic
from typing import Tuple, Dict, List

ic.configureOutput(includeContext = True)

def suma(a: int, b: int) -> int:
    return a + b


def run():
    valor1: int = 5
    valor2: int = 6
    valor3: str = 'Valor str'
    valor4: bool = True

    print("""\nLa definición de los valores se ataca de inicio indicando con : el tipo
de dato de la variable\n""")
    ic(valor1 + valor2)
    ic(type(valor1 + valor2))
    ic(valor3)
    ic(type(valor3))
    ic(valor4)
    ic(type(valor4))

    print("""\n\nEste concepto puede aplicarse de igual forma a una función, sin embargo,
en este caso tendremos un problema debido a que python responde correctamente
al momento de lanzar la petición con tipos de datos diferentes al entero, haciendo
que la configuración de tipado estático no aplique en todos los casos\n""")
    ic(suma(1, 5))
    ic(type(suma(1, 5)))
    ic(suma('1', '5'))
    ic(type(suma('1', '5')))

    list_positives: List[int] = [5, 10, 15, 20]
    dict_users: Dict[str, int] = {
        'Argentina': 23,
        'Mexico': 34,
        'Colombia': 45
    }
    list_countries:Dict[str, int] = [
        {
            'name': 'Argentina',
            'people': 4512000
        },
        {
            'name': 'Mexico',
            'people': 7548000
        },
        {
            'name': 'Colombia',
            'people': 6401200
        }
    ]

    print("""\n\nDe igual forma, es aplicable para la definición de listas y diccionarios,
pero en este caso se usa la libreria typing para traer los tipos de datos
relacionados\n""")
    ic(list_positives)
    ic(type(list_positives))
    ic(dict_users)
    ic(type(dict_users))
    ic(list_countries)
    ic(type(list_countries))

    CoordinatesType = List[Dict[str, Tuple[int, int]]]
    list_coordinates: CoordinatesType = [
        {
            "coord1": (1,2),
            "coord2": (3,5)
            },
        {
            "coord1": (0,1),
            "coord2": (2,5)
        }
    ]

    print("""\n\nLa ultima estructura es una combinación de tipos de tipado en la
que se aprecia que de igual forma, se respetan las caracteristicas
definidas\n""")
    ic(list_coordinates)
    ic(type(list_coordinates))


if __name__ == '__main__':
    run()