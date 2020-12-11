# https://atcoder.jp/contests/abc165/tasks/abc165_b
def answer(X: int) -> str:
    deposit = 100
    years = 0
    while deposit < X:
        deposit += deposit // 100
        years += 1
    return str(years)


def test_入力例1():
    assert answer(103) == "3"


def test_入力例2():
    assert answer(1000000000000000000) == "3760"


def test_入力例3():
    assert answer(1333333333) == "1706"

# https://atcoder.jp/contests/abc094/tasks/abc094_b
# def answer(N: int, M: int, X: int, A(list)) -> str:
#
#
# def test_入力例1():
#     assert answer(5, 3, 3, [1, 2, 4]) == "1"
#
#
# def test_入力例2():
#     assert answer(7, 3, 2, [4, 5, 6]) == "0"
#
#
# def test_入力例3():
#     assert answer(10, 7, 5, [1, 2, 3, 4, 6, 8, 9]) == "3"

# def test_入力例4():
#     assert answer() == ""

# def test_入力例5():
#     assert answer() == ""

# f(*list)
