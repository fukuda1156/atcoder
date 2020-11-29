# https://atcoder.jp/contests/abc155/tasks/abc155_a

def answer(A: str, B: str, C: str) -> str:
    if A == B and B != C:
        return "Yes"

    elif B == C and C != A:
        return "Yes"

    elif C == A and A != B:
        return "Yes"

    else:
        return "No"


def test_入力例1():
    assert answer(5, 7, 5) == "Yes"


def test_入力例2():
    assert answer(4, 4, 4) == "No"


def test_入力例3():
    assert answer(4, 9, 6) == "No"


def test_入力例4():
    assert answer(3, 3, 4) == "Yes"

# def test_入力例5():
#     assert answer(0, 3) == "3"
