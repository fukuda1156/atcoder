# https://atcoder.jp/contests/abc167/submissions/20779167

A, B, C, K = map(int, input().split())

if K <= A:
    print(K)
elif A < K < A + B:
    print(A)
else:
    X = K - (A + B)
    print(A - X)
