INPUT = open("input.txt").read()


def movements():
    for c in INPUT:
        match c:
            case "v":
                yield 0, 1
            case "^":
                yield 0, -1
            case "<":
                yield -1, 0
            case ">":
                yield 1, 0


def part1():
    s = set()
    posx, posy = 0, 0
    s.add((posx, posy))
    for c in INPUT:
        match c:
            case "v":
                posy += 1
            case "^":
                posy -= 1
            case "<":
                posx -= 1
            case ">":
                posx += 1
        s.add((posx, posy))

    return len(s)


def part2():
    s = set()
    posx1, posy1 = 0, 0
    posx2, posy2 = 0, 0
    s.add((0, 0))
    for i, c in enumerate(INPUT):
        posyd, posxd = 0, 0
        match c:
            case "v":
                posyd = 1
            case "^":
                posyd = -1
            case "<":
                posxd = -1
            case ">":
                posxd = 1
            case _:
                assert False
        if i % 2 == 0:
            posx1 += posxd
            posy1 += posyd
            s.add((posx1, posy1))
        else:
            posx2 += posxd
            posy2 += posyd
            s.add((posx2, posy2))

    return len(s)


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
