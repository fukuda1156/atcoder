def answer(a: int, b: int) -> str:
    if a * b % 2 == 0:
        return "Even"
    return "Odd"


def test_入力例1():
    assert answer(3, 4) == "Even"


def test_入力例2():
    assert answer(1, 21) == "Odd"
