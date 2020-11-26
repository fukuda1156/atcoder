# https://atcoder.jp/contests/abc163/tasks/abc163_a

import math


def answer(R: int) -> float:
    return 2 * math.pi * R


def test_入力例1():
    assert answer(1) == 6.28318530717958623200


def test_入力例2():
    assert answer(73) == 458.67252742410977361942

# def test_入力例3():
#     assert answer(-1) == "0"
