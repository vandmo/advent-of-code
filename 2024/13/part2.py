from dataclasses import dataclass
from fractions import Fraction

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


@dataclass(frozen=True)
class Machine:
    Ax: int
    Ay: int
    Bx: int
    By: int
    prizeX: int
    prizeY: int

    def solve(self):
        A = Fraction(
            self.prizeX * self.By - self.Bx * self.prizeY,
            self.Ax * self.By - self.Bx * self.Ay,
        )
        B = Fraction(self.prizeX - self.Ax * A, self.Bx)
        if A.is_integer() and B.is_integer():
            return A * 3 + B
        return 0


machines: list[Machine] = []

for line in lines:
    if line.startswith("Button A: "):
        p = line.split(" ")
        ax = int(p[2].split("+")[1].strip(","))
        ay = int(p[3].split("+")[1])
    elif line.startswith("Button B: "):
        p = line.split(" ")
        bx = int(p[2].split("+")[1].strip(","))
        by = int(p[3].split("+")[1])
    elif line.startswith("Prize: "):
        p = line.split(" ")
        prizeX = 10000000000000 + int(p[1].split("=")[1].strip(","))
        prizeY = 10000000000000 + int(p[2].split("=")[1])
        machines.append(
            Machine(Ax=ax, Ay=ay, Bx=bx, By=by, prizeX=prizeX, prizeY=prizeY)
        )
    else:
        assert False

print("ANSWER", sum(machine.solve() for machine in machines))
