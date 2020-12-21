# https://atcoder.jp/contests/abc119/submissions/18924959

S = input()

if int(S[:4]) <= 2019 and \
        int(S[5:7]) <= 4 and \
        int(S[8:10]) <= 30:
    print("Heisei")
else:
    print("TBD")
