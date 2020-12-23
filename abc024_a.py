# https://atcoder.jp/contests/abc024/submissions/18952875

A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

answer = 0

answer += (A * S) + (B * T)

if S + T >= K:
    answer -= C * (S + T)

print(answer)
