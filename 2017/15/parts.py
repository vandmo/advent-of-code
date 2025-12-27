"""
Generator A starts with 618
Generator B starts with 814
"""

A_FAC = 16807
B_FAC = 48271
M = 2147483647
A, B = [int(line.split(" with ")[1]) for line in open("input.txt")]


def part1():
    cnt = 0
    a = A
    b = B
    for _ in range(40_000_000):
        a = (a * A_FAC) % M
        b = (b * B_FAC) % M
        if bin(a)[-16:] == bin(b)[-16:]:
            cnt += 1
    return cnt


def part2():
    cnt = 0
    a = A
    b = B
    for _ in range(5_000_000):
        while True:
            a = (a * A_FAC) % M
            if a % 4 == 0:
                break
        while True:
            b = (b * B_FAC) % M
            if b % 8 == 0:
                break
        if bin(a)[-16:] == bin(b)[-16:]:
            cnt += 1
    return cnt


print("Could take a minute or two...")
print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
