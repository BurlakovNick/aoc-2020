moves = {'e': (0, 1), 'se': (1, 1), 'sw': (1, 0), 'w': (0, -1), 'nw': (-1, -1), 'ne': (-1, 0)}


def move(line):
    pos = 0
    x, y = 0, 0
    while pos < len(line):
        for ch, (dx, dy) in moves.items():
            if line[pos:pos+len(ch)] == ch:
                x, y = x + dx, y + dy
                pos += len(ch)
                break
    return x, y


def get_neighbors(point):
    x, y = point
    return ((x + dx, y + dy) for (dx, dy) in moves.values())


def count_neighbors(point, active):
    return sum(1 for neighbor in get_neighbors(point) if neighbor in active)


def iterate(active):
    def is_active(point):
        active_neighbors = count_neighbors(point, active)
        return point in active and active_neighbors in (1, 2) or point not in active and active_neighbors == 2

    neighbors = set(y for x in active for y in get_neighbors(x))
    return set(x for x in neighbors if is_active(x))


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    black = set()
    for line in input.split('\n'):
        x, y = move(line)
        if (x, y) in black:
            black.remove((x, y))
        else:
            black.add((x, y))
    print(len(black))

    for _ in range(100):
        black = iterate(black)
    print(len(black))


solve()
