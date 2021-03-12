# https://atcoder.jp/contests/abc159/submissions/20843485

S = input()

l = len(S)

if S == S[::-1] and S[:(l - 1) // 2] == S[(l - 1) // 2 - 1::-1]:
    print("Yes")
else:
    print("No")
