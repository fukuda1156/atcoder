# https://atcoder.jp/contests/abc063/submissions/17658455

input_list = list(input())
word_list = len([x for x in set(input_list) if input_list.count(x) > 1])

if word_list == 0:
    print("yes")
else:
    print("no")
