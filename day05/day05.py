def get_seat_id(code):
    row = 0
    for i in range(0, 7):
        row = (row << 1) + (code[i] == 'B')
    col = 0
    for i in range(7, 10):
        col = (col << 1) + (code[i] == 'R')
    return row * 8 + col


def find_free_seat_id(codes):
    seats = {get_seat_id(x) for x in codes}
    return next(i for i in range(1, 1023) if i not in seats and (i + 1) in seats and (i - 1) in seats)


def solve():
    with open('input.txt', 'r') as inputFile:
        str = inputFile.read()
    print(max(get_seat_id(x) for x in str.split()))
    print(find_free_seat_id(str.split()))


solve()
