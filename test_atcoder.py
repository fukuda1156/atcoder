# https://atcoder.jp/contests/abc104/submissions/18430485

def answer(R: int) -> str:
    if 0 <= R < 1200:
        return ("ABC")
    if 1200 <= R < 2800:
        return ("ARC")
    if 2800 <= R:
        return ("AGC")


def test_入力例1():
    assert answer(1199) == "ABC"


def test_入力例2():
    assert answer(1200) == "ARC"


def test_入力例3():
    assert answer(4208) == "AGC"
