# https://atcoder.jp/contests/abc145/tasks/abc145_a

def answer(C: str) -> str:
    return (chr(ord(C) + 1))


def test_入力例1():
    assert answer("a") == "b"


def test_入力例2():
    assert answer("y") == "z"

# def test_入力例3():
#     assert answer(80) == "19200"
