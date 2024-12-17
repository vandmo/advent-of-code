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


def run(program, A):
    r = tuple()
    B = 0
    C = 0
    instr = 0
    while instr < len(program):
        assert instr % 2 == 0
        opcode = program[instr]
        operand = program[instr + 1]
        match opcode:
            case 0:
                operand = resolve_combo((A, B, C), operand)
                A = A // (2**operand)
            case 1:
                B = B ^ operand
            case 2:
                operand = resolve_combo((A, B, C), operand)
                B = operand % 8
            case 3:
                if A != 0:
                    instr = operand
                    continue
            case 4:
                B = B ^ C
            case 5:
                operand = resolve_combo((A, B, C), operand)
                r += (operand % 8,)
            case 6:
                operand = resolve_combo((A, B, C), operand)
                B = A // (2**operand)
            case 7:
                operand = resolve_combo((A, B, C), operand)
                C = A // (2**operand)
            case _:
                assert False
        instr += 2
    return r


def find(program, implementation):
    L = len(program)
    if len(program) == 0:
        return (0,)
    solutions = tuple()
    for partial_solutions in find(program[1:], implementation):
        for a in range(8):
            s = partial_solutions * 8 + a
            R = implementation(s)
            if program == R:
                solutions += (s,)
    return solutions


def solve(program):
    parsed = tuple(int(n) for n in program.split(","))
    return min(find(parsed, lambda A: run(parsed, A)))


print("EXAMPLE", solve("0,3,5,4,3,0"))
print("ANSWER", solve("--- the program ---"))
