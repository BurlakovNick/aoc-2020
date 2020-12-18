def simple_calc(tokens):
    res = int(tokens[0])
    for i in range(1, len(tokens), 2):
        if tokens[i] == '+':
            res += int(tokens[i + 1])
        if tokens[i] == '*':
            res *= int(tokens[i + 1])
    return res


def advanced_calc(tokens):
    while '+' in tokens:
        pos = tokens.index('+')
        sum = int(tokens[pos - 1]) + int(tokens[pos + 1])
        tokens = [*tokens[:pos - 1], sum, *tokens[pos + 2:]]
    return simple_calc(tokens)


def eval(line, calc):
    tokens = [t for t in f'({line})'.replace('(', ' ( ').replace(')', ' ) ').split(' ') if t != '']
    stack = []
    for token in tokens:
        if token == ')':
            expression = []
            while (last := stack.pop()) != '(':
                expression.append(last)
            expression.reverse()
            stack.append(calc(expression))
        else:
            stack.append(token)
    print('stack[0]')
    return stack[0]


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    lines = input.split('\n')
    print(sum(eval(x, simple_calc) for x in lines))
    print(sum(eval(x, advanced_calc) for x in lines))


solve()
