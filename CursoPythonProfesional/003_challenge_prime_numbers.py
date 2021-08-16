

# The instruction to validate if all variables are typed is: mypy <script.py> --check-untyped-defs

def run() -> None:
    """
    Prime Number Test

        This program checks a number given by user and return if number
        given is a prime number
    """

    check_number = int(input("""\nPRIME NUMBER TEST
Type a number to know if it is prime: """))
    answer = is_prime(check_number)
    if answer:
        print(f'\n{check_number} is a prime number')
    else:
        print(f'\n{check_number} is not a prime number')


def is_prime(check_number: int) -> bool:
    for i in range(2, check_number):
            if check_number % i == 0:
                return False
    return True


if __name__ == '__main__':
    run()