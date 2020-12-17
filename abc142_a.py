# https://atcoder.jp/contests/abc142/submissions/18834068

N = int(input())

odd = 0
for i in range(1, N + 1, 1):
    if i % 2 != 0:
        odd += 1
print(odd / N)
