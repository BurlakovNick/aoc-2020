def calc(start, buses):
    def get_wait_time(bus):
        return (bus - start % bus) % bus

    def get_departure_time(bus):
        return get_wait_time(bus) + start

    best_bus = buses[0]
    earliest_time = get_departure_time(best_bus)
    for bus in buses:
        if bus == 'x':
            continue
        departure = get_departure_time(bus)
        if departure < earliest_time:
            earliest_time = departure
            best_bus = bus
    return best_bus * get_wait_time(best_bus)


def get_reversed(x, modulo):
    return x ** (modulo - 2) % modulo


def calc2(buses):
    a = []
    p = []
    for i in range(len(buses)):
        if buses[i] == 'x':
            continue
        p.append(buses[i])
        a.append((buses[i] - i) % buses[i])
    x = [0] * len(p)
    result = 0
    mult = 1
    for i in range(len(p)):
        x[i] = a[i]
        for j in range(i):
            x[i] = get_reversed(p[j], p[i]) * (x[i] - x[j])
            x[i] = (x[i] % p[i] + p[i]) % p[i]
        result += x[i] * mult
        mult *= p[i]
    return result


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    lines = input.split()
    start = int(lines[0])
    buses = [int(x) if x != 'x' else x for x in lines[1].split(',')]
    print(calc(start, buses))
    print(calc2(buses))


solve()