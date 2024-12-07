with open("input.txt") as f:
    lines = f.readlines()

grid = dict()

pos = None
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == "^":
            assert pos == None
            pos = x + y * 1j
            grid[pos] = "."
        else:
            grid[x + y * 1j] = c

assert pos is not None

dir = -1j

V = set([pos])
while True:
    npos = pos + dir
    if npos not in grid:
        break
    n = grid[npos]
    if n == "#":
        dir *= 1j
    else:
        assert n == "."
        V.add(npos)
        pos = npos

W = len(lines[0])
H = len(lines)
for y in range(H):
    l = ""
    for x in range(W):
        if x + y * 1j in V:
            l += "X"
        else:
            l += grid[x + y * 1j]


print("ANSWER", len(V))
