# https://atcoder.jp/contests/abc022/submissions/19572139

N, S, T = map(int, input().split())

answer = 0
W = 0

for i in range(N):
    W += int(input())
    if S <= W <= T:
        answer += 1
print(answer)
