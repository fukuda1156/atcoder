# https://atcoder.jp/contests/abc058/submissions/17720875

O = input()
E = input()
OE = ""

for i in range(0, len(O)):
    str = (O + E)[i::len(O)]
    OE += str
print(OE)
