# https://atcoder.jp/contests/abc155/submissions/17673684

N = int(input())
list_A = list(map(int, input().split()))

for i in list_A:
    if i % 2 == 0 and \
            i % 3 != 0 and \
            i % 5 != 0:
        print('DENIED')
        exit()
else:
    print("APPROVED")