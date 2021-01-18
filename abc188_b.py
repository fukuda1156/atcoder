# https://atcoder.jp/contests/abc188/submissions/19509003

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

result = 0

for (A, B) in zip(A_list, B_list):
    result += A * B

if result == 0:
    print("Yes")
else:
    print("No")
