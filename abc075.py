# https://atcoder.jp/contests/abc075/submissions/16162705

a, b, c =map(int,input().split())

if int(a) == int(b):
  print(c)
elif int(a) == int(c):
  print(b)
elif int(b) == int(c):
  print(a)