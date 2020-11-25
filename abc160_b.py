# https://atcoder.jp/contests/abc160/submissions/18405637

X = int(input())

X500 = X // 500
X5 = X % 500 // 5

print(1000 * X500 + 5 * X5)
