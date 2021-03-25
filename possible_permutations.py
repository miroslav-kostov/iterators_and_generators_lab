from itertools import permutations

def possible_permutations(n):
    for el in permutations(n):
        yield list(el)

[print(n) for n in possible_permutations([1, 2, 3])]