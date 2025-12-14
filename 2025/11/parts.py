outgoing_edges: dict[str, set[str]] = dict()
incoming_edges: dict[str, set[str]] = dict()
weights: dict[tuple[str, str], int] = dict()

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    source, targets = line.split(": ")
    targets = targets.split()
    for target in targets:
        weights[source, target] = 1
        incoming_edges.setdefault(target, set()).add(source)
    outgoing_edges[source] = set(targets)


def part1():
    def waysout(p):
        if p == "out":
            return 1
        return sum(waysout(x) for x in outgoing_edges[p])

    return waysout("you")


def part2():
    def merge(incoming_node, node, outgoing_node):
        ways = weights[incoming_node, node] * weights[node, outgoing_node]
        weights[incoming_node, outgoing_node] = (
            weights.get((incoming_node, outgoing_node), 0) + ways
        )

        outgoing_from_incoming = outgoing_edges.setdefault(incoming_node, set())
        outgoing_from_incoming.add(outgoing_node)
        outgoing_from_incoming.discard(node)

        incoming_from_outgoing = incoming_edges.setdefault(outgoing_node, set())
        incoming_from_outgoing.add(incoming_node)
        incoming_from_outgoing.discard(node)

    for node in set(outgoing_edges.keys()):
        if node not in ("svr", "out", "fft", "dac"):
            for incoming_node in incoming_edges.get(node, []):
                for outgoing_node in outgoing_edges.get(node, []):
                    merge(incoming_node, node, outgoing_node)

    via_fft_dac = (
        weights.get(("svr", "fft"), 0)
        * weights.get(("fft", "dac"), 0)
        * weights.get(("dac", "out"), 0)
    )
    via_dac_fft = (
        weights.get(("svr", "dac"), 0)
        * weights.get(("dac", "fft"), 0)
        * weights.get(("fft", "out"), 0)
    )
    return via_dac_fft + via_fft_dac


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
