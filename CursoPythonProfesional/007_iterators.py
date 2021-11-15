from icecream import ic
import time

class FiboIter():
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0

        return self


    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            
            '''
            Estas lineas son resumidas usando swapping, que es la linea que me permite
            realizar ambas acciones de reemplazo en una sola
            
            self.n1 = self.n2
            self.n2 = self.aux
            '''
            
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.n2


if __name__ == '__main__':
    value = input('''
FIBONACCI ITERATOR

I'm gonna print all values of the Fibonacci sequence until I reach the number you want.
If you wanna see an infinite sequence, press 0. If not, press any other number.
Give me the number: ''')

    fibo = FiboIter()
    for element in fibo:
        if element < int(value) or int(value) == 0:
            ic(element)
            time.sleep(0.5)
        else:
            break
