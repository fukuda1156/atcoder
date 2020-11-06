# https://atcoder.jp/contests/abc127/submissions/17911093

A, B = map(int, input().split())

if A <= 5:
    print("0")

elif 6 <= A <= 12:
    print(int(B / 2))

elif 13 <= A:
    print(B)
