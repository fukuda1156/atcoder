# https://atcoder.jp/contests/abc154/submissions/18773089

S, T = input().split()
A, B = map(int, input().split())
U = input()

if U == S:
    A -= 1
    print(f"{A} {B}")

if U == T:
    B -= 1
    print(f"{A} {B}")
