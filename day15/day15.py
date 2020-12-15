def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    x = [int(i) for i in input.split(',')]
    used = {x[i]: i for i in range(len(x) - 1)}
    last = x[len(x) - 1]
    for i in range(len(x), 30000000):
        new = 0 if last not in used else i - used[last] - 1
        used[last] = i - 1
        last = new
    print(last)


solve()
