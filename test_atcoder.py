def answer(A: int, B: int) -> str:
    if B % A == 0:
        return str(int(B / A))
    else:
        return str(B // A + 1)


def test_入力例1():
    assert answer(12, 36) == "3"


def test_入力例2():
    assert answer(12, 100) == "9"

# def test_入力例3():
#     assert answer(28, 21) == "4:3"

# def test_入力例4():
#     assert answer(50) == 625
