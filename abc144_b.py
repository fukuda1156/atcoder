# https://atcoder.jp/contests/abc144/submissions/17640233

N = int(input())

for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        if i * j == N:
            print("Yes")
            exit()
print("No")
