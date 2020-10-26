# https://atcoder.jp/contests/abc079/submissions/17664900

S = list(input())

if S[0] == S[1] == S[2] == S[3] \
        or \
        S[0] == S[1] == S[2] \
        or \
        S[1] == S[2] == S[3] \
        or \
        S[1] == S[2] == S[3] \
        :
    print("Yes")
else:
    print("No")
