from collections import Counter, defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

neigbours = defaultdict(lambda: set())

for line in lines:
    a, b = line.split("-")
    neigbours[a].add(b)
    neigbours[b].add(a)

counter = Counter()
for k, v in neigbours.items():
    for n in v:
        counter[",".join(sorted(v.intersection(neigbours[n]) | set([k, n])))] += 1
print("ANSWER", counter.most_common(1)[0][0])
