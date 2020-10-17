# https://atcoder.jp/contests/abc057/submissions/17487533

a, b = map(int, input().split())

if a + b >= 24:
    print(a + b - 24)

else:
    print(a + b)
