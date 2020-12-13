# https://atcoder.jp/contests/abc136/submissions/18772494

N = int(input())

odd = 0

for i in range(N, 0, -1):
    if len(str(i)) % 2 == 1:
        odd += 1
print(odd)
