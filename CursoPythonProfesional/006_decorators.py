from datetime import datetime

def run()-> None:
    print('DECORATORS TEST\n')
    print('\nWe are running test of decorators with time. No arguments where given')
    random_func()
    number1, number2 = input('\nNow, I need you give me two integer values separated by an space: ').split()
    number2 = int(number2)
    number1 = int(number1)
    sum_result = sum_func(number1, number2)
    print('The sum {} + {} = {}'.format(number1, number2, sum_result))


def execution_time(func):
    def wrapper(*args, **kargs):
        initial_time = datetime.now()
        func(*args, **kargs)
        final_time = datetime.now()
        elapsed_time = final_time - initial_time
        print(f'The elapsed time was {elapsed_time.total_seconds()} seconds')
    return wrapper


@execution_time
def random_func():
    for _ in range (1,1000000):
        pass


@execution_time
def sum_func(n1:int, n2:int) -> int:
    return n1 + n2


if __name__ == '__main__':
    run()