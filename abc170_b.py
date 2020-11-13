# https://atcoder.jp/contests/abc170/submissions/18077710

X, Y = map(int, input().split())

answer = "No"

for i in range(X + 1):
    J = X - i
    if 2 * i + 4 * J == Y:
        answer = "Yes"
print(answer)
