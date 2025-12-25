INPUT = tuple(int(n) for n in open("input.txt"))


def part1():
    ptr = 0
    instrs = list(INPUT)
    count = 1
    while True:
        offset = instrs[ptr]
        nptr = ptr + offset
        instrs[ptr] += 1
        if nptr < len(instrs):
            ptr = nptr
        else:
            break
        count += 1
    return count


def part2():
    ptr = 0
    instrs = list(INPUT)
    count = 1
    while True:
        offset = instrs[ptr]
        nptr = ptr + offset
        if offset >= 3:
            instrs[ptr] -= 1
        else:
            instrs[ptr] += 1
        if nptr < len(instrs):
            ptr = nptr
        else:
            break
        count += 1
    return count


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
