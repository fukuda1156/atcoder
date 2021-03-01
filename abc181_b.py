# https://atcoder.jp/contests/abc181/submissions/20599971

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

answer = 0

for i in range(N):
    A, B = l[i]
    answer += (B - A + 1) * (A + B) // 2

print(answer)
