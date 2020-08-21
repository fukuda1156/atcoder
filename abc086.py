# https://atcoder.jp/contests/abc086/tasks/abc086_a

a, b = map(int, input().split())

answer = a * b

if answer >= answer % 2 == 0:
    print('Even')
else:
    print('Odd')