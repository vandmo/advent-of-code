from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = defaultdict(lambda: "X")

pos = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            assert pos == None
            pos = (x, y)
            grid[(x, y)] = "."
        else:
            grid[(x, y)] = c

assert pos is not None

dir = "U"

V = set([pos])
while True:
    match dir:
        case "U":
            npos = (pos[0], pos[1] - 1)
            n = grid[npos]
            if n == "#":
                dir = "R"
                continue
            elif n == "X":
                break
            else:
                assert n == "."
                V.add(npos)
                pos = npos
        case "R":
            npos = (pos[0] + 1, pos[1])
            n = grid[npos]
            if n == "#":
                dir = "D"
                continue
            elif n == "X":
                break
            else:
                assert n == "."
                V.add(npos)
                pos = npos
        case "D":
            npos = (pos[0], pos[1] + 1)
            n = grid[npos]
            if n == "#":
                dir = "L"
                continue
            elif n == "X":
                break
            else:
                assert n == "."
                V.add(npos)
                pos = npos
        case "L":
            npos = (pos[0] - 1, pos[1])
            n = grid[npos]
            if n == "#":
                dir = "U"
                continue
            elif n == "X":
                break
            else:
                assert n == "."
                V.add(npos)
                pos = npos

print("ANSWER", len(V))
