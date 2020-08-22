# https://atcoder.jp/contests/abc061/submissions/16095042

a, b, c = map(int, input().split())

if a <= c and c <= b:
    print('Yes')
else:
    print('No')