def parse(line):
    ingridients, allergens = line.split(' (')
    ingridients = ingridients.split(' ')
    allergens = allergens.replace(')', '').replace('contains ', '').split(', ')
    return ingridients, allergens


def get_mappings(candidates, allergens, pos, mapping):
    if pos == len(allergens):
        yield mapping
        return
    allergen = allergens[pos]
    for candidate in candidates[allergen]:
        if candidate not in mapping:
            mapping[candidate] = allergen
            yield from get_mappings(candidates, allergens, pos + 1, mapping)
            del mapping[candidate]


def is_valid(mapping, foods):
    for food in foods:
        allergens = set(mapping[ingridient] for ingridient in food[0] if ingridient in mapping)
        if not set(food[1]).issubset(allergens):
            return False
    return True


def solve():
    with open('input.txt', 'r') as inputFile:
        input = inputFile.read()
    foods = [parse(line) for line in input.split('\n')]
    ingridients_set = set(x for ingridients, _ in foods for x in ingridients)
    allergens_set = set([x for _, allergens in foods for x in allergens])

    candidates = {}
    for a in allergens_set:
        candidates[a] = set(ingridients_set)
        for food in foods:
            if a in food[1]:
                candidates[a] = candidates[a].intersection(set(food[0]))

    safe = set(ingridients_set)
    for a in allergens_set:
        safe = safe - candidates[a]

    print(sum(1 for food in foods for ingridient in food[0] if ingridient in safe))

    for mapping in get_mappings(candidates, list(allergens_set), 0, {}):
        if is_valid(mapping, foods):
            canonical = sorted([(i, a) for i, a in mapping.items()], key=lambda x: x[1])
            print(','.join(str(x[0]) for x in canonical))
            break


solve()
