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


def fix(update):
    def sort():
        for i in range(1, len(update)):
            v = update[i]
            succeders = rules[v]
            for j in range(0, i):
                w = update[j]
                if w in succeders:
                    update[i] = w
                    update[j] = v
                    return True
        return False

    while sort():
        pass


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
        continue
    fix(update)
    s += update[len(update) // 2]

print("ANSWER", s)
