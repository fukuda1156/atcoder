# https://atcoder.jp/contests/abc157/tasks/abc157_a

def answer(N: int) -> str:
    surplus = N % 2
    truncate = N // 2
    return str(surplus + truncate)


def test_入力例1():
    assert answer(5) == "3"


def test_入力例2():
    assert answer(2) == "1"


def test_入力例3():
    assert answer(100) == "50"
