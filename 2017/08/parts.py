from collections import defaultdict
from math import inf

registers = defaultdict(int)
M = -inf
for line in open("input.txt"):
    line = line.strip()
    lhs, rhs = line.split(" if ")
    if eval(rhs, registers.copy()):
        if " inc " in lhs:
            L, R = lhs.split(" inc ")
            m = 1
        else:
            assert " dec " in lhs
            L, R = lhs.split(" dec ")
            m = -1
        registers[L] += m * int(R)
        M = max(M, registers[L])

print("ANSWER PART 1:", max(registers.values()))
print("ANSWER PART 2:", M)
