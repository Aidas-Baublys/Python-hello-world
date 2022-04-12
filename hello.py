list_2d = [[1, 2, 3], [1, 2, 3, 4], [1, 2]]
list_flat = [2, 1, 1, 1]

print(list_flat.index(1))

for k in list_2d:
    for j, val in enumerate(k):
        k[j] *= 100

for k in list_2d:
    for j in k:
        print(j)
