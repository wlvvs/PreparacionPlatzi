# The instruction to validate if all variables are typed is: mypy <script.py> --check-untyped-defs
from icecream import ic

ic.configureOutput(includeContext = True)

def palindrome(palindrome_text: str) -> bool:
    """
    Palindrome Test
        This program evaluates a string to determine if it is palindrome or not

    """

    return palindrome_text.lower().replace(' ','') == palindrome_text.lower().replace(' ','')[::-1]


def run():
    ic(palindrome('Anita lava la tina'))


if __name__ == '__main__':
    run()