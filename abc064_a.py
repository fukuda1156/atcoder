# https://atcoder.jp/contests/abc064/submissions/16725033

r, g, b = map(str, input().split())

rgb = str(r) + str(g) + str(b)

if int(rgb) % 4 == 0:
  print("YES")
else:
  print("NO")