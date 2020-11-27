# https://atcoder.jp/contests/abc157/submissions/18428224

N = int(input())

surplus = N % 2
truncate = N // 2

print(surplus + truncate)
