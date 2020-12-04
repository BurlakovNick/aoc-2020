import re


def valid_int(value, min_value, max_value):
    return value.isdigit() and min_value <= int(value) <= max_value


class IntField:
    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, value):
        return valid_int(value, self.min_value, self.max_value)


class HeightField:
    def __init__(self):
        self.name = 'hgt'

    def is_valid(self, value):
        if value.endswith('cm'):
            height = value[0:-2]
            return valid_int(height, 150, 193)
        if value.endswith('in'):
            height = value[0:-2]
            return valid_int(height, 59, 76)
        return False


class StringField:
    def __init__(self, name, regexp):
        self.name = name
        self.regexp = regexp

    def is_valid(self, value):
        match = re.search(f'^{self.regexp}$', value)
        if match:
            return True
        return False


def is_valid(passport, checks):
    required = {field.name for field in checks}
    checks_map = {check.name: check for check in checks}
    field_names = [field[0] for field in passport]

    return required.issubset(field_names) and all(
        checks_map[field[0]].is_valid(field[1]) for field in passport if checks_map.get(field[0]))


def solve():
    with open('input.txt', 'r') as inputFile:
        str = inputFile.read()
    passports = [[field.split(':') for field in passport.split()] for passport in str.split('\n\n')]

    fields = [
        IntField('byr', 1920, 2002),
        IntField('iyr', 2010, 2020),
        IntField('eyr', 2020, 2030),
        HeightField(),
        StringField('hcl', '#[0-9a-f]{6}'),
        StringField('ecl', '(amb|blu|brn|gry|grn|hzl|oth)'),
        StringField('pid', '[0-9]{9}')
    ]

    print(sum(1 for passport in passports if is_valid(passport, fields)))


solve()
