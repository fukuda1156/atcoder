# https://atcoder.jp/contests/abc115/submissions/17721764

N = int(input())
P = [int(input()) for _ in range(N)]

PD = sorted(P, reverse=True)

print(int(PD[0] / 2) + sum(PD) - PD[0])
