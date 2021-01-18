# https://atcoder.jp/contests/abc188/submissions/19501804

X, Y = map(int, input().split())

MINPOINT = min(X, Y) + 3
MAXPOINT = max(X, Y)

if MINPOINT > MAXPOINT:
    print("Yes")
else:
    print("No")
