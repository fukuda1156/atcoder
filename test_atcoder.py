# https://atcoder.jp/contests/abc142/tasks/abc142_a
def answer(N: int) -> float:
    odd = 0
    for i in range(1, N + 1, 1):
        if i % 2 != 0:
            odd += 1
    return odd / N


def test_入力例1():
    assert answer(4) == 0.5000000000


def test_入力例2():
    assert answer(5) == 0.6000000000


def test_入力例3():
    assert answer(1) == 1.0000000000

# def test_入力例4():
#     assert answer(50) == 625
