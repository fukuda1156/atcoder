# https://atcoder.jp/contests/abc047/submissions/16636980

a, b, c = map(int, input().split())

if a == b + c or b == a + c or c == a + b:
    print("Yes")
else:
    print("No")
