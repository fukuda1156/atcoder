# https://atcoder.jp/contests/abc167/tasks/abc167_a

def answer(S: str, T: str) -> str:
    if S == T[0:-1]:
        return "Yes"
    else:
        return "No"

def test_入力例1():
    assert answer("chokudai", "chokudaiz") == "Yes"

def test_入力例2():
    assert answer("snuke", "snekee") == "No"


def test_入力例3():
    assert answer("a", "aa") == "Yes"
