def answer(a: int, b: int) -> int:
    if a == b:
        return 0
    else:
        return b - a % b

def test_入力例1():
    assert answer(7, 3) == 2


def test_入力例2():
    assert answer(5, 5) == 0


def test_入力例3():
    assert answer(1, 100) == 99


def test_入力例4():
    assert answer(25, 12) == 11
