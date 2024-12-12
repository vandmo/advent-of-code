from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = defaultdict(lambda: ".")

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x + y * 1j] = c

W = len(lines[0])
H = len(lines)

visited = set()


def find_region(p):
    if p in visited:
        return 0 + 0j
    visited.add(p)
    c = grid[p]
    if c == ".":
        return 0 + 0j
    res = 1 + 0j
    for d in (1, -1, 1j, -1j):
        np = p + d
        n = grid[np]
        if n == c:
            res += find_region(np)
        else:
            res += 1j
    return res


s = 0
for x in range(W):
    for y in range(H):
        r = find_region(x + y * 1j)
        s += r.real * r.imag
print("ANSWER", int(s))
