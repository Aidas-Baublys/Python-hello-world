list_2d = [[1, 2, 3], [13, 7, 8, 2], [1, 2, 3, 4], [1, 2]]
list_flat = []

for k in list_2d:
    list_flat += [x for x in k if x % 2 == 0]

print(list_flat)
