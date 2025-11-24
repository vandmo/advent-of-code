INPUT = open("input.txt").read()


def part1():
    floor = 0
    for c in INPUT:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
    return floor


def part2():
    floor = 0
    n = 1
    for c in INPUT:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor == -1:
            return n
        n += 1


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
