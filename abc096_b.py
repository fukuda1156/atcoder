# https://atcoder.jp/contests/abc096/submissions/18488506

ABC = list(map(int, input().split()))
K = int(input())

if K == 1:
    print(int(max(ABC) * 2 + (sum(ABC) - max(ABC))))
else:
    print(int(max(ABC) ** K + (sum(ABC) - max(ABC))))
