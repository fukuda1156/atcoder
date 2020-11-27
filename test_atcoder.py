# https://atcoder.jp/contests/abc095/tasks/abc095_a

def answer(S: list) -> str:
    return str(700 + (S.count('o') * 100))


def test_入力例1():
    assert answer(['o', 'x', 'o']) == "900"


def test_入力例2():
    assert answer(['o', 'o', 'o']) == "1000"


def test_入力例3():
    assert answer(['x', 'x', 'x']) == "700"
