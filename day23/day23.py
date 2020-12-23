class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircleBuffer:
    def __init__(self, values):
        self.n = len(values)
        self.nodes = {}
        self.cur = Node(values[0])
        self.nodes[values[0]] = self.cur
        left = self.cur
        right = None
        for value in values[1:]:
            right = Node(value)
            self.nodes[value] = right
            left.next = right
            left = right
        right.next = self.cur

    def get_slice(self):
        start = self.cur.next
        finish = start.next.next

        self.cur.next = finish.next
        finish.next = None

        return start, finish, (start.value, start.next.value, start.next.next.value)

    def find_destination(self, val, sliced):
        for i in range(val, 0, -1):
            if i not in sliced:
                return self.nodes[i]
        for i in range(self.n, val, -1):
            if i not in sliced:
                return self.nodes[i]
        return -1

    def iterate(self):
        cur_cup = self.cur.value
        start_node, finish_node, slice_values = self.get_slice()
        new_pos = self.find_destination(cur_cup - 1, slice_values)
        finish_node.next = new_pos.next
        new_pos.next = start_node
        self.cur = self.cur.next

    def __repr__(self):
        pos = self.cur
        values = []
        for i in range(self.n):
            values.append(pos.value)
            pos = pos.next
        return str(values)


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()

    count = 1_000_000
    cycles = 10_000_000

    values = [int(input[i]) if i < len(input) else i + 1 for i in range(count)]
    cups = CircleBuffer(values)
    for i in range(cycles):
        if i % 100_000 == 0:
            print(i)
        cups.iterate()

    with open('output.txt', 'w') as outputFile:
        outputFile.write(str(cups))

    one = cups.find_destination(1, [])
    print(one.next.value * one.next.next.value)


solve()
