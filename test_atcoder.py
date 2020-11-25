def answer(N: int, L: list) -> str:
    if max(L) < sum(L) - max(L):
        return ("Yes")
    else:
        return ("No")


def test_入力例1():
    assert answer(4, [3, 8, 5, 1]) == "Yes"


def test_入力例2():
    assert answer(4, [3, 8, 4, 1]) == "No"


def test_入力例3():
    assert answer(10, [1, 8, 10, 5, 8, 12, 34, 100, 11, 3]) == "No"
