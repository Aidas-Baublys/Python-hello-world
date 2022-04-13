def average(*args):
    print(sum(args) / len(args))


average(1, 2, 3, 4, 5, 6)


def average_2(*args):
    res = 0
    counter = 0
    for arg in args:
        res += arg
        counter += 1

    print(res / counter)


average_2(1, 2, 3, 4, 5, 6)
