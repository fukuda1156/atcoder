# https://atcoder.jp/contests/abc058/submissions/16788991

a, b, c = map(int, input().split())

if b - a == c - b:
    print("YES")
else:
    print("NO")
