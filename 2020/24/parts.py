DIRECTIONS = {
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
    "ne": (1, 1),
}

blacks = set()
x, y = 0, 0
for line in open("input.txt"):
    line = line.strip()
    x, y = 0, 0
    while line:
        for direction, (dx, dy) in DIRECTIONS.items():
            if line.startswith(direction):
                x += dx
                y += dy
                line = line[len(direction) :]
                break
        else:
            assert False
    if (x, y) in blacks:
        blacks.remove((x, y))
    else:
        blacks.add((x, y))


def part2(blacks):
    for _ in range(100):
        neighbours = dict()
        for x, y in blacks:
            for dx, dy in DIRECTIONS.values():
                p = x + dx, y + dy
                neighbours[p] = neighbours.get(p, 0) + 1
        new_blacks = set()
        for tile, neigbour_count in neighbours.items():
            if tile in blacks:
                if neigbour_count != 0 and neigbour_count <= 2:
                    new_blacks.add(tile)
            else:
                if neigbour_count == 2:
                    new_blacks.add(tile)
        blacks = new_blacks
    return len(blacks)


print("ANSWER PART 1:", len(blacks))
print("ANSWER PART 2:", part2(blacks))
