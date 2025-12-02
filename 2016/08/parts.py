from collections import defaultdict

grid = defaultdict(lambda: " ")


def apply(instr: str):
    if instr.startswith("rect "):
        arg = instr[len("rect ") :]
        x, y = arg.split("x")
        for x0 in range(int(x)):
            for y0 in range(int(y)):
                grid[(x0, y0)] = "#"
    elif instr.startswith("rotate column "):
        arg = instr[len("rotate column ") :]
        x, by = arg.split(" by ")
        x = int(x.split("=")[1])
        by = int(by)
        col = [grid[(x, cy)] for cy in range(6)]
        col = col[-by:] + col[:-by]
        for cy, c in enumerate(col):
            grid[(x, cy)] = c
    elif instr.startswith("rotate row "):
        arg = instr[len("rotate row ") :]
        y, by = arg.split(" by ")
        y = int(y.split("=")[1])
        by = int(by)
        row = [grid[(cx, y)] for cx in range(50)]
        row = row[-by:] + row[:-by]
        for cx, c in enumerate(row):
            grid[(cx, y)] = c
    else:
        assert 0


for line in open("input.txt"):
    apply(line.strip())

print("ANSWER PART 1:", sum(1 for c in grid.values() if c == "#"))
print("ANSWER PART 2:")

for y in range(6):
    line = ""
    for x in range(50):
        line += grid[(x, y)]
    print(line)
