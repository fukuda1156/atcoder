# https://atcoder.jp/contests/abc103/tasks/abc103_a

def answer(N: int, R: int) -> str:
    if N < 10:
        return str(100 * (10 - N) + R)
    else:
        return str(R)


def test_入力例1():
    assert answer(2, 2919) == "3719"


def test_入力例2():
    assert answer(22, 3051) == "3051"

# def test_入力例3():
#     assert answer(1, 1) == "0"
#
#
# def test_入力例4():
#     assert answer(13, 3) == "81"
#
#
# def test_入力例5():
#     assert answer(0, 3) == "3"
