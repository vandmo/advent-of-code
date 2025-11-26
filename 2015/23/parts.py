def run(a, b):
    program = []
    for line in open("input.txt"):
        line = line.strip()
        if not line:
            continue
        instr = line[:3]
        rest = line[3:]
        args = tuple(arg.strip() for arg in rest.split(","))
        program.append((instr, args))

    def as_register_idx(name):
        return 0 if name == "a" else 1

    ptr = 0
    registers = [a, b]
    while ptr < len(program):
        instr, args = program[ptr]
        match instr:
            case "hlf":
                # hlf r sets register r to half its current value, then continues with the next instruction.
                registers[as_register_idx(args[0])] //= 2
                ptr += 1
            case "tpl":
                # tpl r sets register r to triple its current value, then continues with the next instruction.
                registers[as_register_idx(args[0])] *= 3
                ptr += 1
            case "inc":
                # inc r increments register r, adding 1 to it, then continues with the next instruction.
                registers[as_register_idx(args[0])] += 1
                ptr += 1
            case "jmp":
                # jmp offset is a jump; it continues with the instruction offset away relative to itself
                ptr += int(args[0])
            case "jie":
                # jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
                if registers[as_register_idx(args[0])] % 2 == 0:
                    ptr += int(args[1])
                else:
                    ptr += 1
            case "jio":
                # jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
                if registers[as_register_idx(args[0])] == 1:
                    ptr += int(args[1])
                else:
                    ptr += 1
            case _:
                assert False
    return registers[1]


print("ANSWER PART 1:", run(0, 0))
print("ANSWER PART 2:", run(1, 0))
