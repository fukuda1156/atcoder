# https://atcoder.jp/contests/abc148/submissions/17721122

N = int(input())
O, E = input().split()
OE = ""

for i in range(0, N):
    str = (O + E)[i::N]
    OE += str
print(OE)
