# https://atcoder.jp/contests/abc179/submissions/17858154

S = list(input())

if S[-1] == "s":
    print("".join(S) + "es")

else:
    print("".join(S) + "s")
