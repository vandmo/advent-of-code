from collections import Counter

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


L = sorted([int(l.split("   ")[0]) for l in lines])
R = Counter(sorted([int(l.split("   ")[1]) for l in lines]))
S = 0

for anl in L:
    S += anl * R[anl]

print("ANSWER", S)
