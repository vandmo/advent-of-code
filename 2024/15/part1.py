from vector2d import Vector2D

V = Vector2D

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = dict()
instructions = ""
robot = None
for y, line in enumerate(lines):
    if line.startswith("#"):
        for x, c in enumerate(line):
            p = V(x, y)
            if c == "@":
                grid[p] = "."
                robot = p
            else:
                grid[p] = c
    else:
        instructions += line.strip()
assert robot is not None

for instr in instructions:
    match instr:
        case "<":
            D = V(-1, 0)
        case ">":
            D = V(1, 0)
        case "^":
            D = V(0, -1)
        case "v":
            D = V(0, 1)
    NP = robot + D
    NNP = robot + D * 2
    N = grid[NP]
    NN = grid.get(NNP, None)
    if N == ".":
        robot = NP
    elif N == "#":
        continue
    else:
        L = 0
        while grid[NP + D * L] == "O":
            L += 1
        assert L > 0
        if grid[NP + D * L] == ".":
            grid[NP] = "."
            grid[NP + D * L] = "O"
            robot = NP

print("ANSWER", sum(k.x + k.y * 100 for k, v in grid.items() if v == "O"))
