# https://atcoder.jp/contests/abc103/tasks/abc103_a

def answer(A123: list) -> str:
    return str(max(A123) - min(A123))


def test_入力例1():
    assert answer([1, 6, 3]) == "5"


def test_入力例2():
    assert answer([11, 5, 5]) == "6"


def test_入力例3():
    assert answer([100, 100, 100]) == "0"
