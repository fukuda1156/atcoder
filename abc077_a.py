# https://atcoder.jp/contests/abc077/submissions/17664950

C1 = list(input())
C2 = list(input())

C1[0], C1[2] = C1[2], C1[0]

if C1 == C2:
    print("YES")
else:
    print("NO")
