# https://atcoder.jp/contests/abc041/submissions/20564790

A, B, C = map(int, input().split())

print(A * B % 1000000007 * C % 1000000007)
