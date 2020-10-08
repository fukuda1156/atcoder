# https://atcoder.jp/contests/abc044/submissions/17247908

n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n < k:
    print(n * x)
else:
    print(k * x + (n - k) * y)
