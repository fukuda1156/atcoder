# https://atcoder.jp/contests/abc063/submissions/16094813

a, b = map(int, input().split())

answer = a + b

if answer >= 10:
    print('error')
else:
    print(answer)