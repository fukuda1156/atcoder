# https://atcoder.jp/contests/abc109/submissions/18772720

A, B = map(int, input().split())

for i in range(3, 1, -1):
    num = A * B * i
    if num % 2 != 0:
        print("Yes")
        break
    else:
        print("No")
        break
