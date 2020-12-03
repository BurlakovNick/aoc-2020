def solve():
    with open('input.txt', 'r') as inputFile:
        str = inputFile.read()
    arr = [int(x) for x in str.split()]
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if (arr[i] + arr[j] + arr[k] == 2020):
                    print(arr[i] * arr[j] * arr[k])
                    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solve()