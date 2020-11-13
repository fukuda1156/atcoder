# https://atcoder.jp/contests/abc062/submissions/18081903

l0 = list(map(int, input().split()))

l1 = [1, 3, 5, 7, 8, 10, 12]
l2 = [4, 6, 9, 11]
l3 = [2]

if set(l0) <= set(l1) or \
        set(l0) <= set(l2) or \
        set(l0) <= set(l3):
    print("Yes")
else:
    print("No")
