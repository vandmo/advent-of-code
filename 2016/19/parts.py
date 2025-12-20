from dataclasses import dataclass
from typing import Self

INPUT = 5


def part1():
    def step(first, inc, count):
        if count % 2 == 0:
            return first, inc * 2, count // 2
        else:
            inc *= 2
            return first + inc, inc, count // 2

    first = 1
    inc = 1
    count = INPUT

    while count > 1:
        first, inc, count = step(first, inc, count)
    return first


def part2():

    @dataclass
    class Elf:
        number: int
        neighbour: Self | None = None

    elf1 = Elf(number=1)
    elf = elf1

    N = INPUT
    melf = None
    for i in range(2, N + 1):
        if i == (N // 2) + 1:
            melf = elf
        nelf = Elf(number=i)
        elf.neighbour = nelf
        elf = nelf
    elf.neighbour = elf1

    if N % 2 == 1:
        melf.neighbour = melf.neighbour.neighbour
        melf = melf.neighbour

    while melf != melf.neighbour.neighbour:
        melf.neighbour = melf.neighbour.neighbour.neighbour
        melf = melf.neighbour

    return melf.number


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
