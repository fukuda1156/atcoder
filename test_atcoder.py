# https://atcoder.jp/contests/abc150/tasks/abc150_a

def answer(K: int, X: int) -> str:
    if 500 * K >= X:
        return ("Yes")
    else:
        return ("No")


def test_入力例1():
    assert answer(2, 900) == "Yes"


def test_入力例2():
    assert answer(1, 501) == "No"


def test_入力例3():
    assert answer(4, 2000) == "Yes"
