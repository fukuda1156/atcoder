def answer(A: int, P: int) -> int:
    return (A * 3 + P) // 2


def test_入力例1():
    assert answer(1, 3) == 3


def test_入力例2():
    assert answer(0, 1) == 0


def test_入力例3():
    assert answer(32, 21) == 58

# def test_入力例4():
#     assert answer(50) == 625
