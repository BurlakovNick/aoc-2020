def calc(x):
    distr = {1: 0, 2: 0, 3: 0}
    for i in range(1, len(x)):
        dx = x[i] - x[i - 1]
        distr[dx] = distr[dx] + 1
    return distr[1] * distr[3]


def calc2(x, i, mem):
    if i == 0:
        return 1
    if i in mem:
        return mem[i]
    mem[i] = sum(calc2(x, i - j, mem) for j in range(1, 4) if i - j >= 0 and x[i] - x[i - j] <= 3)
    return mem[i]


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    x = [int(s) for s in input.split()]
    x.append(0)
    x.append(max(x) + 3)
    x.sort()
    print(calc(x))
    print(calc2(x, len(x) - 1, {}))


solve()
