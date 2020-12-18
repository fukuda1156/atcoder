def answer(M: int, D: int) -> str:
    if M % D == 0:
        return "YES"
    else:
        return "NO"

def test_入力例1():
    assert answer(1, 1) == "YES"


def test_入力例2():
    assert answer(2, 29) == "NO"


def test_入力例3():
    assert answer(12, 6) == "YES"

# def test_入力例4():
#     assert answer(50) == 625
