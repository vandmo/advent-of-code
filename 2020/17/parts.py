initial_cubes: set[tuple[int, int]] = set()

for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        if c == "#":
            initial_cubes.add((x, y))


def part1():
    cubes = set((x, y, 0) for x, y in initial_cubes)
    for _ in range(6):
        new_cubes = set()
        neigbour_count: dict[tuple[int, int, int], int] = dict()
        for x, y, z in cubes:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    for dz in range(-1, 2):
                        if dx == 0 and dy == 0 and dz == 0:
                            continue
                        coord = (x + dx, y + dy, z + dz)
                        neigbour_count[coord] = neigbour_count.get(coord, 0) + 1
        for coord in cubes:
            nc = neigbour_count.get(coord, 0)
            if nc in (2, 3):
                new_cubes.add(coord)
        for coord, nc in neigbour_count.items():
            if nc == 3:
                new_cubes.add(coord)
        cubes = new_cubes
    return len(cubes)


def part2():
    cubes = set((x, y, 0, 0) for x, y in initial_cubes)
    for _ in range(6):
        new_cubes = set()
        neigbour_count: dict[tuple[int, int, int, int], int] = dict()
        for x, y, z, w in cubes:
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    for dz in range(-1, 2):
                        for dw in range(-1, 2):
                            if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                                continue
                            coord = (x + dx, y + dy, z + dz, w + dw)
                            neigbour_count[coord] = neigbour_count.get(coord, 0) + 1
        for coord in cubes:
            nc = neigbour_count.get(coord, 0)
            if nc in (2, 3):
                new_cubes.add(coord)
        for coord, nc in neigbour_count.items():
            if nc == 3:
                new_cubes.add(coord)
        cubes = new_cubes

    return len(cubes)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
