grid = dict()


for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        grid[x, y] = c

DELTAS = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if (dx, dy) != (0, 0)]


counts = []

while True:
    count = 0
    accessible_positions = set()
    for (x, y), v in grid.items():
        adjacent_count = 0
        if v == "@":
            for dx, dy in DELTAS:
                if grid.get((x + dx, y + dy), ".") == "@":
                    adjacent_count += 1
            if adjacent_count < 4:
                count += 1
                accessible_positions.add((x, y))
    for x, y in accessible_positions:
        grid[x, y] = "."
    if count == 0:
        break
    counts.append(count)

print("ANSWER PART 1:", counts[0])
print("ANSWER PART 2:", sum(counts))
