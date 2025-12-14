shapes = {}
counts = {}
trees = []

lines = [line.strip() for line in open("input.txt")]
i = 0
while i < len(lines):
    line = lines[i]
    if "x" in line:
        a, b = line.split(": ")
        w, h = [int(n) for n in a.split("x")]
        presents = [int(n) for n in b.split()]
        trees.append(((w, h), presents))
        i += 1
    elif ":" in line:
        idx = int(line.removesuffix(":"))
        lines_for_shape = lines[i + 1 : i + 4]
        shapes[idx] = lines_for_shape
        counts[idx] = sum(1 for c in "".join(lines_for_shape) if c == "#")
        i += 5
    else:
        assert False

count = 0
for (w, h), presents in trees:
    number_of_presents = sum(presents)
    parts = sum(counts[i] * p for i, p in enumerate(presents))
    if parts <= w * h:
        q, r = divmod(number_of_presents, w // 3)
        if r > 0:
            q += 1
        if q <= h // 3:
            count += 1
        else:
            raise Exception("This was not part of the deal!")

print("ANSWER PART 1:", count)
