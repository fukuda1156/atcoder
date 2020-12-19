# https://atcoder.jp/contests/abc139/submissions/18850127

S = list(input())
T = list(input())

answer = 0

for i in range(len(S)):
    if S[i] == T[i]:
        answer += 1

print(answer)
