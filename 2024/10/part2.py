from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = defaultdict(lambda: ".")

heads = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        v = int(c)
        p = (x, y)
        grid[p] = v
        if v == 0:
            heads.append(p)


def reachable_from(p):
    v = grid[p]
    x, y = p
    if v == ".":
        return 0
    if v == 9:
        return 1
    s = 0
    for neighbor in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
        if grid[neighbor] == v + 1:
            s += reachable_from(neighbor)
    return s


print("ANSWER", sum(reachable_from(head) for head in heads))
