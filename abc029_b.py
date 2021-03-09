# https://atcoder.jp/contests/abc029/submissions/20788868

S = [input() for _ in range(12)]

R = 0

for i in S:
    if i.count('r'):
        R += 1

print(R)
