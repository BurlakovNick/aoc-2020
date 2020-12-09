class Multiset:
    def __init__(self):
        self.cnt = {}

    def add(self, *values):
        for value in values:
            if value not in self.cnt:
                self.cnt[value] = 0
            self.cnt[value] = self.cnt[value] + 1

    def remove(self, *values):
        for value in values:
            self.cnt[value] = self.cnt[value] - 1
            if self.cnt[value] == 0:
                self.cnt.pop(value)

    def __contains__(self, item):
        return item in self.cnt


def get_not_valid(xmas):
    preamble = xmas[:25]
    message = xmas[25:]
    sums = Multiset()
    for i in range(len(preamble)):
        for j in range(i, len(preamble)):
            sums.add(preamble[i] + preamble[j])
    for x in message:
        if x not in sums:
            yield x
        last = preamble.pop(0)
        sums.remove(*(last + p for p in preamble))
        sums.add(*(x + p for p in preamble))
        preamble.append(x)


def find_weakness(xmas, target):
    for i in range(len(xmas)):
        sum = xmas[i]
        mn = xmas[i]
        mx = xmas[i]
        for j in range(i + 1, len(xmas)):
            sum += xmas[j]
            mn = min(mn, xmas[j])
            mx = max(mx, xmas[j])
            if sum > target:
                break
            if sum == target:
                return mn + mx


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    xmas = [int(x) for x in input.split()]
    invalid = next(get_not_valid(xmas))
    print(invalid)
    print(find_weakness(xmas, invalid))


solve()
