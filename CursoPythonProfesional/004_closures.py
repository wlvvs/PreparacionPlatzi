from icecream import ic
from icecream.icecream import NoSourceAvailableError

def run() -> None:
    n = int(input("""
STRING REPEATER

Give me a number of loops you want to repeat a string: """))
    repeat_n = make_repeater_of(n)
    string = input(f"""
Now, give a string to be repeated {n} times: """)
    ic(repeat_n(string))


def make_repeater_of(n: int) -> str:
    def repeater(string: str) -> str:
        assert type(string) == str, 'Only strings are available'
        return string * n
    return repeater


if __name__ == '__main__':
    run()