# https://atcoder.jp/contests/abc106/submissions/18842590

A, B = map(int, input().split())

road_area = A + B - 1
all_area = A * B
print(all_area - road_area)
