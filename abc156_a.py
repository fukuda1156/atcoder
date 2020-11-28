# https://atcoder.jp/contests/abc156/submissions/18441635

N, R = map(int, input().split())

if N < 10:
    print(100 * (10 - N) + R)
else:
    print(R)
