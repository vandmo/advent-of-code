from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = defaultdict(lambda: "X")

spos = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            assert spos == None
            spos = (x, y)
            grid[(x, y)] = "."
        else:
            grid[(x, y)] = c

assert spos is not None

W = len(lines[0])
H = len(lines)


def is_win():
    pos = spos
    V = set([pos])
    dir = "U"
    while True:
        match dir:
            case "U":
                npos = (pos[0], pos[1] - 1)
                n = grid[npos]
                if n == "#":
                    dir = "R"
                    continue
                elif n == "X":
                    return False
                else:
                    assert n == "."
                    if (npos, dir) in V:
                        return True
                    V.add((npos, dir))
                    pos = npos
            case "R":
                npos = (pos[0] + 1, pos[1])
                n = grid[npos]
                if n == "#":
                    dir = "D"
                    continue
                elif n == "X":
                    return False
                else:
                    assert n == "."
                    if (npos, dir) in V:
                        return True
                    V.add((npos, dir))
                    pos = npos
            case "D":
                npos = (pos[0], pos[1] + 1)
                n = grid[npos]
                if n == "#":
                    dir = "L"
                    continue
                elif n == "X":
                    return False
                else:
                    assert n == "."
                    if (npos, dir) in V:
                        return True
                    V.add((npos, dir))
                    pos = npos
            case "L":
                npos = (pos[0] - 1, pos[1])
                n = grid[npos]
                if n == "#":
                    dir = "U"
                    continue
                elif n == "X":
                    return False
                else:
                    assert n == "."
                    if (npos, dir) in V:
                        return True
                    V.add((npos, dir))
                    pos = npos


s = 0
for x in range(W):
    print(f"{x} of {W}")
    for y in range(H):
        if (x, y) == spos:
            continue
        if grid[(x, y)] == "#":
            continue
        grid[(x, y)] = "#"
        if is_win():
            s += 1
        grid[(x, y)] = "."

print("ANSWER", s)
