# https://atcoder.jp/contests/abc080/submissions/19540207

N = int(input())

result = sum(list(map(int, str(N))))

if N % result == 0:
    print("Yes")
else:
    print("No")
