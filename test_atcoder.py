def answer(X: int, Y: int) -> str:
    MINPOINT = min(X, Y) + 3
    MAXPOINT = max(X, Y)

    if MINPOINT > MAXPOINT:
        return "Yes"
    else:
        return "No"


def test_入力例1():
    assert answer(3, 5) == "Yes"


def test_入力例2():
    assert answer(6, 2) == "No"


def test_入力例3():
    assert answer(12, 15) == "No"

# def test_入力例4():
#     assert answer(25, 12) == 11
