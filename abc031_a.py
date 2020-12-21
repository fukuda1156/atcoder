# https://atcoder.jp/contests/abc031/submissions/18926736

A, D = map(int, input().split())

Offensive = (A + 1) * D
Defense = A * (D + 1)

if Offensive == Defense:
    print(Offensive)
elif Offensive >= Defense:
    print(Offensive)
elif Offensive <= Defense:
    print(Defense)
