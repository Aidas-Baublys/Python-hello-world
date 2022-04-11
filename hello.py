dict1 = {
    1: [1, 2, 3, 4],
    2: [1, 2, 3],
    3: [1, 2],
    4: [1, 2, 3, 4, 5]
}

for key in dict1:
    if key % 2 == 0:
        print(f"key: {key}, val: {dict1[key]}", dict1[key][::2])
