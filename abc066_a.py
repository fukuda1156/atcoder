# https://atcoder.jp/contests/abc066/submissions/16635882

a, b, c = map(int, input().split())
print(min(a + b, a + c, c + b))
