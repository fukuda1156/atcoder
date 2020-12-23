# https://atcoder.jp/contests/abc120/submissions/18956488

A, B, K = map(int, input().split())

answer_list = []

for i in range(1, 100 + 1):
    if A % i == 0 and B % i == 0:
        answer_list.append(i)
else:
    print(answer_list[- K])
