def get_splits(start, finish, count, split):
    if start >= finish:
        return
    if count == 1:
        split.append((start, finish))
        yield split.copy()
        split.pop()
    else:
        for i in range(start, finish):
            split.append((start, i + 1))
            yield from get_splits(i + 1, finish, count - 1, split)
            split.pop()


class Rule:
    def __init__(self, line):
        id, desc = line.split(': ')
        self.id = int(id)
        if desc.startswith('"'):
            self.token = desc[1]
            self.options = None
            return
        self.token = None
        self.options = [[int(ruleId) for ruleId in option.split(' ')] for option in desc.split(' | ')]

    def parse(self, message, start, finish, rules, cache):
        def is_valid_split(split, option):
            return all(rules[option[i]].parse(message, split[i][0], split[i][1], rules, cache) for i in range(len(option)))
        if start >= finish:
            return False
        if self.token:
            return start + len(self.token) == finish and self.token == message[start:finish]
        if (self.id, start, finish) in cache:
            return cache[self.id, start, finish]
        for option in self.options:
            splits = get_splits(start, finish, len(option), [])
            if any(is_valid_split(split, option) for split in splits):
                cache[self.id, start, finish] = True
                return True
        cache[self.id, start, finish] = False
        return False

    def is_valid(self, message, rules):
        return self.parse(message, 0, len(message), rules, {})


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    rules, messages = input.split('\n\n')
    rules = rules.replace('8: 42', '8: 42 | 42 8')
    rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
    rules = [Rule(x) for x in rules.split('\n')]
    rules = {r.id: r for r in rules}
    messages = messages.split('\n')
    print(sum(1 for m in messages if rules[0].is_valid(m, rules)))


solve()
