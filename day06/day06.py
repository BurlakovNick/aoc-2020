def get_universum(lines):
    result = set()
    for line in lines:
        result = result.union(set(line))
    return result


def get_intersection(lines):
    result = set(lines[0])
    for line in lines:
        result = result.intersection(line)
    return result


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    tests = [x.split() for x in input.split('\n\n')]
    print(sum(len(get_universum(test)) for test in tests))
    print(sum(len(get_intersection(test)) for test in tests))


solve()
