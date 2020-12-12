moves = {'N': (-1, 0), 'E': (0, +1), 'S': (+1, 0), 'W': (0, -1)}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, angle):
        for i in range(angle // 90):
            if angle > 0:
                self.x, self.y = self.y, -self.x
            else:
                self.x, self.y = -self.y, self.x

    def move(self, dir, cnt):
        delta = moves[dir] if dir in moves else (dir.x, dir.y)
        self.x += delta[0] * cnt
        self.y += delta[1] * cnt

    def dist(self):
        return abs(self.x) + abs(self.y)


class State:
    def __init__(self, pos, waypoint=None):
        self.pos = pos
        self.waypoint = waypoint
        self.dir = Point(+1, 0)

    def execute(self, command):
        action = command[0]
        arg = int(command[1:])
        if action in 'NESW':
            if self.waypoint:
                self.waypoint.move(action, arg)
            else:
                self.pos.move(action, arg)
        if action == 'F':
            self.pos.move(self.waypoint if self.waypoint else self.dir, arg)
        if action in 'LR':
            if action == 'L':
                arg = -arg;
            if self.waypoint:
                self.waypoint.rotate(arg)
            else:
                self.dir.rotate(arg)


def execute(commands, waypoint=None):
    state = State(Point(0, 0), waypoint)
    for command in commands:
        state.execute(command)
    return state.pos.dist()


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    commands = input.split()
    print(execute(commands))
    print(execute(commands, Point(-1, 10)))


solve()
