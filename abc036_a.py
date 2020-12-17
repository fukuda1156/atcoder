# https://atcoder.jp/contests/abc036/submissions/18830937

A, B = map(int, input().split())

if B % A == 0:
    print(int(B / A))
else:
    print(int(B // A + 1))
