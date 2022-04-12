dict1 = {
    1: [1, 2, 3, 4],
    2: [1, 2, 3],
    3: [1, 2],
    4: [1, 2, 3, 4, 5]
}

for key, value in dict1.items():
    if key % 2 == 0:
        print(f"key: {key}, val: {value}", value[::2])
