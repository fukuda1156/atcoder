# https://atcoder.jp/contests/abc129/submissions/17487197

N = int(input())
w_list = list(map(int, input().split()))

answer = sum(w_list)

for i in range(len(w_list)):
    tmp = abs(sum(w_list[0:i]) - sum(w_list[i:]))
    if answer > tmp: answer = tmp

print(answer)