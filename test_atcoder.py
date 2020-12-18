def answer(A: int, B: int) -> str:
    return f"{B} {A}"


def test_入力例1():
    assert answer(1, 2) == "2 1"


def test_入力例2():
    assert answer(5, 5) == "5 5"

# def test_入力例3():
#     assert answer(12, 6) == "YES"

# def test_入力例4():
#     assert answer(50) == 625
