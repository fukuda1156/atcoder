def answer(A: int, B: int) -> int:
    if A == B:
        return A + B
    if A != B:
        return max(A, B) + (max(A, B) - 1)


def test_入力例1():
    assert answer(5, 3) == 9


def test_入力例2():
    assert answer(6, 6) == 12

# def test_入力例3():
#     assert answer(12, 6) == "YES"

# def test_入力例4():
#     assert answer(50) == 625
