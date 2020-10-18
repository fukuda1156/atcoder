# https://atcoder.jp/contests/abc054/submissions/17491622

a, b = map(int, input().split())

if a == b:
    print("Draw")
elif a == 1:
    print("Alice")
elif b == 1:
    print("Bob")
elif a > b:
    print("Alice")
elif a < b:
    print("Bob")
