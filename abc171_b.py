# https://atcoder.jp/contests/abc171/submissions/18959960

N, K = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
print(sum(P[0:K]))
