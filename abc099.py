# https://atcoder.jp/contests/abc099/submissions/16071974

n = int(input())

if n >= 1000:
    print("ABD")
    # print("ABD" + str(n - 999).zfill(3))
if n <= 999:
    print("ABC")
    # print("ABC" + str(n))