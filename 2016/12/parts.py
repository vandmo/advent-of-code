prog = []

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    instr, *args = line.split(" ")
    prog.append((instr, args))


def solve(registers):
    register_names = "abcd"

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
            case _:
                assert 0
    return registers[0]


print("ANSWER PART 1:", solve([0] * 4))
print("ANSWER PART 2:", solve([0, 0, 1, 0]))
