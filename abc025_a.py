# https://atcoder.jp/contests/abc025/submissions/19561193

S = input()
N = int(input())

N -= 1

A = N // 5
B = N % 5

print(f"{S[A]}{S[B]}")
