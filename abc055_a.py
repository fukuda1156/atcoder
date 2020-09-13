# https://atcoder.jp/contests/abc055/submissions/16730672

n = int(input())

if n >= 15:
    print(n * 800 - (n // 15) * 200)
else:
    print(n * 800)
