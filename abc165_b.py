# https://atcoder.jp/contests/abc165/submissions/18688884

X = int(input())

deposit = 100
years = 0

while deposit < X:
    deposit += deposit // 100
    years += 1
print(years)
