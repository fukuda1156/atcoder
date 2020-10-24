ABC_list = list(map(int, input().split()))
K = int(input())

max_num = max(ABC_list) * (int(f"{K}") + 1)
other_num = sum(ABC_list) - max(ABC_list)

print(int(max_num + other_num))
