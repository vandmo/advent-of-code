from functools import cache
from math import inf


def parse():
    reading_medicine_molecule = False
    medicine_molecule = None
    replacements = dict()
    for line in open("input.txt"):
        line = line.strip()
        if not line:
            assert not reading_medicine_molecule
            reading_medicine_molecule = True
        if reading_medicine_molecule:
            medicine_molecule = line
        else:
            source, target = line.split(" => ")
            replacements.setdefault(source, set()).add(target)
    assert medicine_molecule is not None
    return replacements, medicine_molecule


replacements, medicine_molecule = parse()


def part1():
    s = set()
    for source, targets in replacements.items():
        for target in targets:
            o = 0
            while True:
                i = medicine_molecule.find(source, o)
                if i < 0:
                    break
                s.add(
                    medicine_molecule[:i]
                    + target
                    + medicine_molecule[i + len(source) :]
                )
                o = i + 1

    return len(s)


@cache
def distance_between(source, target):
    if source == target:
        return 0
    if len(source) > len(target):
        return inf
    possible_replacements = replacements.get(source, set())
    if target in possible_replacements:
        return 1
    best = inf
    for i in range(len(source) - 1):
        SL = source[: i + 1]
        SR = source[i + 1 :]
        for j in range(len(target) - 1):
            D1 = distance_between(SL, target[: j + 1])
            if D1 == inf:
                continue
            best = min(best, D1 + distance_between(SR, target[j + 1 :]))
    for replacement in possible_replacements:
        best = min(best, distance_between(replacement, target) + 1)
    return best


print("ANSWER PART 1:", part1())
print("Will take about 5 minutes...")
print("ANSWER PART 2:", distance_between("e", medicine_molecule))
