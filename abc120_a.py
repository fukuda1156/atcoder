# https://atcoder.jp/contests/abc120/submissions/17643456

A, B, C = map(int, input().split())

BA = int(B / A)

if BA >= C:
    print(C)
else:
    print(BA)
