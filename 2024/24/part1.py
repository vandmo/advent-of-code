with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


wires = dict()
gates = list()
for line in lines:
    if "->" in line:
        L, op, R, _, T = line.split(" ")
        gates.append((L, op, R, T))
    else:
        n, v = line.split(": ")
        wires[n] = int(v)


while True:
    changed = False
    for L, op, R, T in gates:
        if L in wires and R in wires and T not in wires:
            changed = True
            if op == "XOR":
                wires[T] = wires[L] ^ wires[R]
            elif op == "OR":
                wires[T] = wires[L] | wires[R]
            elif op == "AND":
                wires[T] = wires[L] & wires[R]
            else:
                assert False
    if not changed:
        break

s = ""
for b in sorted(wires.keys()):
    if b.startswith("z"):
        s += str(wires[b])
print("ANSWER", int(s[::-1], 2))
