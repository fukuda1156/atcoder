# https://atcoder.jp/contests/abc164/submissions/17920271

S, W = map(int, input().split())

if S == W or S <= W:
    print("unsafe")
elif S >= W:
    print("safe")
