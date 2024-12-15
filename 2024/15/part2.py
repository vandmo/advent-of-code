from vector2d import Vector2D

V = Vector2D

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = dict()
instructions = ""
robot = None
boxes = set()
for y, line in enumerate(lines):
    if line.startswith("#"):
        for x, c in enumerate(line):
            p1 = V(x * 2, y)
            p2 = p1 + V(1, 0)
            if c == "@":
                grid[p1] = "."
                grid[p2] = "."
                robot = p1
            elif c == "O":
                grid[p1] = "."
                grid[p2] = "."
                assert p1 not in boxes
                boxes.add(p1)
            else:
                grid[p1] = c
                grid[p2] = c
    else:
        instructions += line.strip()
assert robot is not None


def can_move_h(box, D):
    if box + D * 2 in boxes:
        return can_move_h(box + D * 2, D)
    elif grid[box + D] == "#" or grid[box + D + V(1, 0)] == "#":
        return False
    elif grid[box + D] == ".":
        return True
    else:
        assert False


def move_h(box, D):
    nb = box + D * 2
    if nb in boxes:
        move_h(nb, D)
    boxes.remove(box)
    boxes.add(box + D)


def can_move_v(box, D):
    if grid[box + D] == "#" or grid[box + D + V(1, 0)] == "#":
        return False
    for hD in (V(-1, 0), V(0, 0), V(1, 0)):
        nb = box + D + hD
        if nb in boxes and not can_move_v(nb, D):
            return False
    return True


def move_v(box, D):
    for hD in (V(-1, 0), V(0, 0), V(1, 0)):
        nb = box + D + hD
        if nb in boxes:
            move_v(nb, D)
    boxes.remove(box)
    boxes.add(box + D)


for instr in instructions:
    match instr:
        case "<":
            D = V(-1, 0)
            if grid[robot + D] == "#":
                continue
            else:
                assert robot + D not in boxes
                b = robot + D * 2
                if b in boxes:
                    if can_move_h(b, D):
                        move_h(b, D)
                        robot += D
                else:
                    robot += D
        case ">":
            D = V(1, 0)
            if grid[robot + D] == "#":
                continue
            else:
                assert robot not in boxes
                b = robot + D
                if b in boxes:
                    if can_move_h(b, D):
                        move_h(b, D)
                        robot += D
                else:
                    robot += D
        case "^":
            D = V(0, -1)
            if grid[robot + D] == "#":
                continue
            else:
                b1 = robot + D
                b2 = robot + D - V(1, 0)
                b = None
                if b1 in boxes:
                    assert b2 not in boxes
                    b = b1
                if b2 in boxes:
                    assert b1 not in boxes
                    b = b2
                if b is not None:
                    if can_move_v(b, D):
                        move_v(b, D)
                        robot += D
                else:
                    robot += D
        case "v":
            D = V(0, 1)
            if grid[robot + D] == "#":
                continue
            else:
                b1 = robot + D
                b2 = robot + D - V(1, 0)
                b = None
                if b1 in boxes:
                    assert b2 not in boxes
                    b = b1
                if b2 in boxes:
                    assert b1 not in boxes
                    b = b2
                if b is not None:
                    if can_move_v(b, D):
                        move_v(b, D)
                        robot += D
                else:
                    robot += D

print("ANSWER", sum(box.x + 100 * box.y for box in boxes))
