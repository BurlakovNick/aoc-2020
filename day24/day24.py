import re


class Point(tuple):
    def __add__(self, other):
        return Point(x + y for x, y in zip(self, other))


moves = {'e': (0, 1), 'se': (1, 1), 'sw': (1, 0), 'w': (0, -1), 'nw': (-1, -1), 'ne': (-1, 0)}


def go(line):
    point = Point((0, 0))
    for token in re.findall('|'.join(moves.keys()), line):
        point = point + moves[token]
    return point


def get_neighbors(point):
    return (point + move for move in moves.values())


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

    points = [go(line) for line in input.split('\n')]

    black = set()
    for point in points:
        if point in black:
            black.remove(point)
        else:
            black.add(point)
    print(len(black))

    for _ in range(100):
        black = iterate(black)
    print(len(black))


solve()
