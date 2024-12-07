from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

W = len(lines[0])
H = len(lines)

grid = defaultdict(lambda: "Q")
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x, y)] = c

s = 0

for x in range(W):
    for y in range(H):
        if grid[(x, y)] == "X":
            if (
                grid[(x - 1, y)] == "M"
                and grid[(x - 2, y)] == "A"
                and grid[(x - 3, y)] == "S"
            ):
                s += 1
            if (
                grid[(x + 1, y)] == "M"
                and grid[(x + 2, y)] == "A"
                and grid[(x + 3, y)] == "S"
            ):
                s += 1
            if (
                grid[(x, y - 1)] == "M"
                and grid[(x, y - 2)] == "A"
                and grid[(x, y - 3)] == "S"
            ):
                s += 1
            if (
                grid[(x, y + 1)] == "M"
                and grid[(x, y + 2)] == "A"
                and grid[(x, y + 3)] == "S"
            ):
                s += 1
            if (
                grid[(x - 1, y - 1)] == "M"
                and grid[(x - 2, y - 2)] == "A"
                and grid[(x - 3, y - 3)] == "S"
            ):
                s += 1
            if (
                grid[(x + 1, y - 1)] == "M"
                and grid[(x + 2, y - 2)] == "A"
                and grid[(x + 3, y - 3)] == "S"
            ):
                s += 1
            if (
                grid[(x - 1, y + 1)] == "M"
                and grid[(x - 2, y + 2)] == "A"
                and grid[(x - 3, y + 3)] == "S"
            ):
                s += 1
            if (
                grid[(x + 1, y + 1)] == "M"
                and grid[(x + 2, y + 2)] == "A"
                and grid[(x + 3, y + 3)] == "S"
            ):
                s += 1

print("ANSWER", s)
