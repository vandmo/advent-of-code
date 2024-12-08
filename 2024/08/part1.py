from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

antinodes = set()
W = len(lines[0])
H = len(lines)


@dataclass(frozen=True)
class Point2D:
    x: int
    y: int

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def is_in_map(self):
        return self.x >= 0 and self.x < W and self.y >= 0 and self.y < H


nodemap = defaultdict(lambda: [])
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c != ".":
            nodemap[c].append(Point2D(x, y))

for nodes in nodemap.values():
    for a, b in combinations(nodes, 2):
        diff = b - a
        antinodes.add(a - diff)
        antinodes.add(b + diff)

print("ANSWER", sum(1 for p in antinodes if p.is_in_map()))
