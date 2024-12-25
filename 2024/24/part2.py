from graphml import Graph


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


gates = dict()
for line in lines:
    if "->" in line:
        L, op, R, _, T = line.split(" ")
        gates[T] = (L, op, R)


def calculate(wire, input_wires):
    if wire in input_wires:
        return input_wires[wire]
    L, op, R = gates[wire]
    Lv = calculate(L, input_wires)
    Rv = calculate(R, input_wires)
    if op == "XOR":
        return Lv ^ Rv
    elif op == "OR":
        return Lv | Rv
    elif op == "AND":
        return Lv & Rv
    else:
        assert False


def add(x, y):
    constants = dict()
    for i in range(45):
        constants[f"x{i:02}"] = x & 0b1
        constants[f"y{i:02}"] = y & 0b1
        x >>= 1
        y >>= 1
    return sum(calculate(f"z{i:02}", constants) << i for i in range(45))


add_failed = set()
carry_failed = set()
for i in range(45):
    if add(1 << i, 0) != 1 << i or add(0, 1 << i) != 1 << i:
        add_failed.add(i)
        print(f"Addition failure at {i}")
    if add(1 << i, 1 << i) != 1 << (i + 1) and i < 44:
        print(f"Failed carry from {i}")
        carry_failed.add(i)


g = Graph()
for i in range(45):
    g.add_node(f"x{i:02}", color="#335511")
    g.add_node(f"y{i:02}", color="#335511")
for i in range(46):
    id = f"z{i:02}"
    if i in add_failed:
        g.add_node(id, color="#FF1111", label=f"{id} (very suspect)", size=2.0)
    elif i in carry_failed:
        g.add_node(id, color="#FF8888", label=f"{id} (a little suspect)", size=1.4)
    else:
        g.add_node(id, color="#3333FF", label=f"{id}")

for T, (L, op, R) in gates.items():
    gate = f"{L}{op}{R}"
    if op == "XOR":
        color = "#2244FF"
    elif op == "OR":
        color = "#44FF22"
    elif op == "AND":
        color = "#FF2244"
    g.add_node(gate, form="diamond", label=f"{L} {op} {R}", color=color)
    if T[0] not in "xyz":
        g.add_node(T, label=f"{T}")
    g.add_edge(L, gate)
    g.add_edge(R, gate)
    g.add_edge(gate, T)

with open("addition.graphml", "w") as f:
    f.write(str(g))

print(
    "Wrote addition.graphml, open with yEd, do organic layout, and find the faulty wires manually..."
)
