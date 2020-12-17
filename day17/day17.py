def init(field):
    return set((x, y, 0, 0) for x in range(len(field)) for y in range(len(field[x])) if field[x][y] == '#')


def get_neighbors(pos):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dz in (-1, 0, 1):
                for dw in (-1, 0, 1):
                    if not (dx == 0 and dy == 0 and dz == 0 and dw == 0):
                        yield pos[0] + dx, pos[1] + dy, pos[2] + dz, pos[3] + dw


def count_neighbors(pos, active):
    return sum(1 for neighbor in get_neighbors(pos) if neighbor in active)


def iterate(active):
    def is_active(x):
        active_neighbors = count_neighbors(x, active)
        return x in active and active_neighbors in (2, 3) or x not in active and active_neighbors == 3

    neighbors = set(y for x in active for y in get_neighbors(x))
    return set(x for x in neighbors if is_active(x))


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    active = init(input.split())
    for _ in range(6):
        active = iterate(active)
    print(len(active))


solve()
