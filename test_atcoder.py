# https://atcoder.jp/contests/abc160/tasks/abc160_a

def answer(S: list) -> str:
    if S[2] == S[3] and S[4] == S[5]:
        return ("Yes")
    else:
        return ("No")


def test_入力例1():
    assert answer(['s', 'i', 'p', 'p', 'u', 'u']) == "Yes"


def test_入力例2():
    assert answer(['i', 'p', 'h', 'o', 'n', 'e']) == "No"


def test_入力例3():
    assert answer(['c', 'o', 'f', 'f', 'e', 'e']) == "Yes"
