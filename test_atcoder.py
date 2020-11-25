# https://atcoder.jp/contests/abc145/tasks/abc145_a

def answer(r: int) -> str:
    return str(3 * r * r)


def test_入力例1():
    assert answer(4) == "48"


def test_入力例2():
    assert answer(15) == "675"


def test_入力例3():
    assert answer(80) == "19200"
