from itertools import pairwise

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


def is_safe(ns):
    if ns[0] > ns[1]:
        for a, b in pairwise(ns):
            if a <= b:
                return False
            if abs(a - b) < 1 or abs(a - b) > 3:
                return False
        return True
    if ns[0] < ns[1]:
        for a, b in pairwise(ns):
            if a >= b:
                return False
            if abs(a - b) < 1 or abs(a - b) > 3:
                return False
        return True
    return False


print("ANSWER", sum(1 for line in lines if is_safe([int(n) for n in line.split()])))
