from dataclasses import dataclass

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


@dataclass(frozen=True)
class Machine:
    a: tuple[int, int]
    b: tuple[int, int]
    prize: tuple[int, int]


machines: list[Machine] = []

ca = None
cb = None

for line in lines:
    if line.startswith("Button A: "):
        p = line.split(" ")
        ca = (int(p[2].split("+")[1].strip(",")), int(p[3].split("+")[1]))
    elif line.startswith("Button B: "):
        p = line.split(" ")
        cb = (int(p[2].split("+")[1].strip(",")), int(p[3].split("+")[1]))
    elif line.startswith("Prize: "):
        p = line.split(" ")
        prize = (int(p[1].split("=")[1].strip(",")), int(p[2].split("=")[1]))
        machines.append(Machine(ca, cb, prize))
    else:
        assert False


s = 0
for machine in machines:
    best = None
    for a in range(0, 101):
        for b in range(0, 101):
            if (machine.a[0] * a + machine.b[0] * b) == machine.prize[0] and (
                machine.a[1] * a + machine.b[1] * b
            ) == machine.prize[1]:
                if best == None or a * 3 + b < best:
                    best = a * 3 + b
    if best != None:
        s += best
print("ANSWER", s)
