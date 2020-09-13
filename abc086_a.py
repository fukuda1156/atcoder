# https://atcoder.jp/contests/abc086/submissions/16730231

a, b = map(int, input().split())

if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')
