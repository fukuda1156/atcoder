# https://atcoder.jp/contests/abc103/tasks/abc103_a

def answer(N: int, M: int) -> str:
    return str(int(N * (N - 1) / 2 + M * (M - 1) / 2))


def test_入力例1():
    assert answer(2, 1) == "1"


def test_入力例2():
    assert answer(4, 3) == "9"


def test_入力例3():
    assert answer(1, 1) == "0"


def test_入力例4():
    assert answer(13, 3) == "81"


def test_入力例5():
    assert answer(0, 3) == "3"
