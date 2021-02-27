# https://atcoder.jp/contests/abc172/submissions/20505750

S = input()
T = input()

word_count = 0

for i, j in zip(S, T):
    if i != j:
        word_count += 1

print(word_count)
