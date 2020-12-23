# https://atcoder.jp/contests/abc110/submissions/18925545

ABC = list(map(int, input().split()))
ABC.sort(reverse=True)
Maximize = f"{ABC[0]}{ABC[1]}"
print(int(Maximize) + int(ABC[2]))
