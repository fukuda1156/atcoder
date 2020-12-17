def answer(W: int, H: int) -> str:
    if W / 4 == H / 3:
        return "4:3"
    else:
        return "16:9"

def test_入力例1():
    assert answer(4, 3) == "4:3"


def test_入力例2():
    assert answer(16, 9) == "16:9"


def test_入力例3():
    assert answer(28, 21) == "4:3"

# def test_入力例4():
#     assert answer(50) == 625
