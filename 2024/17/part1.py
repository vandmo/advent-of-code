def resolve_combo(state, v):
    A, B, C = state
    match v:
        case 0 | 1 | 2 | 3:
            return v
        case 4:
            return A
        case 5:
            return B
        case 6:
            return C
        case _:
            assert False


def run(program, state, instr=0):
    program = tuple(int(n) for n in program.split(","))
    r = []
    while instr < len(program):
        assert instr % 2 == 0
        opcode = program[instr]
        operand = program[instr + 1]
        A, B, C = state
        match opcode:
            case 0:
                operand = resolve_combo(state, operand)
                v = A // (2**operand)
                state = (v, B, C)
            case 1:
                state = (A, B ^ operand, C)
            case 2:
                operand = resolve_combo(state, operand)
                state = (A, operand % 8, C)
            case 3:
                if A != 0:
                    instr = operand
                    continue
            case 4:
                state = (A, B ^ C, C)
            case 5:
                operand = resolve_combo(state, operand)
                r.append(str(operand % 8))
            case 6:
                operand = resolve_combo(state, operand)
                v = A // (2**operand)
                state = (A, v, C)
            case 7:
                operand = resolve_combo(state, operand)
                v = A // (2**operand)
                state = (A, B, v)
            case _:
                assert False
        instr += 2
    return ",".join(r), state


assert run("5,0,5,1,5,4", (10, 0, 0)) == ("0,1,2", (10, 0, 0))
assert run("0,1,5,4,3,0", (2024, 0, 0)) == ("4,2,5,6,7,7,7,7,3,1,0", (0, 0, 0))
assert run("1,7", (0, 29, 0)) == ("", (0, 26, 0))
assert run("4,0", (0, 2024, 43690)) == ("", (0, 44354, 43690))
assert run("0,1,5,4,3,0", (729, 0, 0)) == ("4,6,3,5,6,3,5,2,1,0", (0, 0, 0))
A = 0
B = 0
C = 0
print("ANSWER", run("--- the program ---", (A, B, C))[0])
