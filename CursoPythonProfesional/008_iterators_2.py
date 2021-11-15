from icecream import ic
from time import sleep

class FiboIter():
    
    def __init__(self, max = None):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
        
    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter ==1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            self.counter += 1
            self.n1, self.n2 = self.n2, self.aux
            if not self.max:
                return self.n2

            if self.max:
                if self.aux > int(self.max):
                    raise StopIteration
                else:
                    return self.n2


if __name__ == '__main__':
    value = input('''
FIBONACCI ITERATOR

I'm gonna print all values of the Fibonacci sequence until I reach the number you want.
If you wanna see an infinite sequence, press 0. If not, press any other number.
Give me the number: ''')
    if int(value) == 0:
        value = None

    for element in FiboIter(value):
        ic(element)
        sleep(0.5)