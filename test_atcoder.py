# https://atcoder.jp/contests/abc184/tasks/abc184_a

def answer(a: int, b: int, c: int, d: int) -> str:
    return str((a * d) - (b * c))


def test_入力例1():
    assert answer(1, 2, 3, 4) == "-2"


def test_入力例2():
    assert answer(0, -1, 1, 0) == "1"


def test_入力例3():
    assert answer(100, 100, 100, 100) == "0"
