# https://atcoder.jp/contests/abc030/submissions/18900826

A, B, C, D = map(int, input().split())

TAKAHASHI = B / A
AOKI = D / C

if TAKAHASHI == AOKI:
    print("DRAW")

if TAKAHASHI > AOKI:
    print("TAKAHASHI")

if TAKAHASHI < AOKI:
    print("AOKI")
