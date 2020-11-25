# https://atcoder.jp/contests/abc145/tasks/abc145_a

def answer(r: int) -> str:
    return str(r * r)


def test_入力例1():
    assert answer(2) == "4"


def test_入力例2():
    assert answer(100) == "10000"

# def test_入力例3():
#     assert answer() == "0"
