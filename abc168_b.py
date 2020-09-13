# https://atcoder.jp/contests/abc168/submissions/16666272

k = int(input())
s = str(input())

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")
