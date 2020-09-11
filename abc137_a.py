# https://atcoder.jp/contests/abc137/submissions/16636243

a, b = map(int, input().split())
print(max(a + b, a - b, a * b))