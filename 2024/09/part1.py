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
            blocks.append(id)
        id += 1
    odd = not odd


def get_block(r, rmin):
    while r > rmin:
        r -= 1
        if blocks[r] != ".":
            v = blocks[r]
            blocks[r] = "."
            return r, v
    return None


r = len(blocks)

for i in range(len(blocks)):
    if blocks[i] == ".":
        block = get_block(r, i)
        if block == None:
            break
        r, v = block
        blocks[i] = v


print("ANSWER", sum(i * n for i, n in enumerate(blocks) if n != "."))
