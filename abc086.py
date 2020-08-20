a, b = map(int, input().split())

answer = a * b

if answer >= answer % 2 == 0:
    print('Even')
else:
    print('Odd')