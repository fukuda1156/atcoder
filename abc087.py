# https://atcoder.jp/contests/abc087/submissions/16221586

# x, a, b = map(int, input().split())

x = int(input())
a = int(input())
b = int(input())

xa = x - a
xab = xa // b
answer = xa - (b * xab)

print(answer)