def is_valid_part1(p):
    parts = list(p.split())
    return len(set(parts)) == len(parts)


def is_valid_part2(p):
    parts = list(p.split())
    return len(set("".join(sorted(part)) for part in parts)) == len(parts)


lines = [line.strip() for line in open("input.txt")]
print("ANSWER PART 1:", sum(1 for line in lines if is_valid_part1(line)))
print("ANSWER PART 2:", sum(1 for line in lines if is_valid_part2(line)))
