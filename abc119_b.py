# https://atcoder.jp/contests/abc119/submissions/20843777

N = int(input())
list = []

for i in range(N):
    A, B = input().split()
    list.append([float(A), B])

answer = []

for i in list:
    if i[1] == "JPY":
        answer.append(i[0])

    elif i[1] == "BTC":
        answer.append(380000 * i[0])

print(sum(answer))
