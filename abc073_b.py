# https://atcoder.jp/contests/abc073/submissions/20640269

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

answer = 0

for i in l:
    answer += 1 + max(i) - min(i)

print(answer)
