# https://atcoder.jp/contests/abc083/submissions/18622225

N, A, B = map(int, input().split())

answer = 0
for i in range(1, N + 1):
    X = i
    C = 0
    for j in range(5):
        C += X % 10
        X = X // 10
    if A <= C <= B:
        answer += i
print(answer)
