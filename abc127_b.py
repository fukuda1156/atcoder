# https://atcoder.jp/contests/abc127/submissions/20601699

r, D, x = map(int, input().split())

for i in range(10):
    x = r * x - D
    print(x)
