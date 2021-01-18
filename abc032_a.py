# https://atcoder.jp/contests/abc032/submissions/19501907

a = int(input())
b = int(input())
n = int(input())

for i in range(n, n + a * b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break
