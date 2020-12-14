# https://atcoder.jp/contests/abc102/submissions/18773540

N = int(input())

for i in range(N, 10000000000, N):
    if i % 2 == 0:
        print(i)
        break
