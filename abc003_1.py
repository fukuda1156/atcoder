# https://atcoder.jp/contests/abc003/tasks/abc003_1

N = int(input())

M = 0

for i in range(1, N + 1):
    M += 10000 * i

print(int(M * 1 / N))
