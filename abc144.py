a, b = map(int, input().split())

if a >= 10 and b >= 10:
    print('-1')
else:
    answer = a * b
    print(answer)