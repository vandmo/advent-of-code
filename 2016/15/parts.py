def parse(line):
    line = line.strip()
    _, rest = line.split(" has ")
    npos, rest = rest.split(" positions;")
    _, startpos = rest.split(" at position ")
    return int(npos), int(startpos.removesuffix("."))


DISCS = [parse(line) for line in open("input.txt") if line.strip()]


def solve(discs):
    n = 0
    inc = 1
    for i, (m, s) in enumerate(discs):
        while (n + i + s + 1) % m != 0:
            n += inc
        inc *= m
    return n


print("ANSWER PART 1:", solve(DISCS))
print("ANSWER PART 2:", solve(DISCS + [(11, 0)]))
