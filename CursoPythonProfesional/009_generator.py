from icecream import ic
import time

def fibo_gen():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    value = input('''
FIBONACCI ITERATOR

I'm gonna print all values of the Fibonacci sequence until I reach the number you want.
If you wanna see an infinite sequence, press 0. If not, press any other number.
Give me the number: ''')

    fibonacci = fibo_gen()
    for element in fibonacci:
        if element < int(value) or int(value) == 0:
            ic(element)
            time.sleep(0.5)
        else:
            break