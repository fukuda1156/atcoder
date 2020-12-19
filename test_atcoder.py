def answer(W: str) -> str:
    return f"{W}s"


def test_入力例1():
    assert answer("dog") == "dogs"


def test_入力例2():
    assert answer("chokudai") == "chokudais"

# def test_入力例3():
#     assert answer(32, 21) == 58

# def test_入力例4():
#     assert answer(50) == 625
