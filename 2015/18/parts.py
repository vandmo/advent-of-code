grid = dict()

for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        if c == "#":
            grid[x, y] = 1
        else:
            grid[x, y] = 0

minx = min(x for x, _ in grid.keys())
maxx = max(x for x, _ in grid.keys())
miny = min(y for _, y in grid.keys())
maxy = max(y for _, y in grid.keys())


def forward(grid):
    new_grid = dict()
    for (x, y), state in grid.items():
        neighbors = sum(
            grid.get((nx, ny), 0)
            for nx, ny in [
                (x + 1, y),
                (x - 1, y),
                (x - 1, y - 1),
                (x, y - 1),
                (x + 1, y - 1),
                (x - 1, y + 1),
                (x, y + 1),
                (x + 1, y + 1),
            ]
        )
        if state == 1:
            if neighbors < 2:
                new_grid[(x, y)] = 0
            elif neighbors in (2, 3):
                new_grid[(x, y)] = 1
            else:
                assert neighbors > 3
                new_grid[(x, y)] = 0
        else:
            assert state == 0
            if neighbors == 3:
                new_grid[(x, y)] = 1
            else:
                new_grid[(x, y)] = 0
    return new_grid


def turn_on_corners(grid):
    grid[minx, miny] = 1
    grid[minx, maxy] = 1
    grid[maxx, miny] = 1
    grid[maxx, maxy] = 1


def part1(grid):
    for _ in range(100):
        grid = forward(grid)
    return sum(grid.values())


def part2(grid):
    for _ in range(100):
        turn_on_corners(grid)
        grid = forward(grid)
    turn_on_corners(grid)
    return sum(grid.values())


print("ANSWER PART 1:", part1(grid))
print("ANSWER PART 2:", part2(grid))
