from icecream import ic

def run() -> None:
    numerator = int(input("""
DIVISION WITH CLOSURES

Give me a number to be consider as numerator: """))
    repeat_n = make_division_by(numerator)
    denominator = int(input(f"""
Now, give me a number to be divided by {numerator}: """))
    ic(repeat_n(denominator))


def make_division_by(numerator: int) -> float:
    def repeater(denominator: int) -> float:
        assert numerator != 0, 'Zero division is not allowed'
        return denominator / numerator
    return repeater


if __name__ == '__main__':
    run()