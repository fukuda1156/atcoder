# https://atcoder.jp/contests/abc178/submissions/20564620

a, b, c, d = map(int, input().split())

print(max(a * c, a * d, b * c, b * d))
