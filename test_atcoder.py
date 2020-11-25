def answer(X: int) -> str:
    X500 = X // 500
    X5 = X % 500 // 5
    return str(1000 * X500 + 5 * X5)


def test_入力例1():
    assert answer(1024) == "2020"


def test_入力例2():
    assert answer(0) == "0"


def test_入力例3():
    assert answer(1000000000) == "2000000000"
