# H, W = int(2), int(1)
#
# if W == 1:
#     W += 1
#
# # abc
# # arc
#
# print("#" + f"{H}" + "#")
#
# print(f'{"#" * (W + 1)}\n{"#" * (W + 1)}')

H, W = map(int, input().split())
l = [list(input()) for l in range(H)]
print(l)
