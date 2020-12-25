def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    a, b = [int(x) for x in input.split('\n')]

    cur = 1
    for i in range(1, 20201227):
        cur = (cur * 7) % 20201227
        if cur == a:
            ans = 1
            for j in range(i):
                ans = ans * b % 20201227
            print(ans)
            break


solve()
