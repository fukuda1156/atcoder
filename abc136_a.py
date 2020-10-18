# https://atcoder.jp/contests/abc136/submissions/17491794

a, b, c = map(int, input().split())

ab = a - b
answer = c - ab

if answer <= 0:
    print("0")
else:
    print(answer)
