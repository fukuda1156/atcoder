# https://atcoder.jp/contests/abc111/submissions/18967495

N = int(input())

i = int(N / 111)

if N % 111 != 0:
    i += 1
print(i * 111)
