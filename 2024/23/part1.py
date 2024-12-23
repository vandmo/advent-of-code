from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

neigbours = defaultdict(lambda: set())

for line in lines:
    a, b = line.split("-")
    neigbours[a].add(b)
    neigbours[b].add(a)

found = set()
for k1 in neigbours.keys():
    if not k1.startswith("t"):
        continue
    for k2 in neigbours.keys():
        if k2 == k1:
            continue
        for k3 in neigbours.keys():
            if k3 == k2:
                continue
            if k1 in neigbours[k2] and k2 in neigbours[k3] and k3 in neigbours[k1]:
                found.add(tuple(sorted([k1, k2, k3])))
print("ANSWER", len(found))
