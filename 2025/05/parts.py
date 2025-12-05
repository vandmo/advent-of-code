ingredients = []
ranges = []

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    if "-" in line:
        lower, upper = [int(n) for n in line.split("-")]
        assert lower <= upper
        ranges.append((lower, upper))
    else:
        ingredients.append(int(line))


def part1():
    def is_fresh(ingredient):
        for lower, upper in ranges:
            if ingredient >= lower and ingredient <= upper:
                return True
        return False

    return sum(1 for ingredient in ingredients if is_fresh(ingredient))


def part2(ranges):
    def find_match():
        for i in range(len(ranges) - 1):
            range1_lower, range1_upper = ranges[i]
            for j in range(i + 1, len(ranges)):
                range2_lower, range2_upper = ranges[j]
                if range2_lower <= range1_upper and range2_upper >= range1_lower:
                    return (i, j), (
                        min(range1_lower, range2_lower),
                        max(range1_upper, range2_upper),
                    )
        return None

    while True:
        match = find_match()
        if match is None:
            break
        indices, newrange = match
        ranges = [newrange] + [
            item for index, item in enumerate(ranges) if index not in indices
        ]

    return sum(upper - lower + 1 for lower, upper in ranges)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2(ranges))
