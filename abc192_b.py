# https://atcoder.jp/contests/abc192/submissions/20471652

S = input()

for i in range(len(S)):
    if i % 2 == 1:
        if S[i].islower():
            print('No')
            exit()
    if i % 2 == 0:
        if S[i].isupper():
            print('No')
            exit()
print('Yes')
