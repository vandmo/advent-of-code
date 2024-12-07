from operator import add, mul

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

equations = []


def concat(lhs, rhs):
    return int(str(lhs) + str(rhs))


for line in lines:
    s, p = line.split(":")
    s = int(s)
    p = tuple([int(n) for n in p.strip().split(" ")])
    equations.append((s, p))


def is_solveable(target, current, rest):
    if len(rest) == 0:
        return target == current
    if target < current:
        return False
    for operator in [add, mul, concat]:
        if is_solveable(target, operator(current, rest[0]), rest[1:]):
            return True
    return False


answer = 0
for equation in equations:
    if is_solveable(equation[0], equation[1][0], equation[1][1:]):
        answer += equation[0]

print("ANSWER", answer)
