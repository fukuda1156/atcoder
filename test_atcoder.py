def answer(A: int, B: int) -> int:
    road_area = A + B - 1
    all_area = A * B
    return all_area - road_area


def test_入力例1():
    assert answer(2, 2) == 1


# A * B == 4
# A + B == 2

def test_入力例2():
    assert answer(5, 7) == 24

# def test_入力例3():
#     assert answer(12, 6) == "YES"

# def test_入力例4():
#     assert answer(50) == 625
