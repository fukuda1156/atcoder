# https://atcoder.jp/contests/abc096/tasks/abc096_b

def answer(ABC: list, K: int) -> str:
    return str(sum(ABC) + (max(ABC) * (2 ** K - 1)))


def test_入力例1():
    assert answer([5, 3, 11], 1) == "30"


def test_入力例2():
    assert answer([3, 3, 4], 2) == "22"


def test_入力例3():
    assert answer([3, 3, 4], 2) == "22"

# def test_入力例4():
#     assert answer() == ""

# def test_入力例5():
#     assert answer() == ""
