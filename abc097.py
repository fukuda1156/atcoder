# https://atcoder.jp/contests/abc097/submissions/16080681

a, b, c, d = map(int, input().split())

if abs(a-b) <= d and abs(b-c) <= d or abs(a-c) <= d:
    print('Yes')
else:
    print('No')