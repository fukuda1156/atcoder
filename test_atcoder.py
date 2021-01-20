def answer(N: int) -> str:
    result = sum(list(map(int, str(N))))

    if N % result == 0:
        return ("Yes")
    else:
        return ("No")

def test_入力例1():
    assert answer(12) == "Yes"


def test_入力例2():
    assert answer(57) == "No"


def test_入力例3():
    assert answer(148) == "No"

# def test_入力例4():
#     assert answer(25, 12) == 11
