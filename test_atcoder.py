def answer(N: int) -> int:
    odd = 0
    for i in range(N, 0, -1):
        if len(str(i)) % 2 == 1:
            odd += 1
    return odd


def test_入力例1():
    assert answer(11) == 9


def test_入力例2():
    assert answer(136) == 46


def test_入力例3():
    assert answer(100000) == 90909

# def test_入力例4():
#     assert answer() == ""
