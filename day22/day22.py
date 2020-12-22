from functools import cache


def simple_play_round(left, right):
    return 0 if left[0] > right[0] else 1


def hard_play_round(left, right):
    x = left[0]
    y = right[0]
    if len(left) <= x or len(right) <= y:
        return simple_play_round(left, right)
    winner, _ = hard_play(left[1:x + 1], right[1:y + 1])
    return winner


def play(left, right, play_round):
    used = set()
    while len(left) > 0 and len(right) > 0:
        if (left, right) in used:
            return 0, ()
        used.add((left, right))
        if play_round(left, right) == 0:
            left, right = left[1:] + (left[0], right[0]), right[1:]
        else:
            left, right = left[1:], right[1:] + (right[0], left[0])
    winner = 0 if len(left) > 0 else 1
    deck = left if winner == 0 else right
    return winner, deck


def simple_play(left, right):
    return play(left, right, simple_play_round)


@cache
def hard_play(left, right):
    return play(left, right, hard_play_round)


def get_answer(deck):
    ans = 0
    for i in range(len(deck)):
        ans += (len(deck) - i) * deck[i]
    return ans


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    p1, p2 = input.split('\n\n')
    left = tuple(int(x) for x in p1.split('\n')[1:])
    right = tuple(int(x) for x in p2.split('\n')[1:])

    _, deck = simple_play(left, right)
    print(get_answer(deck))

    _, deck = hard_play(left, right)
    print(get_answer(deck))


solve()
