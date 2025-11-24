instructions = []

for line in open("input.txt"):
    p1, p2, p3 = line.strip().split()
    assert p2 == "="
    if p1 == "mask":
        instructions.append(("mask", p3))
    else:
        assert p1.startswith("mem[")
        instructions.append(
            ("mem", int(p1.removeprefix("mem[").removesuffix("]")), int(p3))
        )


def part1():
    rev_mask = "X" * 32
    mem = dict()

    for instr in instructions:
        match instr:
            case ("mask", mask):
                rev_mask = mask[::-1]
            case ("mem", addr, value):
                value = bin(value).removeprefix("0b").zfill(36)
                b = ""
                for i, n in enumerate(value[::-1]):
                    c = rev_mask[i]
                    match c:
                        case "X":
                            b = n + b
                        case "0" | "1":
                            b = c + b
                        case _:
                            assert False
                mem[addr] = int(b, 2)
            case _:
                assert False
    return sum(mem.values())


def part2():
    rev_mask = "0" * 32
    mem = dict()

    def write_to_memory(p1, p2: str, value):
        if not "X" in p2:
            addr = int(p1 + p2, 2)
            # print(p1, p2, addr, value)
            mem[addr] = value
        else:
            before, after = p2.split("X", 1)
            write_to_memory(p1 + before + "0", after, value)
            write_to_memory(p1 + before + "1", after, value)

    for instr in instructions:
        match instr:
            case ("mask", mask):
                rev_mask = mask[::-1]
            case ("mem", addr, value):
                addr = bin(addr).removeprefix("0b").zfill(36)
                b = ""
                for i, n in enumerate(addr[::-1]):
                    c = rev_mask[i]
                    match c:
                        case "X" | "1":
                            b = c + b
                        case "0":
                            b = n + b
                        case _:
                            assert False
                write_to_memory("", b, value)
    return sum(mem.values())


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
