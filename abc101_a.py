# https://atcoder.jp/contests/abc101/submissions/18773298

S = input()

Plus_Minus = 0

Plus_Minus += S.count("+")
Plus_Minus -= S.count("-")

print(Plus_Minus)
