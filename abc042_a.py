# https://atcoder.jp/contests/abc042/submissions/17916803

l = list(map(int, input().split()))

if l.count(7) == 1 and l.count(5) == 2:
    print("YES")
else:
    print("NO")
