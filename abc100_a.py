# https://atcoder.jp/contests/abc100/submissions/18916426

A, B = map(int, input().split())

cake = 16 / 2

if cake >= A and cake >= B:
    print("Yay!")
else:
    print(":(")
