from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    x: int
    y: int
    used: int
    avail: int


def parse_node(line: str):
    node, _, used, avail, _ = line.split()
    node = node.removeprefix("/dev/grid/node-x")
    x, y = tuple(int(n) for n in node.split("-y"))
    return Node(x=x, y=y, used=int(used[:-1]), avail=int(avail[:-1]))


NODES = tuple(
    parse_node(line)
    for line in open("input.txt")
    if line.strip()
    and not line.startswith("root@")
    and not line.startswith("Filesystem")
)
NODES_BY_COORD = {(node.x, node.y): node for node in NODES}
WIDTH = max(node.x for node in NODES) + 1
HEIGHT = max(node.y for node in NODES) + 1


def part1():
    count = 0
    for i in range(len(NODES) - 1):
        for j in range(i + 1, len(NODES)):
            node_a = NODES[i]
            node_b = NODES[j]
            if node_a.used > 0 and node_a.used <= node_b.avail:
                count += 1
            if node_b.used > 0 and node_b.used <= node_a.avail:
                count += 1
    return count


def part2():

    EMPTY = None
    for node in NODES:
        if node.used == 0:
            assert EMPTY is None
            EMPTY = node
    assert EMPTY is not None

    def distance(source, target, max_used: int):
        q = deque([(0, source)])
        visited = set()
        while q:
            dist, N = q.popleft()
            if N in visited:
                continue
            visited.add(N)
            if N == target:
                return dist
            Nx, Ny = N
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                P = Nx + dx, Ny + dy
                Pnode = NODES_BY_COORD.get(P)
                if Pnode is None:
                    continue
                if Pnode.used > max_used:
                    continue
                q.append((dist + 1, P))
        assert False

    count = 0
    # move empty node to the left of the target data
    count += distance((EMPTY.x, EMPTY.y), (WIDTH - 2, 0), EMPTY.avail)
    # move target data one step left
    count += 1
    # every additional step to the left takes 5 moves
    count += (WIDTH - 2) * 5
    return count


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
