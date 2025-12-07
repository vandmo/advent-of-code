from functools import cache

grid = dict()
start = None
for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        if c == "S":
            start = x, y
        grid[x, y] = c
assert start is not None
sx, sy = start


def part1():
    visited = set()

    def splits(x, y):
        c = grid.get((x, y), " ")
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        match c:
            case ".":
                return splits(x, y + 1)
            case "^":
                return 1 + splits(x + 1, y + 1) + splits(x - 1, y + 1)
            case _:
                return 0

    return splits(sx, sy + 1)


def part2():
    @cache
    def timelines(x, y):
        c = grid.get((x, y), " ")
        match c:
            case ".":
                return timelines(x, y + 1)
            case "^":
                return timelines(x + 1, y + 1) + timelines(x - 1, y + 1)
            case _:
                return 1

    return timelines(sx, sy + 1)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
