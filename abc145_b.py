# https://atcoder.jp/contests/abc145/submissions/18956227

N = int(input())
S = input()

if S[:len(S) // 2] == S[len(S) // 2:]:
    print("Yes")
else:
    print("No")
