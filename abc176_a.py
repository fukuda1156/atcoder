# https://atcoder.jp/contests/abc176/submissions/17916659

import math

N, X, T = map(int, input().split())

print(math.ceil(N / X) * T)
