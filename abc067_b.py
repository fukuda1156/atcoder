# https://atcoder.jp/contests/abc067/submissions/17609040

N, K = map(int, input().split())
L_list = list(map(int, input().split()))

L_list.sort(reverse=True)
K_list = L_list[:int(f"{K}")]
print(sum(K_list))
