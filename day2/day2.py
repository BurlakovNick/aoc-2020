def is_correct_1(str):
    limits, char, password = str.split(' ')
    lower_bound, upper_bound = [int(x) for x in limits.split('-')]
    cnt = password.count(char[0])
    return lower_bound <= cnt <= upper_bound


def is_correct_2(str):
    limits, char, password = str.split(' ')
    left, right = [int(x) - 1 for x in limits.split('-')]
    expected = char[0]
    return (password[left] == expected) ^ (password[right] == expected)


def solve():
    with open('input.txt', 'r') as inputFile:
        str = inputFile.read()
    result = [is_correct_2(x) for x in str.split('\n')].count(True)
    print(result)


solve()
