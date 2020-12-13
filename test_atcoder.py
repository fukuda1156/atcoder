def answer(ABC: list, K: int) -> int:
    if K == 1:
        return int(max(ABC) * 2 + (sum(ABC) - max(ABC)))
    else:
        return int(max(ABC) ** K + (sum(ABC) - max(ABC)))


def test_入力例1():
    assert answer([5, 3, 11], 1) == 30


def test_入力例2():
    assert answer([3, 3, 4], 2) == 22

# def test_入力例3():
#     assert answer() == ""
#
#
# def test_入力例4():
#     assert answer() == ""
