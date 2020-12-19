import functools


def get_splits(start, finish, count, split):
    if start >= finish:
        return
    if count == 1:
        yield *split, (start, finish)
    else:
        for i in range(start, finish):
            yield from get_splits(i + 1, finish, count - 1, (*split, (start, i + 1)))


def parse_rules(lines):
    rules = {}
    for line in lines.split('\n'):
        id, desc = line.split(': ')
        if desc.startswith('"'):
            rules[id] = desc[1]
        else:
            rules[id] = [[ruleId for ruleId in option.split(' ')] for option in desc.split(' | ')]
    return rules


def is_valid(message, rules):
    def is_valid_split(split, option):
        return all(parse(option[i], split[i][0], split[i][1]) for i in range(len(option)))

    @functools.cache
    def parse(id, start, finish):
        if start >= finish:
            return False
        if isinstance(rules[id], str):
            return start + len(rules[id]) == finish and rules[id] == message[start:finish]
        for option in rules[id]:
            splits = list(get_splits(start, finish, len(option), ()))
            if any(is_valid_split(split, option) for split in splits):
                return True
        return False
    return parse('0', 0, len(message))


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    rules, messages = input.split('\n\n')
    rules = rules.replace('8: 42', '8: 42 | 42 8')
    rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
    rules = parse_rules(rules)
    messages = messages.split('\n')
    print(sum(1 for m in messages if is_valid(m, rules)))


solve()
