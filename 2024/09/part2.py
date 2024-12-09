with open("input.txt") as f:
    line = f.read().strip()

blocks = []
odd = False
id = 0
for c in line:
    n = int(c)
    if odd:
        for _ in range(n):
            blocks.append(".")
    else:
        for _ in range(n):
            blocks.append(str(id))
        id += 1
    odd = not odd

r = len(blocks) - 1


def find():
    global r
    if r < 1:
        return
    R = r
    while blocks[R] == ".":
        if R < 0:
            return None
        R -= 1
    c = blocks[R]
    L = R
    while blocks[L] == c:
        if L <= 0:
            r = 0
            return 0, R + 1
        L -= 1
    r = L
    return L + 1, R + 1


def trymove(L, R):
    D = R - L
    for i in range(L):
        if set(blocks[i : i + D]) == set("."):
            for j in range(D):
                v = blocks[L + j]
                blocks[L + j] = "."
                blocks[i + j] = v
            return


print("Grab some coffee...")
while True:
    f = find()
    if f == None:
        break
    L, R = f
    trymove(L, R)

print("ANSWER", sum(i * int(n) for i, n in enumerate(blocks) if n != "."))
