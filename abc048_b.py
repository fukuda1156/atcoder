# https://atcoder.jp/contests/abc048/tasks/abc048_b

a, b, x = map(int, input().split())

print(b // x - ~ -a // x)
