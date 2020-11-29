# https://atcoder.jp/contests/abc088/tasks/abc088_b

def answer(N: int, A: list) -> str:
    A.sort(reverse=True)
    Alice = sum(A[0::2])
    Bob = sum(A[1::2])

    return str(abs(Alice - Bob))


def test_入力例1():
    assert answer(2, [3, 1]) == "2"


def test_入力例2():
    assert answer(3, [2, 7, 4]) == "5"


def test_入力例3():
    assert answer(4, [20, 18, 2, 18]) == "18"

# def test_入力例4():
#     assert answer() == ""

# def test_入力例5():
#     assert answer() == ""
