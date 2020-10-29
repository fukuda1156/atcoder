# https://atcoder.jp/contests/abc142/submissions/17722326

N, K = map(int, input().split())
H = map(int, input().split())

list = []

for i in H:
    if i >= K:
        list.append(i)

print(len(list))
