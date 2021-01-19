# https://atcoder.jp/contests/abc018/submissions/19516899

l = [int(input()) for i in range(3)]
s = sorted(l)[::-1]
for i in l:
    print(s.index(i) + 1)
