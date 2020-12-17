# https://atcoder.jp/contests/abc037/submissions/18816552

A, B, C = map(int, input().split())

answer = C // min(A, B)
print(answer)
