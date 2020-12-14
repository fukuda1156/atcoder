# https://atcoder.jp/contests/abc143/submissions/18773179

A, B = map(int, input().split())

long = A - B * 2

if long >= 0:
    print(long)
else:
    print(0)
