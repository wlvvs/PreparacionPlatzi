def divisors(num_div):
    div_list = [b for b in range (1, num_div + 1) if num_div % b == 0]
    return div_list
    

def run():
    print('')
    num_div = input('Escribe un número positivo al cual se le calcularán sus divisores:   ')
    assert num_div.isnumeric(), 'Debes ingresar un número positivo'
    print(divisors(int(num_div)))
    

if __name__ == '__main__':
    run()