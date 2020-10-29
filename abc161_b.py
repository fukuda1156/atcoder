# https://atcoder.jp/contests/abc161/submissions/17708112

N, M = map(int, input().split())
i = list(map(int, input().split()))

i = sorted(i, reverse=True)

if i[M - 1] < sum(i) / (4 * M):
    print("No")
else:
    print("Yes")
