# https://atcoder.jp/contests/abc156/submissions/18408993

N, K = map(int, input().split())

i = 1
while N >= K ** i:
    i += 1
print(i)
