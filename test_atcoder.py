def answer(A: int, B: int, T: int) -> int:
    return (T // A) * B


def test_入力例1():
    assert answer(3, 5, 7) == 10


def test_入力例2():
    assert answer(3, 2, 9) == 6


def test_入力例3():
    assert answer(20, 20, 19) == 0

# def test_入力例4():
#     assert answer(50) == 625
