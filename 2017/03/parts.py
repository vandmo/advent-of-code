from math import isqrt

INPUT = 1024


def part1():
    lv = (isqrt(INPUT - 1) + 1) // 2
    side = lv * 2 + 1
    last = side**2
    remain = (last - INPUT + side // 2) % (side - 1)
    if remain > side // 2:
        remain = side - remain - 1
    return lv + remain


def part2():
    def spiral_next(p: tuple[int, int]) -> tuple[int, int]:
        x, y = p
        layer = max(abs(x), abs(y))
        if x == layer:
            if y == layer:
                return x + 1, y
            elif y == -layer:
                return x - 1, y
            else:
                return x, y - 1
        elif x == -layer:
            if y == layer:
                return x + 1, y
            elif y == -layer:
                return x, y + 1
            else:
                return x, y + 1
        elif y == layer:
            return x + 1, y
        elif y == -layer:
            return x - 1, y
        else:
            assert False

    grid = {}
    p = 0, 0
    grid[p] = 1
    while True:
        p = spiral_next(p)
        x, y = p
        v = sum(
            grid.get((x + dx, y + dy), 0) for dx in range(-1, 2) for dy in range(-1, 2)
        )
        if v > INPUT:
            return v
        grid[p] = v


print("ANSWER PART 1:", part1())
print("ANSWER PART 1:", part2())
