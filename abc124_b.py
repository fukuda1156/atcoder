# https://atcoder.jp/contests/abc124/submissions/17399720

n = int(input())
h = list(map(int, input().split()))
sea = 0
for i in range(n):
    if max(h[:i + 1]) == h[i]:
        sea += 1
print(sea)
