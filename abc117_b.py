# https://atcoder.jp/contests/abc117/submissions/18406331

N = int(input())
L = list(map(int, input().split()))

if max(L) < sum(L) - max(L):
    print("Yes")
else:
    print("No")
