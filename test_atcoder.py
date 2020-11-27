# https://atcoder.jp/contests/abc165/tasks/abc165_a

# def answer(K: int, A: int, B: int) -> str:
#     for i in range(0, 1000, K):
#         if A <= i <= B:
#             return ("OK")
#             exit()
#     else:
#         return ("NG")

def answer(K: int, A: int, B: int) -> str:
    if B - A >= B % K:
        return ("OK")
    else:
        return ("NG")


def test_入力例1():
    assert answer(7, 500, 600) == "OK"


def test_入力例2():
    assert answer(4, 5, 7) == "NG"


def test_入力例3():
    assert answer(1, 11, 11) == "OK"
