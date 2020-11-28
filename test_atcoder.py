# https://atcoder.jp/contests/abc118/tasks/abc118_a

def answer(A: int, B: int) -> str:
    if B % A == 0:
        return str(A + B)
    else:
        return str(B - A)


def test_入力例1():
    assert answer(4, 12) == "16"


def test_入力例2():
    assert answer(8, 20) == "12"


def test_入力例3():
    assert answer(1, 1) == "2"
