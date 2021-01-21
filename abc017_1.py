# https://atcoder.jp/contests/abc017/submissions/19544357

l = [list(map(int, input().split())) for l in range(3)]

Task = 0

for (i, i2) in l:
    Task += i * i2 * 0.1

print(int(Task))
