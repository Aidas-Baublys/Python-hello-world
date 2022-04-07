import copy


simple = [1, [2], 3]
simple_2 = copy.deepcopy(simple)

simple_2[1][0] = 22

print(simple, simple_2)
