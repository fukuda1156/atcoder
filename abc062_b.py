# https://atcoder.jp/contests/abc062/tasks/abc062_b

H, W = map(int, input().split())
a = [input() for i in range(H)]

print("#" * (W + 2))
for i in a:
    print(f"#{i}#")
else:
    print("#" * (W + 2))
