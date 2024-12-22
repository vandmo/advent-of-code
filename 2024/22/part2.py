with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


def advance(n):
    n = ((64 * n) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


def generate_lookup(n):
    changes = []
    lookup = dict()
    previous_price = None
    for _ in range(2000):
        price = int(str(n)[-1])
        if previous_price != None:
            changes.append(price - previous_price),
        if len(changes) == 4:
            E = f"{changes[0]}{changes[1]}{changes[2]}{changes[3]}"
            if E not in lookup:
                lookup[E] = price
            changes.pop(0)
        previous_price = price
        n = advance(n)
    return lookup


lookups = tuple(generate_lookup(int(line)) for line in lines)

candidates = set()
for lookup in lookups:
    candidates.update(lookup.keys())

best_deal = 0
for candidate in candidates:
    bananas = sum(lookup.get(candidate, 0) for lookup in lookups)
    if bananas > best_deal:
        best_deal = bananas
        print(f"Found better deal for {best_deal} bananas!")

print(f"Best deal is {best_deal} bananas!")
