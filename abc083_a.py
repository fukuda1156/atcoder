# https://atcoder.jp/contests/abc083/submissions/17857749

l = list(map(int, input().split()))

if l[0] + l[1] == l[2] + l[3]:
    print("Balanced")

elif l[0] + l[1] >= l[2] + l[3]:
    print("Left")

elif l[0] + l[1] <= l[2] + l[3]:
    print("Right")
