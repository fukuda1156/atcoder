# https://atcoder.jp/contests/abc144/submissions/16074405

a, b = map(int, input().split())

if a >= 10 or b >= 10:
    print('-1')
else:
    answer = a * b
    print(answer)
