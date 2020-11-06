# https://atcoder.jp/contests/abc098/submissions/17911449

A, B = map(int, input().split())

AB_Calculation = []

AB_Calculation.append(A + B)
AB_Calculation.append(A - B)
AB_Calculation.append(A * B)

print(max(AB_Calculation))
