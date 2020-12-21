# https://atcoder.jp/contests/abc111/submissions/18925276

n = input()

print(n.translate(str.maketrans({"1": "9", "9": "1"})))
