import numpy as np

a = np.random.randint(0, 11, (6, 6))

print(a)
print(a[2:4, 0:2])
print(a[[0, 1, 2, 3], [2, 3, 4, 5]])
print(a[[0, -2, -1], 4:])
