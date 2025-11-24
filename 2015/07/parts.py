circuits = dict()

for line in open("input.txt"):
    lhs, rhs = line.split(" -> ")
    rhs = rhs.strip()
    circuits[rhs] = lhs


def resolve(circuit, cache):
    if circuit in cache:
        return cache[circuit]
    if " AND " in circuit:
        lhs, rhs = circuit.split(" AND ")
        resolved = resolve(lhs, cache) & resolve(rhs, cache)
    elif " OR " in circuit:
        lhs, rhs = circuit.split(" OR ")
        resolved = resolve(lhs, cache) | resolve(rhs, cache)
    elif " RSHIFT " in circuit:
        lhs, rhs = circuit.split(" RSHIFT ")
        resolved = resolve(lhs, cache) >> resolve(rhs, cache)
    elif " LSHIFT " in circuit:
        lhs, rhs = circuit.split(" LSHIFT ")
        resolved = resolve(lhs, cache) << resolve(rhs, cache)
    elif "NOT " in circuit:
        rhs = circuit.split("NOT ")[1]
        resolved = ~resolve(rhs, cache)
    elif all([c in "abcdefghijklmnopqrstuvwxyz" for c in circuit]):
        resolved = resolve(circuits[circuit], cache)
    else:
        resolved = int(circuit)
    cache[circuit] = resolved
    return resolved


part1 = resolve("a", dict())
print("ANSWER PART 1:", part1)
circuits["b"] = str(part1)
part2 = resolve("a", dict())
print("ANSWER PART 2:", part2)
