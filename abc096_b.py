# https://atcoder.jp/contests/abc096/submissions/18488506

ABC = list(map(int, input().split()))
K = int(input())

print(sum(ABC) + (max(ABC) * (2 ** K - 1)))
