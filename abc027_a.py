# https://atcoder.jp/contests/abc027/submissions/18916493

L1, L2, L3, = map(int, input().split())

if L1 == L2:
    print(L3)
elif L2 == L3:
    print(L1)
elif L3 == L1:
    print(L2)
