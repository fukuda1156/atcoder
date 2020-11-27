# https://atcoder.jp/contests/abc078/submissions/17917667

X, Y = input().split()

X16 = f"{X}".encode('utf-8', 'replace').hex()
Y16 = f"{Y}".encode('utf-8', 'replace').hex()

if X16 > Y16:
    print(">")
if X16 < Y16:
    print("<")
if X16 == Y16:
    print("=")
