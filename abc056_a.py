# https://atcoder.jp/contests/abc056/submissions/17487648

a, b = map(str, input().split())

if a == "H" and b == "H":
    print("H")
if a == "H" and b == "D":
    print("D")
if a == "D" and b == "H":
    print("D")
if a == "D" and b == "D":
    print("H")
