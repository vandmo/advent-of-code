from functools import cache
from itertools import pairwise

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

number_board_rows = [
    "789",
    "456",
    "123",
    " 0A",
]

direction_board_rows = [
    " ^A",
    "<v>",
]


def rows_to_grid(rows):
    grid = dict()
    for y, row in enumerate(rows):
        for x, c in enumerate(row):
            grid[c] = (x, y)
    return grid


number_board_grid = rows_to_grid(number_board_rows)
direction_board_grid = rows_to_grid(direction_board_rows)


def ways_from_XY(grid, source, target):
    result = ""
    sx, sy = grid[source]
    tx, ty = grid[target]
    for x in range(min(sx, tx), max(sx, tx)):
        if grid[" "] == (x, sy):
            return None
        elif sx < tx:
            result += ">"
        elif sx > tx:
            result += "<"
        else:
            assert False
    for y in range(min(sy, ty), max(sy, ty)):
        if grid[" "] == (tx, y):
            return None
        elif sy < ty:
            result += "v"
        elif sy > ty:
            result += "^"
        else:
            assert False
    return result + "A"


def ways_from_YX(grid, source, target):
    result = ""
    sx, sy = grid[source]
    tx, ty = grid[target]
    for y in range(min(sy, ty), max(sy, ty)):
        if grid[" "] == (sx, y):
            return None
        elif sy < ty:
            result += "v"
        elif sy > ty:
            result += "^"
        else:
            assert False
    for x in range(min(sx, tx), max(sx, tx)):
        if grid[" "] == (x, ty):
            return None
        elif sx < tx:
            result += ">"
        elif sx > tx:
            result += "<"
        else:
            assert False
    return result + "A"


@cache
def ways_to_press_number(source, target):
    if source == target:
        return ("A",)
    # Going XYX or YXY or similar can never be shorter than just XY or YX
    xy = ways_from_XY(number_board_grid, source, target)
    yx = ways_from_YX(number_board_grid, source, target)
    return tuple(set((v for v in (xy, yx) if v is not None)))


@cache
def ways_to_press_direction(source, target):
    if source == target:
        return ("A",)
    # Going XYX or YXY or similar can never be shorter than just XY or YX
    xy = ways_from_XY(direction_board_grid, source, target)
    yx = ways_from_YX(direction_board_grid, source, target)
    return tuple(set((v for v in (xy, yx) if v is not None)))


@cache
def shortest_for_direction_step(source, target, steps_left):
    if steps_left == 0:
        return min(
            sum(
                min(
                    len(way)
                    for way in ways_to_press_direction(
                        current_direction, wanted_direction
                    )
                )
                for current_direction, wanted_direction in pairwise(
                    "A" + way_to_press_direction
                )
            )
            for way_to_press_direction in ways_to_press_direction(source, target)
        )
    else:
        return min(
            sum(
                shortest_for_direction_step(
                    current_direction, wanted_direction, steps_left - 1
                )
                for current_direction, wanted_direction in pairwise(
                    "A" + way_to_press_direction
                )
            )
            for way_to_press_direction in ways_to_press_direction(source, target)
        )


def shortest_for_number(source, target, number_of_directional_keypads):
    return min(
        sum(
            shortest_for_direction_step(
                current_number, wanted_number, number_of_directional_keypads - 2
            )
            for current_number, wanted_number in pairwise("A" + way_to_press_number)
        )
        for way_to_press_number in ways_to_press_number(source, target)
    )


def find_answer(number_of_directional_keypads):
    return sum(
        int(line[0:3])
        * sum(
            shortest_for_number(source, target, number_of_directional_keypads)
            for source, target in pairwise("A" + line)
        )
        for line in lines
    )


print("ANSWER PART1", find_answer(2))
print("ANSWER PART2", find_answer(25))
