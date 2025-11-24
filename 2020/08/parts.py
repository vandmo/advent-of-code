program = []
for line in open("input.txt"):
    op, arg = line.split()
    program.append((op, int(arg)))


def check(prog):
    var = 0
    ptr = 0
    seen = set()
    while ptr not in seen and ptr < len(prog):
        seen.add(ptr)
        op, arg = prog[ptr]
        match op:
            case "nop":
                ptr += 1
            case "acc":
                var += arg
                ptr += 1
            case "jmp":
                ptr += arg
    return ptr < len(prog), var


print("ANSWER PART 1:", check(program)[1])

for i in range(len(program)):
    newprog = program[:i] + [("nop", 0)] + program[i + 1 :]
    broken, var = check(newprog)
    if not broken:
        print("ANSWER PART 2:", var)
        break
