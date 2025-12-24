from collections import deque
from itertools import pairwise, permutations

grid = {}
places = {}
for y, line in enumerate(open("input.txt")):
    for x, c in enumerate(line.strip()):
        if c in ["#", "."]:
            grid[(x, y)] = c
        else:
            grid[(x, y)] = "."
            places[c] = (x, y)


def shortest(source, target):
    visited = set()
    q = deque()
    q.append((0, source))
    while q:
        node = q.popleft()
        distance, location = node
        if location == target:
            return distance
        if node in visited:
            continue
        x, y = location
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = x + dx, y + dy
            nb = grid.get(np)
            if nb is None:
                continue
            if nb == ".":
                q.append((distance + 1, np))
        visited.add(node)


distance_map = {}
for k, v in places.items():
    for k2, v2 in places.items():
        distance_map[(k, k2)] = shortest(v, v2)

places_to_visit = tuple(sorted(k for k in places.keys() if k != "0"))

print(
    "ANSWER PART 1:",
    min(
        sum(distance_map[step] for step in pairwise(("0",) + visit_order))
        for visit_order in permutations(places_to_visit)
    ),
)
print(
    "ANSWER PART 2:",
    min(
        sum(distance_map[step] for step in pairwise(("0",) + visit_order + ("0",)))
        for visit_order in permutations(places_to_visit)
    ),
)
