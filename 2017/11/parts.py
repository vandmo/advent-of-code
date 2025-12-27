def move(p, step):
    x, y = p
    match step:
        case "n":
            y -= 2
        case "ne":
            y -= 1
            x += 1
        case "se":
            y += 1
            x += 1
        case "s":
            y += 2
        case "sw":
            y += 1
            x -= 1
        case "nw":
            y -= 1
            x -= 1
    return x, y


def steps_from_origo(p):
    x, y = p
    x = abs(x)
    y = abs(y)
    if y < x:
        return x
    else:
        return x + (y - x) // 2


def steps_away(steps):
    part2 = 0
    p = 0, 0
    for step in steps.split(","):
        p = move(p, step)
        part2 = max(part2, steps_from_origo(p))
    return steps_from_origo(p), part2


part1, part2 = steps_away(open("input.txt").read().strip())
print("ANSWER PART 1:", part1)
print("ANSWER PART 2:", part2)
