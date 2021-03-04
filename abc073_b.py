# https://atcoder.jp/contests/abc073/submissions/20640254

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

answer = 0

for i in l:
    answer += 1 + i[1] - i[0]

print(answer)
