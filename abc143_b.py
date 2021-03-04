# https://atcoder.jp/contests/abc143/submissions/20640190

N = int(input())
D = list(map(int, input().split()))

answer = 0

for i in range(N):
    for j in range(i + 1, N):
        answer += D[i] * D[j]

print(answer)
