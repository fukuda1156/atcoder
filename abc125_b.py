# https://atcoder.jp/contests/abc125/submissions/20601839

N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

answer = 0

for V, C in zip(V, C):
    if V >= C:
        answer += V - C

print(answer)
