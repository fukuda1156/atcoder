# https://atcoder.jp/contests/abc190/submissions/20471838

N, S, D = map(int, input().split())
incantation = [list(map(int, input().split())) for l in range(N)]

for i in incantation:
    if i[0] < S and i[1] > D:
        print("Yes")
        exit()
print("No")
