def solve(prog, registers):
    register_names = "abcd"

    def resolve(arg):
        if arg in register_names:
            return registers[register_names.index(arg)]
        else:
            return int(arg)

    ptr = 0
    while ptr < len(prog):
        instr, args = prog[ptr]
        if prog[ptr : ptr + 5] == [
            ("inc", ["a"]),
            ("dec", ["c"]),
            ("jnz", ["c", "-2"]),
            ("dec", ["d"]),
            ("jnz", ["d", "-5"]),
        ]:
            registers[0] = registers[0] + registers[2] * registers[3]
            registers[2] = 0
            registers[3] = 0
            ptr += 5
            continue
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
                    ptr += resolve(y)
                else:
                    ptr += 1
            case "tgl":
                (x,) = args
                target_ptr = ptr + resolve(x)
                if target_ptr < len(prog):
                    target_instr, target_args = prog[target_ptr]
                    if target_instr == "inc":
                        prog[target_ptr] = "dec", target_args
                    elif len(target_args) == 1:
                        prog[target_ptr] = "inc", target_args
                    elif target_instr == "jnz":
                        prog[target_ptr] = "cpy", target_args
                    elif len(target_args) == 2:
                        prog[target_ptr] = "jnz", target_args
                    else:
                        assert 0
                ptr += 1
            case _:
                assert 0
    return registers[0]


prog = []

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    instr, *args = line.split(" ")
    prog.append((instr, args))

print("ANSWER PART 1:", solve(prog.copy(), [7, 0, 0, 0]))
print("ANSWER PART 2:", solve(prog.copy(), [12, 0, 0, 0]))
