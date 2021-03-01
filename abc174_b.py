# https://atcoder.jp/contests/abc174/submissions/20585803

N, D = map(int, input().split())
l = [list(map(int, input().split())) for l in range(N)]

answer = 0

for i in l:
    if i[0] ** 2 + i[1] ** 2 <= D * D:
        answer += 1

print(answer)
