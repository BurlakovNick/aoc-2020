def get_new_state2(seats, x, y):
    if seats[x][y] == '.':
        return seats[x][y]
    busy = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            i = 1
            while 0 <= x + dx * i < len(seats) and 0 <= y + dy * i < len(seats[0]):
                if seats[x + dx * i][y + dy * i] == '.':
                    i += 1
                else:
                    busy += seats[x + dx * i][y + dy * i] == '#'
                    break
    if seats[x][y] == 'L' and busy == 0:
        return '#'
    if seats[x][y] == '#' and busy >= 5:
        return 'L'
    return seats[x][y]


def get_new_state(seats, x, y):
    if seats[x][y] == '.':
        return seats[x][y]
    busy = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < len(seats) and 0 <= y + dy < len(seats[0]):
                busy += seats[x + dx][y + dy] == '#'
    if seats[x][y] == 'L' and busy == 0:
        return '#'
    if seats[x][y] == '#' and busy >= 4:
        return 'L'
    return seats[x][y]


def iterate(seats, new_state_func):
    def get_line(x):
        return ''.join(new_state_func(seats, x, y) for y in range(len(seats[0])))
    return [get_line(x) for x in range(len(seats))]


def go(seats, new_state_func):
    while (new_seats := iterate(seats, new_state_func)) != seats:
        seats = new_seats
    return seats


def count_busy(seats):
    return sum(seats[x][y] == '#' for x in range(len(seats)) for y in range(len(seats[0])))


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    seats = input.split()
    finished = go(seats, get_new_state)
    print(count_busy(finished))
    finished = go(seats, get_new_state2)
    print(count_busy(finished))


solve()
