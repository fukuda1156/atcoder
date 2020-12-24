# https://atcoder.jp/contests/abc173/submissions/18959875

N = int(input())
S = [(input()) for _ in range(N)]

print(f"AC x {S.count('AC')}")
print(f"WA x {S.count('WA')}")
print(f"TLE x {S.count('TLE')}")
print(f"RE x {S.count('RE')}")
