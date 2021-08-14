from icecream import ic
from car import Car
from account import Account

if __name__ == '__main__':
    print('Hola Mundo')
    
    car = Car('AWS666', Account('Oscar Chaparro', 'CABO861221HDFHLS07'))
    ic(vars(car), vars(car.driver))

    car2 = Car('LOL875', Account('Eduardo Chaparro', 'CAOE861221HDFHLS01'))
    ic(vars(car2), vars(car2.driver))