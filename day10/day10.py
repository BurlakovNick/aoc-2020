import functools


def calc(x):
    distr = {1: 0, 2: 0, 3: 0}
    for i in range(1, len(x)):
        dx = x[i] - x[i - 1]
        distr[dx] = distr[dx] + 1
    return distr[1] * distr[3]


@functools.lru_cache(maxsize=1000)
def calc2(x, i):
    if i == 0:
        return 1
    return sum(calc2(x, i - j) for j in range(1, 4) if i - j >= 0 and x[i] - x[i - j] <= 3)


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    x = sorted(int(s) for s in input.split())
    x = (0, *x, x[len(x) - 1] + 3)
    print(calc(x))
    print(calc2(tuple(x), len(x) - 1))


solve()
