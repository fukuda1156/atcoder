# https://atcoder.jp/contests/abc182/tasks/abc182_a

def answer(A: int, B: int) -> str:
    limit = 2 * A + 100
    rising = limit - B
    return str(rising)


def test_入力例1():
    assert answer(200, 300) == "200"


def test_入力例2():
    assert answer(10000, 0) == "20100"

# def test_入力例3():
#     assert answer(-1) == "0"
