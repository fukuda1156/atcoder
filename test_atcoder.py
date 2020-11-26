# https://atcoder.jp/contests/abc088/tasks/abc088_a

def answer(N: int, A: int) -> str:
    if N % 500 - A <= 0:
        return "Yes"
    else:
        return "No"


def test_入力例1():
    assert answer(2018, 218) == "Yes"


def test_入力例2():
    assert answer(2763, 0) == "No"


def test_入力例3():
    assert answer(37, 514) == "Yes"
