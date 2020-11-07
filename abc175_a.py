# https://atcoder.jp/contests/abc175/submissions/17916205

S = input()

if S == "SSS":
    print("0")

if S.count("RRR"):
    print("3")

elif S.count("RR"):
    print("2")

elif S.count("R"):
    print("1")
