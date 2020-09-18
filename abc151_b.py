https: // atcoder.jp / contests / abc151 / submissions / 16821595

n, k, m = map(int, input().split())
a = map(int, input().split())

a = (n * m) - sum(a)

if a <= k:
    if a < 0:
        print("0")
    else:
        print(a)
else:
    print("-1")
