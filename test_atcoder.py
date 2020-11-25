def answer(N: int, K: int) -> str:
    number = 1

    for i in range(N):
        if number + K < 2 * number:
            number += K
        else:
            number *= 2
    return str(number)


def test_入力例1():
    assert answer(4, 3) == "10"


def test_入力例2():
    assert answer(10, 10) == "76"
