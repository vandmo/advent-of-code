from itertools import count

prog = []

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    instr, *args = line.split(" ")
    prog.append((instr, args))


def solve(registers):
    register_names = "abcd"
    out = []
    visited = set()

    def resolve(arg):
        if arg in register_names:
            return registers[register_names.index(arg)]
        else:
            return int(arg)

    ptr = 0
    while ptr < len(prog):
        instr, args = prog[ptr]
        match instr:
            case (
                "cpy"
            ):  # cpy x y copies x (either an integer or the value of a register) into register y.
                x, y = args
                registers[register_names.index(y)] = resolve(x)
                ptr += 1
            case "inc":  # inc x increases the value of register x by one.
                (x,) = args
                registers[register_names.index(x)] += 1
                ptr += 1
            case "dec":  # decreases the value of register x by one.
                (x,) = args
                registers[register_names.index(x)] -= 1
                ptr += 1
            case (
                "jnz"
            ):  # jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero.
                x, y = args
                if resolve(x) != 0:
                    ptr += int(y)
                else:
                    ptr += 1
            case "out":
                state = tuple(registers), ptr
                (x,) = args
                if state in visited:
                    return "infinite", out
                out.append(resolve(x))
                visited.add(state)
                ptr += 1
            case _:
                assert 0
    return "finite", out


SET0 = set([0])
SET1 = set([1])


def part1():
    for i in count():
        status, result = solve([i, 0, 0, 0])
        if (
            status == "infinite"
            and set(result[0::2]) == SET0
            and set(result[1::2]) == SET1
        ):
            return i


print("ANSWER PART 1:", part1())
