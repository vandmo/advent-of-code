from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

rules = defaultdict(lambda: [])
updates = []
for line in lines:
    if "|" in line:
        parts = line.split("|")
        L = int(parts[0])
        R = int(parts[1])
        rules[L].append(R)
    else:
        updates.append([int(i) for i in line.split(",")])


def is_right(update):
    for i in range(len(update)):
        v = update[i]
        for succeders in rules[v]:
            if succeders in update[0:i]:
                return False
    return True


s = 0
for update in updates:
    if is_right(update):
        s += update[len(update) // 2]

print("ANSWER", s)
