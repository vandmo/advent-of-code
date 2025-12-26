from functools import reduce
from itertools import batched
from operator import xor

INPUT = open("input.txt").read().strip()


def part1():
    I = list(range(256))
    L = [int(n) for n in INPUT.split(",")]
    skip = 0
    pos = 0
    for l in L:
        for i in range(l // 2):
            j = pos + i
            i1 = j % len(I)
            i2 = (j + l - i * 2 - 1) % len(I)
            v = I[i1]
            I[i1] = I[i2]
            I[i2] = v
        pos = (pos + l + skip) % len(I)
        skip += 1

    return I[0] * I[1]


def part2():
    I = list(range(256))
    L = [ord(c) for c in INPUT] + [17, 31, 73, 47, 23]

    skip = 0
    pos = 0
    for _ in range(64):
        for l in L:
            for i in range(l // 2):
                j = pos + i
                i1 = j % len(I)
                i2 = (j + l - i * 2 - 1) % len(I)
                v = I[i1]
                I[i1] = I[i2]
                I[i2] = v
            pos = (pos + l + skip) % len(I)
            skip += 1
    return "".join(f"{reduce(xor, ns, 0):02x}" for ns in batched(I, 16))


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
