INPUT = int(open("input.txt").read().strip())


def part1():
    b = [0]
    pos = 0
    v = 0
    for _ in range(2017):
        v += 1
        pos = (pos + INPUT) % v + 1
        b.insert(pos, v)

    return b[pos + 1]


def part2():
    pos = 0
    v = 0
    ANSWER = 0
    for _ in range(50_000_000):
        v += 1
        pos = (pos + INPUT) % v + 1
        if pos == 1:
            ANSWER = v

    return ANSWER


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
