# https://atcoder.jp/contests/abc012/submissions/20783808

N = int(input())

if N >= 86399:
    print("23:59:59")

else:
    hh = N // 3600
    zero_hh = str(hh).zfill(2)

    mm = N // 60 % 60
    zero_mm = str(mm).zfill(2)

    ss = N % 60
    zero_ss = str(ss).zfill(2)

    print(f"{zero_hh}:{zero_mm}:{zero_ss}")
