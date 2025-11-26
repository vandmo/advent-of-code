import operator

known = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

sues = []
for line in open("input.txt"):
    sue = dict()
    number, owned = line.split(":", 1)
    for thing in owned.split(","):
        id, count = thing.split(":")
        id = id.strip()
        count = int(count)
        sue[id] = count
    sues.append((number, sue))


def is_the_sue(sue):
    _, sue = sue
    for item in known.splitlines():
        id, count = item.split(":")
        id = id.strip()
        count = int(count)
        if count == 0:
            if id in sue and sue[id] != 0:
                return False
        elif id in sue:
            if count != sue[id]:
                return False
    return True


def is_the_real_sue(sue):
    _, sue = sue
    for item in known.splitlines():
        id, count = item.split(":")
        id = id.strip()
        count = int(count)
        if id in ("cats", "trees"):
            cmp = operator.le
        elif id in ("pomeranians", "goldfish"):
            cmp = operator.gt
        else:
            cmp = operator.eq
        if count == 0:
            if id in sue and not cmp(sue[id], 0):
                return False
        elif id in sue:
            if not cmp(count, sue[id]):
                return False
    return True


possible_sues = list(filter(is_the_sue, sues))
assert len(possible_sues) == 1
print("ANSWER PART 1:", possible_sues[0])

possible_real_sues = list(filter(is_the_real_sue, sues))
assert len(possible_real_sues) == 1
print("ANSWER PART 2:", possible_real_sues[0])
