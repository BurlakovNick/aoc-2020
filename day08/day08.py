class Command:
    def __init__(self, desc):
        cmd, arg = desc.split(' ')
        self.cmd = cmd
        self.arg = int(arg)
        self.executed = False

    def execute(self, acc, pos):
        self.executed = True
        if self.cmd == 'nop':
            return acc, pos + 1
        if self.cmd == 'acc':
            return acc + self.arg, pos + 1
        if self.cmd == 'jmp':
            return acc, pos + self.arg


def execute(commands):
    acc, pos = 0, 0
    for command in commands:
        command.executed = False
    while pos < len(commands) and not commands[pos].executed:
        acc, pos = commands[pos].execute(acc, pos)
    return pos == len(commands), acc


def fix_bug(commands):
    fix = {'jmp': 'nop', 'nop': 'jmp'}
    for command in commands:
        if command.cmd in fix.keys():
            command.cmd = fix[command.cmd]
            finished, acc = execute(commands)
            if finished:
                return acc
            command.cmd = fix[command.cmd]


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    commands = [Command(line) for line in input.split('\n')]
    print(execute(commands))
    print(fix_bug(commands))


solve()
