def execute(commands):
    mask = 0
    mask_replace = 0
    mem = {}
    for command in commands:
        left, right = command.split(' = ')
        if left == 'mask':
            mask = int(right.replace('0', '1').replace('X', '0'), 2)
            mask_replace = int(right.replace('X', '0'), 2)
        else:
            value = int(right)
            mem[left] = value - (value & mask) + mask_replace
    return sum(mem.values())


def get_addresses(mask, origin, pos=0, res=''):
    if pos == 36:
        yield res
        return
    if mask[pos] == '0':
        yield from get_addresses(mask, origin, pos + 1, res + origin[pos])
    if mask[pos] == '1':
        yield from get_addresses(mask, origin, pos + 1, res + '1')
    if mask[pos] == 'X':
        yield from get_addresses(mask, origin, pos + 1, res + '0')
        yield from get_addresses(mask, origin, pos + 1, res + '1')


def execute2(commands):
    mask = 0
    mem = {}
    for command in commands:
        left, right = command.split(' = ')
        if left == 'mask':
            mask = right
        else:
            _, address = left.replace('[', ' ').replace(']', ' ').split()
            origin = f'{int(address):036b}'
            for ptr in get_addresses(mask, origin):
                mem[ptr] = int(right)
    return sum(mem.values())


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    commands = input.split('\n')
    print(execute(commands))
    print(execute2(commands))


solve()
