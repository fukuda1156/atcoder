# https://atcoder.jp/contests/abc147/submissions/8846579

S = input()

answer = 0

for i in range(len(S) // 2):
    A = S[i]
    B = S[-1 - i]

    if A != B:
        answer += 1

print(answer)
