# https://atcoder.jp/contests/abc165/tasks/abc165_b

def answer(N: int, K: int) -> str:
    i = 1
    while N >= K ** i:
        i += 1
    return str(i)


def test_入力例1():
    assert answer(11, 2) == "4"


def test_入力例2():
    assert answer(1010101, 10) == "7"


def test_入力例3():
    assert answer(314159265, 3) == "18"
