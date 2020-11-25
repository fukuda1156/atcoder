# https://atcoder.jp/contests/abc076/submissions/18404877

N = int(input())
K = int(input())

number = 1

for i in range(N):
    if number + K < 2 * number:
        number += K
    else:
        number *= 2
print(number)
