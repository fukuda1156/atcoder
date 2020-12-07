# https://atcoder.jp/contests/abc083/tasks/abc083_b

# 1以上N以下の整数のうち、
# 10進法での各桁の和がA以上B以下であるものの
# 総和を出力せよ。

def answer(N: int, A: int, B: int) -> str:
    answer = 0
    for i in range(1, N + 1):
        X = i
        C = 0
        for j in range(5):
            C += X % 10
            X = X // 10
        if A <= C <= B:
            answer += i
    return str(answer)


def test_入力例1():
    assert answer(20, 2, 5) == "84"


def test_入力例2():
    assert answer(10, 1, 2) == "13"


def test_入力例3():
    assert answer(100, 4, 16) == "4554"

# def test_入力例4():
#     assert answer() == ""

# def test_入力例5():
#     assert answer() == ""
