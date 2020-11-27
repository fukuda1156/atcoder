# https://atcoder.jp/contests/abc165/submissions/18427641

K = int(input())
A, B = map(int, input().split())

if B - A >= B % K:
    print("OK")
else:
    print("NG")

# for i in range(0, 1000, K):
#     if A <= i <= B:
#         print("OK")
#         exit()
# else:
#     print("NG")
