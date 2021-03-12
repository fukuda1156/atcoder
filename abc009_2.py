# https://atcoder.jp/contests/abc009/submissions/20848995

N = int(input())
A = [int(input()) for _ in range(N)]

print(sorted(set(A))[-2])
