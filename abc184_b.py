# https://atcoder.jp/contests/abc184/submissions/18487835

N, X = map(int, input().split())
S = input()
for s in S:
    if s == 'o':
        X += 1
    elif X:
        X -= 1
print(X)
