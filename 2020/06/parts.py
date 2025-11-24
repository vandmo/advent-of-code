def part1():
    groups = []
    group = set()
    for line in open("input.txt"):
        if not line.strip():
            groups.append(group)
            group = set()
        group.update(line.strip())
    groups.append(group)

    return sum(len(group) for group in groups)


def part2():
    groups = []
    group = None
    for line in open("input.txt"):
        if not line.strip():
            groups.append(group)
            group = None
        elif group is None:
            group = set(line.strip())
        else:
            group = group.intersection(set(line.strip()))
    groups.append(group)

    return sum(len(group) for group in groups)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
