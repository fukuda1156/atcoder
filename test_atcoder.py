def answer(n: int, x: int) -> str:
    if x - 1 <= n - x:
        return str(x - 1)
    if x - 1 >= n - x:
        return str(n - x)


def test_入力例1():
    assert answer(5, 2) == "1"


def test_入力例2():
    assert answer(6, 4) == "2"


def test_入力例3():
    assert answer(90, 30) == "29"

# def test_入力例4():
#     assert answer(50) == 625
