from math import prod

grid = {}

for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        grid[(x, y)] = c

width = max(x for x, _ in grid.keys()) + 1
height = max(y for _, y in grid.keys()) + 1


def traverse(Mx, My):
    s = 0
    x = 0
    for y in range(My, height, My):
        x = (x + Mx) % width
        if grid[(x, y)] == "#":
            s += 1
    return s


print("ANSWER PART 1:", traverse(3, 1))
print(
    "ANSWER PART 2:",
    prod(traverse(Mx, My) for Mx, My in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]),
)
