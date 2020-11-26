# https://atcoder.jp/contests/abc183/tasks/abc183_a

def answer(x: int) -> str:
    if x >= 0:
        return str(x)
    if x < 0:
        return str(0)

def test_入力例1():
    assert answer(1) == "1"

def test_入力例2():
    assert answer(0) == "0"


def test_入力例3():
    assert answer(-1) == "0"
