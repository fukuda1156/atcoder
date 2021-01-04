def answer(A: str, B: str) -> int:
    A = int(A[0]) + int(A[1]) + int(A[2])
    B = int(B[0]) + int(B[1]) + int(B[2])
    return max(A, B)

def test_入力例1():
    assert answer("123", "234") == 9


def test_入力例2():
    assert answer("593", "953") == 17


def test_入力例3():
    assert answer("100", "999") == 27

# def test_入力例4():
#     assert answer(25, 12) == 11
