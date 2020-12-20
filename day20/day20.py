def parse(tile):
    id, field = tile.split(':\n')
    id = int(id.split(' ')[1])
    field = [[char for char in line] for line in field.split('\n')]
    return (id, field)


# refactor
def rotate(field):
    rotated = [line.copy() for line in field]
    n = len(field)
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = field[i][j]
    return rotated


def flip_x(field):
    flipped = [line.copy() for line in field]
    n = len(field)
    for i in range(n):
        for j in range(n):
            flipped[n - i - 1][j] = field[i][j]
    return flipped


def flip_y(field):
    flipped = [line.copy() for line in field]
    n = len(field)
    for i in range(n):
        for j in range(n):
            flipped[i][n - 1 - j] = field[i][j]
    return flipped


def to_string(field):
    return '\n'.join(''.join(line) for line in field)


def mutate(field):
    current = field
    for _ in range(4):
        yield current
        yield flip_x(current)
        yield flip_y(current)
        yield flip_x(flip_y(current))
        current = rotate(current)


def is_neighbors(left, right):
    n = len(left)
    for x in mutate(left):
        for y in mutate(right):
            if x[n - 1] == y[0]:
                return True
    return False


def get_right_border(field):
    n = len(field)
    return [field[i][n - 1] for i in range(n)]


def get_left_border(field):
    n = len(field)
    return [field[i][0] for i in range(n)]


def can_connect_right(left, right):
    for mutated in mutate(right):
        if get_right_border(left) == get_left_border(mutated):
            return True
    return False


def can_connect_down(up, down):
    for mutated in mutate(down):
        if up[len(up) - 1] == mutated[0]:
            return True
    return False


def count_neighbors(tile, tiles):
    cnt = 0
    for other in tiles:
        if tile[0] != other[0] and is_neighbors(tile[1], other[1]):
            cnt += 1
    return cnt


def can_connect_to_corner(corner, tiles):
    right = any(True for tile in tiles if can_connect_right(corner, tile[1]))
    down = any(True for tile in tiles if can_connect_down(corner, tile[1]))
    return right and down


def get_field(connected):
    n = len(connected[0][0][1])
    size = len(connected)
    field = []
    for i in range(size):
        for x in range(1, n - 1):
            row = []
            for j in range(size):
                for y in range(1, n - 1):
                    row.append(connected[i][j][1][x][y])
            field.append(row)
    return field


def mark_monsters(field):
    pattern = ['..................#.',
               '#....##....##....###',
               '.#..#..#..#..#..#...']
    n = len(field)

    def is_match(sx, sy):
        if sx + len(pattern) > n or sy + len(pattern[0]) > n:
            return False
        for dx in range(len(pattern)):
            for dy in range(len(pattern[0])):
                if pattern[dx][dy] == '#' and field[sx + dx][sy + dy] != '#':
                    return False
        return True

    for x in range(n):
        for y in range(n):
            if is_match(x, y):
                for i in range(len(pattern)):
                    for j in range(len(pattern[0])):
                        if pattern[i][j] == '#':
                            field[x + i][y + j] = 'O'
    return field


def count(field, char):
    n = len(field)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if field[i][j] == char:
                cnt += 1
    return cnt


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    tiles = input.split('\n\n')
    tiles = [parse(tile) for tile in tiles]
    corner = next(tile for tile in tiles if count_neighbors(tile, tiles) == 2)
    other_tiles = [tile for tile in tiles if tile[0] != corner[0]]
    corner = corner[0], next(mutated for mutated in mutate(corner[1]) if can_connect_to_corner(mutated, other_tiles))

    size = next(i for i in range(2000) if i * i == len(tiles))
    connected = [[None for j in range(size)] for i in range(size)]
    connected[0][0] = corner

    n = len(corner[1])
    used = set()
    used.add(corner[0])
    for i in range(1, size):
        for tile in tiles:
            if tile[0] not in used:
                success = False
                for mutated in mutate(tile[1]):
                    if get_right_border(connected[0][i - 1][1]) == get_left_border(mutated) and \
                            any(True for tile in tiles if can_connect_down(mutated, tile[1])):
                        connected[0][i] = tile[0], mutated
                        print(tile[0])
                        used.add(tile[0])
                        break

                if success:
                    break

    for i in range(1, size):
        for tile in tiles:
            if tile[0] not in used:
                success = False
                for mutated in mutate(tile[1]):
                    if connected[i - 1][0][1][n - 1] == mutated[0] and \
                            any(True for tile in tiles if can_connect_right(mutated, tile[1])):
                        connected[i][0] = tile[0], mutated
                        print(tile[0])
                        used.add(tile[0])
                        break

                if success:
                    break

    for i in range(1, size):
        for j in range(1, size):
            for tile in tiles:
                if tile[0] not in used:
                    success = False
                    for mutated in mutate(tile[1]):
                        if connected[i - 1][j][1][n - 1] == mutated[0] and \
                                get_right_border(connected[i][j - 1][1]) == get_left_border(mutated):
                            connected[i][j] = tile[0], mutated
                            print(tile[0])
                            used.add(tile[0])
                            break

                    if success:
                        break

    print(connected[0][0][0] * connected[0][size - 1][0] * connected[size - 1][0][0] * connected[size - 1][size - 1][0])

    field = get_field(connected)
    print(to_string(field))

    for mutated in mutate(field):
        if count(mark_monsters(mutated), 'O') > 0:
            print(count(mutated, '#'))
            break


solve()
