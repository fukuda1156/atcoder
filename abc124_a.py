# https://atcoder.jp/contests/abc124/submissions/18842680
A, B = map(int, input().split())

if A == B:
    print(A + B)
if A != B:
    print(max(A, B) + (max(A, B) - 1))
