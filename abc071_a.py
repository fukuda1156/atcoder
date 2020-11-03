# https://atcoder.jp/contests/abc071/tasks/abc071_a

x, a, b = map(int, input().split())

ax = abs(a - x)
bx = abs(b - x)

if ax >= bx:
    print("B")
if bx >= ax:
    print("A")
