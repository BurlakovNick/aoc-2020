class Rule:
    def __init__(self, line):
        self.name, boundaries = line.split(': ')
        b1, b2 = boundaries.split(' or ')
        l1, r1 = b1.split('-')
        l2, r2 = b2.split('-')
        self.left1, self.right1 = int(l1), int(r1)
        self.left2, self.right2 = int(l2), int(r2)

    def is_valid(self, value):
        return self.left1 <= value <= self.right1 or self.left2 <= value <= self.right2

    def __repr__(self):
        return f'{self.name}: {self.left1}-{self.right1} or {self.left2}-{self.right2}'


class Ticket:
    def __init__(self, line):
        self.values = [int(x) for x in line.split(',')]

    def get_error_rate(self, rules):
        def is_invalid(value):
            return all(not rule.is_valid(value) for rule in rules)
        return sum(value for value in self.values if is_invalid(value))


def get_error_rate(tickets, rules):
    return sum(ticket.get_error_rate(rules) for ticket in tickets)


def is_valid_rule(rule, tickets, position):
    return all(rule.is_valid(ticket.values[position]) for ticket in tickets)


def dfs(rule, used, match, rules, tickets):
    if rule.name in used:
        return False
    used.add(rule.name)
    for i in range(len(rules)):
        if is_valid_rule(rule, tickets, i):
            if i not in match or dfs(match[i], used, match, rules, tickets):
                match[i] = rule
                return True
    return False


def get_order(tickets, rules):
    valid_tickets = [ticket for ticket in tickets if ticket.get_error_rate(rules) == 0]
    match = {}
    for rule in rules:
        dfs(rule, set(), match, rules, valid_tickets)
    order = [None] * len(rules)
    for position, rule in match.items():
        order[position] = rule
    return order


def find_product(rules, ticket):
    x = 1
    for i in range(len(rules)):
        if rules[i] and rules[i].name.startswith('departure'):
            x *= ticket.values[i]
    return x


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    rules, your_ticket, nearby_tickets = input.split('\n\n')
    rules = [Rule(x) for x in rules.split('\n')]
    your_ticket = Ticket(your_ticket.split('\n')[1])
    nearby_tickets = [Ticket(x) for x in nearby_tickets.split('\n')[1:]]
    print(get_error_rate(nearby_tickets, rules))
    order = get_order(nearby_tickets, rules)
    print(find_product(order, your_ticket))


solve()
