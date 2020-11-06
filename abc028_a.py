# https://atcoder.jp/contests/abc028/submissions/17910875

N = int(input())

if N == 100:
    print("Perfect")

elif N <= 59:
    print("Bad")

elif 89 >= N >= 60:
    print("Good")

elif 99 >= N >= 90:
    print("Great")
