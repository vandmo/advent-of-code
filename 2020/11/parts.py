from typing import Callable, Literal

type Coord = tuple[int, int]
type Grid = dict[Coord, Seat]
type IsWantedCheck = Callable[[Grid, Coord], WantedOrNot]
type Seat = Literal[".", "#", "L", "!"]
type WantedOrNot = Literal["yes", "no", "neutral"]

grid: Grid = dict()

for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        assert c == "." or c == "#" or c == "L" or c == "!"
        grid[x, y] = c

WIDTH = max(x for x, _ in grid.keys()) + 1
HEIGHT = max(y for _, y in grid.keys()) + 1
DIRECTIONS: tuple[Coord, ...] = tuple(
    (dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0
)
NON_EMPTY_SEATS: set[Seat] = set(["!", "#", "L"])


def grid_to_string(grid: Grid) -> str:
    s = ""
    for y in range(HEIGHT):
        line = ""
        for x in range(WIDTH):
            line += grid[x, y]
        s += line + "\n"
    return s


def first_seat_in_direction(grid: Grid, seat: Coord, direction: Coord) -> Seat:
    x, y = seat
    dx, dy = direction
    while True:
        x += dx
        y += dy
        c = grid.get((x, y), "!")
        if c in NON_EMPTY_SEATS:
            return c


def is_wanted_part1(grid: Grid, coord: Coord) -> WantedOrNot:
    x, y = coord
    occupied = sum(1 for dx, dy in DIRECTIONS if grid.get((x + dx, y + dy), ".") == "#")
    if occupied == 0:
        return "yes"
    elif occupied >= 4:
        return "no"
    else:
        return "neutral"


def is_wanted_part2(grid: Grid, coord: Coord) -> WantedOrNot:
    occupied = sum(
        1
        for dx, dy in DIRECTIONS
        if first_seat_in_direction(grid, coord, (dx, dy)) == "#"
    )
    if occupied == 0:
        return "yes"
    elif occupied >= 5:
        return "no"
    else:
        return "neutral"


def simulate(grid: Grid, is_wanted: IsWantedCheck) -> Grid:
    new_grid: Grid = dict()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            c = grid[x, y]
            if c == ".":
                new_grid[x, y] = "."
            else:
                wanted = is_wanted(grid, (x, y))
                if c == "L":
                    new_grid[x, y] = "#" if wanted == "yes" else "L"
                elif c == "#":
                    new_grid[x, y] = "L" if wanted == "no" else "#"
                else:
                    assert False
    return new_grid


def run_simulation(grid: Grid, is_wanted: IsWantedCheck) -> int:
    prev = grid_to_string(grid)
    while True:
        grid = simulate(grid, is_wanted)
        state = grid_to_string(grid)
        if state == prev:
            break
        prev = state
    return sum(1 for c in grid_to_string(grid) if c == "#")


print("ANSWER PART 1:", run_simulation(grid.copy(), is_wanted_part1))
print("ANSWER PART 2:", run_simulation(grid.copy(), is_wanted_part2))
