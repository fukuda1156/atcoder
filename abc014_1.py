# https://atcoder.jp/contests/abc014/submissions/18945935

a = int(input())
b = int(input())

if a == b:
    print(0)
else:
    print(b - a % b)