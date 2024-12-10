from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = defaultdict(lambda: ".")

heads = []
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        v = int(c)
        p = x + y * 1j
        grid[p] = v
        if v == 0:
            heads.append(p)


def reachable_from(p):
    v = grid[p]
    if v == ".":
        return set()
    if v == 9:
        return set([p])
    s = set()
    for step in (1, -1, 1j, -1j):
        if grid[p + step] == v + 1:
            s.update(reachable_from(p + step))
    return s


print("ANSWER", sum(len(reachable_from(head)) for head in heads))
