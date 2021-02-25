# https://atcoder.jp/contests/abc191/submissions/20471692

N, X = map(int, input().split())
l = list(map(int, input().split()))

mylist = []

for i in l:
    if i != X:
        mylist.append(i)

print(' '.join([str(x) for x in mylist]))
