# https://atcoder.jp/contests/abc132/submissions/20784110

N = int(input())
P = list(map(int, input().split()))

answer = 0

for i in range(N - 2):
    if P[i] < P[i + 1] < P[i + 2]:
        answer += 1
    if P[i] > P[i + 1] > P[i + 2]:
        answer += 1

print(answer)
