from itertools import product


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

equations = []

for line in lines:
    s, p = line.split(":")
    s = int(s)
    p = tuple([int(n) for n in p.strip().split(" ")])
    equations.append((s, p))


def is_solveable(equation):
    s, p = equation
    for operators in product(["*", "+", "||"], repeat=len(p) - 1):
        v = p[0]
        for j, operator in enumerate(operators):
            if operator == "*":
                v *= p[j + 1]
            elif operator == "+":
                v += p[j + 1]
            elif operator == "||":
                v = int(str(v) + str(p[j + 1]))
            else:
                assert False
        if v == s:
            return True
    return False


answer = 0
for equation in equations:
    if is_solveable(equation):
        answer += equation[0]

print("ANSWER", answer)
