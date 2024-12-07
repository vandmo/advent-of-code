from collections import Counter, defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

W = len(lines[0])
H = len(lines)

grid = defaultdict(lambda: "Q")
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x, y)] = c

s = 0

for x in range(W):
    for y in range(H):
        L1 = grid[(x - 1, y - 1)] + grid[(x, y)] + grid[(x + 1, y + 1)]
        L2 = grid[(x + 1, y - 1)] + grid[(x, y)] + grid[(x - 1, y + 1)]
        L3 = L1[::-1]
        L4 = L2[::-1]
        LS = [L1, L2, L3, L4]
        cnt = Counter(LS)
        if cnt["MAS"] == 2:
            s += 1

print("ANSWER", s)
