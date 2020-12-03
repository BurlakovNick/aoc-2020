from functools import reduce


def count_trees(forest, dx, dy):
    n = len(forest)
    m = len(forest[0])
    return sum(1 for i in range(0, len(forest))
               if i * dx < n
               and forest[i * dx][i * dy % m] == '#')


def solve():
    with open('input.txt', 'r') as inputFile:
        str = inputFile.read()
    forest = str.split()
    steps = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    print(reduce(lambda acc, step: acc * count_trees(forest, step[0], step[1]), steps, 1))


solve()
