# https://atcoder.jp/contests/abc101/submissions/18895091

N = input()
S = list(map(int, N))

if int(N) % sum(S) == 0:
    print("Yes")
else:
    print("No")
