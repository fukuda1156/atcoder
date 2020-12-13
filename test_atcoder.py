# https://atcoder.jp/contests/abc068/tasks/abc068_b
def answer(N: int) -> str:
    for i in range(N, 0, -1):
        if i == 1:
            return str(i)
        if i == 2:
            return str(i)
        if i == 4:
            return str(i)
        if i == 8:
            return str(i)
        if i == 16:
            return str(i)
        if i == 32:
            return str(i)
        if i == 64:
            return str(i)


def test_入力例1():
    assert answer(7) == "4"


def test_入力例2():
    assert answer(32) == "32"


def test_入力例3():
    assert answer(1) == "1"


def test_入力例4():
    assert answer(100) == "64"

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
