# https://atcoder.jp/contests/abc016/submissions/20783298

A, B, C = map(int, input().split())

AB_Plus = A + B
AB_Minus = A - B

if AB_Plus == C and AB_Minus == C:
    print("?")

elif AB_Plus == C:
    print("+")

elif AB_Minus == C:
    print("-")

else:
    print("!")
