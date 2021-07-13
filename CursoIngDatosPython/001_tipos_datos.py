from icecream import ic
from datetime import datetime
from PIL import Image

def run():
    print('Datos estructurados\n')

    integer_type = 42
    float_type = 3.14159
    bool_type = False
    hex_type = 0xff
    oct_type = 0o23
    today = datetime.now()
    str_type = 'Oscar'
    image = Image.open('./files/test.jpg')

    ic(type(integer_type), integer_type)
    ic(type(float_type), float_type)
    ic(type(bool_type), bool_type)
    ic(type(hex_type), hex_type)
    ic(type(oct_type), oct_type)
    ic(type(today), today)
    ic(type(str_type), str_type)
    ic(type(image))
    image.show()
    """
    Como dato curioso, los datos que se ingresan como valores hexadecimales y
    octales, al ser impresos en pantalla aparecen en su valor entero, de igual
    forma, el tipo de la variable que los contiene es considerada como entero
    
    """


if __name__ == '__main__':
    run()