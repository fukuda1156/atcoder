# https://atcoder.jp/contests/abc075/submissions/16730310

a, b, c = map(int, input().split())

if int(a) == int(b):
    print(c)
if int(a) == int(c):
    print(b)
if int(b) == int(c):
    print(a)
