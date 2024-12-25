from itertools import batched, product


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

keys = list()
locks = list()

for line in batched(lines, 7):
    a, b, c, d, e = -1, -1, -1, -1, -1
    nlines = list(line)
    for nline in nlines:
        if nline[0] == "#":
            a += 1
        if nline[1] == "#":
            b += 1
        if nline[2] == "#":
            c += 1
        if nline[3] == "#":
            d += 1
        if nline[4] == "#":
            e += 1
    if nlines[0] == "#####":
        locks.append((a, b, c, d, e))
    else:
        assert nlines[6] == "#####"
        keys.append((a, b, c, d, e))


def fit(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True


print("ANSWER", sum(1 for key, lock in product(keys, locks) if fit(key, lock)))
