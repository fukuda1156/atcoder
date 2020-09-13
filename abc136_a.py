a, b, c = map(int, input().split())

ab = a - b
cab = c - ab

if cab >= 0:
    print(0)

if cab < 0:
    print(cab)
