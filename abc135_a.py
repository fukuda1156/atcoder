# https://atcoder.jp/contests/abc135/submissions/18914282

A, B = map(int, input().split())

if A % 2 != B % 2:
    print("IMPOSSIBLE")
else:
    print(int((A + B) / 2))
