def answer(N: int, K: int) -> int:
    if N % K == 0:
        return 0
    else:
        return 1


def test_入力例1():
    assert answer(7, 3) == 1


def test_入力例2():
    assert answer(100, 10) == 0


def test_入力例3():
    assert answer(1, 1) == 0

# def test_入力例4():
#     assert answer(50) == 625
