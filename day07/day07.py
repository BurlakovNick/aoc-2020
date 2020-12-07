import re


class Contained:
    def __init__(self, description):
        cnt, name = description.split(' ', 1)
        self.cnt = int(cnt)
        self.name = name

    def __str__(self):
        return f'{self.cnt} {self.name}'


class Bag:
    def __init__(self, description):
        name, contains = description.split(' bags contain ')
        self.name = name
        if contains == 'no other bags.':
            self.contains = []
            return
        contains = [bag.strip() for bag in re.split(r'bags?[\,\.]|bag[\,\.]', contains) if bag != '']
        self.contains = [Contained(bag) for bag in contains]

    def __str__(self):
        return f'{self.name}: {", ".join(str(x) for x in self.contains)}'


def dfs(bags, used, start, goal):
    if start == goal:
        return True
    if start in used:
        return False
    used.add(start)
    for new_bag in bags[start].contains:
        if dfs(bags, used, new_bag.name, goal):
            return True
    return False


def can_reach(goal, start, bags):
    used = set()
    return dfs(bags, used, start, goal)


def calc(bags, required, start):
    if start in required:
        return required[start]
    cnt = 1
    for new_bag in bags[start].contains:
        cnt += new_bag.cnt * calc(bags, required, new_bag.name)
    required[start] = cnt
    return cnt


def count_bags(bags):
    required = {}
    return calc(bags, required, 'shiny gold')


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    bags = [Bag(line) for line in input.split('\n')]
    bags = {bag.name: bag for bag in bags}
    print(sum(1 for bag in bags if can_reach('shiny gold', bag, bags)) - 1)
    print(count_bags(bags) - 1)


solve()
