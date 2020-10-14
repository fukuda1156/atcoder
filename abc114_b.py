# https://atcoder.jp/contests/abc114/submissions/17397941

s = input()
answer = 999
for i in range(len(s) - 2):
    answer = min(answer, abs(753 - int(s[i: i + 3])))
print(answer)
