instructions = [line.strip() for line in open("input.txt")]


def rotate(angle, x, y):
    angle %= 360
    match angle:
        case 90:
            return y, -x
        case 180:
            return x * -1, y * -1
        case 270:
            return -y, x
        case _:
            assert False


def move(direction, value, x, y):
    match direction:
        case "S":
            return x, y - value
        case "N":
            return x, y + value
        case "E":
            return x + value, y
        case "W":
            return x - value, y
        case _:
            assert False


def part1():
    x, y = 0, 0
    dirx, diry = 1, 0

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        match action:
            case "S" | "N" | "E" | "W":
                x, y = move(action, value, x, y)
            case "F":
                x += value * dirx
                y += value * diry
            case "R":
                dirx, diry = rotate(value, dirx, diry)
            case "L":
                dirx, diry = rotate(-value, dirx, diry)
            case _:
                assert False
    return abs(x) + abs(y)


def part2():
    x, y = 0, 0
    wx, wy = 10, 1

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        match action:
            case "S" | "N" | "E" | "W":
                wx, wy = move(action, value, wx, wy)
            case "F":
                x += value * wx
                y += value * wy
            case "R":
                wx, wy = rotate(value, wx, wy)
            case "L":
                wx, wy = rotate(-value, wx, wy)
            case _:
                assert False
    return abs(x) + abs(y)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
