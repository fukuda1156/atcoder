# https://atcoder.jp/contests/abc112/submissions/20472012

N, T = map(int, input().split())
l = [list(map(int, input().split())) for l in range(N)]

cost = []

for i in l:
    if i[1] > T:
        continue
    cost.append(i[0])

if not cost:
    print("TLE")
else:
    print(min(cost))
