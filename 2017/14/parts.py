from functools import reduce
from itertools import batched
from operator import xor


INPUT = open("input.txt").read().strip()


def knothash(s):
    I = list(range(256))
    L = [ord(c) for c in s] + [17, 31, 73, 47, 23]

    skip = 0
    pos = 0
    for _ in range(64):
        for l in L:
            for i in range(l // 2):
                j = pos + i
                i1 = j % len(I)
                i2 = (j + l - i * 2 - 1) % len(I)
                v = I[i1]
                I[i1] = I[i2]
                I[i2] = v
            pos = (pos + l + skip) % len(I)
            skip += 1
    return "".join(f"{reduce(xor, ns, 0):02x}" for ns in batched(I, 16))


def part1():
    return sum(int(knothash(f"{INPUT}-{i}"), 16).bit_count() for i in range(128))


def part2():
    grid = {}

    for y in range(128):
        h = int(knothash(f"{INPUT}-{y}"), 16)
        for x, c in enumerate(f"{h:0128b}"):
            grid[x, y] = c

    visited = set()

    def visit(p):
        if p in visited:
            return
        visited.add(p)
        x, y = p
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            n = x + dx, y + dy
            nc = grid.get(n)
            if nc == "1":
                visit(n)

    cnt = 0
    for y in range(128):
        for x in range(128):
            p = x, y
            c = grid.get(p)
            if c == "1" and p not in visited:
                cnt += 1
                visit(p)
    return cnt


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
