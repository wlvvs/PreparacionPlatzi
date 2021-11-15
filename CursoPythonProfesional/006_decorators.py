from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        elapsed_time = final_time - initial_time
        print(f'The elapsed time was {elapsed_time.total_seconds()} seconds')
    return wrapper


@execution_time
def random_func():
    for _ in range (1,10000000):
        pass


@execution_time
def sum_func(n1:int, n2:int) -> int:
    return n1 + n2


def run()-> None:
    print('DECORATORS TEST\n')
    print('\nWe are running test of decorators with time. No arguments where given')
    random_func()
    print('The sum {} + {} = {}'.format(1, 2, sum_func(1,2)))


if __name__ == '__main__':
    run()