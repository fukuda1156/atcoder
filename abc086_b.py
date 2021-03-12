# https://atcoder.jp/contests/abc086/submissions/20844227

A, B = input().split()

AB = int(A + B)

if AB ** 0.5 == int(AB ** 0.5):
    print("Yes")
else:
    print("No")
