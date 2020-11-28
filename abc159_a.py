# https://atcoder.jp/contests/abc159/submissions/18441500

N, M = map(int, input().split())

print(int(N * (N - 1) / 2 + M * (M - 1) / 2))
