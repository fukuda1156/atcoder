# https://atcoder.jp/contests/abc103/submissions/20788271

S = input()
T = input()

S += S

if T in S:
    print("Yes")
else:
    print("No")
