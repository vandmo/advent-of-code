import heapq

from collections import defaultdict
from collections.abc import Iterable
from itertools import combinations
from math import inf
from typing import Literal

type Item = Literal[
    "PrG",
    "PrM",
    "CoG",
    "CuG",
    "PlG",
    "RG",
    "CoM",
    "CuM",
    "PlM",
    "RM",
    "DG",
    "DM",
    "EG",
    "EM",
    "HM",
    "LM",
    "HG",
    "LG",
]
type Floor = tuple[Item, ...]
type State = tuple[int, tuple[Floor, Floor, Floor, Floor]]


def part1_state() -> State:
    floors = tuple()
    for line in open("input.txt"):
        line = line.strip()
        if not line:
            continue
        floor = []
        if "promethium generator" in line:
            floor.append("PrG")
        if "promethium-compatible microchip" in line:
            floor.append("PrM")
        if "cobalt generator" in line:
            floor.append("CoG")
        if "curium generator" in line:
            floor.append("CuG")
        if "plutonium generator" in line:
            floor.append("PlG")
        if "ruthenium generator" in line:
            floor.append("RG")
        if "cobalt-compatible microchip" in line:
            floor.append("CoM")
        if "curium-compatible microchip" in line:
            floor.append("CuM")
        if "plutonium-compatible microchip" in line:
            floor.append("PlM")
        if "ruthenium-compatible microchip" in line:
            floor.append("RM")
        floors += (tuple(floor),)
    assert len(floors) == 4
    return 1, floors


def part2_state() -> State:
    """
    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.
    """
    floor, (p1f1, p1f2, p1f3, p1f4) = part1_state()
    return floor, (tuple(sorted(p1f1 + ("DG", "DM", "EG", "EM"))), p1f2, p1f3, p1f4)


def is_safe(items: Iterable[Item]):
    chips = set(item[:-1] for item in items if item.endswith("M"))
    generators = set(item[:-1] for item in items if item.endswith("G"))
    if not generators:
        return True
    for chip in chips:
        if chip not in generators:
            return False
    return True


assert not is_safe(["CuG", "CuM", "PlM", "PrG", "PrM"])
assert is_safe(["HM", "LM"])
assert is_safe(["HG", "HM", "LG"])
assert is_safe(["HG", "LG"])
assert is_safe(["HG", "HM", "LG"])
assert is_safe(["HG", "HM", "LG", "LM"])
assert not is_safe(["HG", "HM", "LM"])


def next_states(state: State):
    current_floor, floors = state
    current_floor_items = set(floors[current_floor - 1])
    possible_item_sets_to_pick = list()
    for i in range(1, 3):
        for items in combinations(current_floor_items, i):
            items = set(items)
            others = current_floor_items - items
            if is_safe(others):
                possible_item_sets_to_pick.append((tuple(items), tuple(others)))

    def for_floor(possible_floor):
        for possible_items_to_pick, remaining_on_floor in possible_item_sets_to_pick:
            possible_items = floors[possible_floor - 1] + possible_items_to_pick
            if is_safe(possible_items):
                new_floors = list(floors)
                new_floors[current_floor - 1] = tuple(sorted(remaining_on_floor))
                new_floors[possible_floor - 1] = tuple(sorted(possible_items))
                yield (possible_floor, tuple(new_floors))

    if current_floor > 1:
        yield from for_floor(current_floor - 1)
    if current_floor < 4:
        yield from for_floor(current_floor + 1)


def shortest_path(edge_generator, source: State, target):
    distances = defaultdict(lambda: inf)
    prev = dict()
    visited = set()
    distances[source] = 0
    priority_queue = [(0, source)]
    while priority_queue:
        _, u = heapq.heappop(priority_queue)
        if u == target:
            return distances, prev
        visited.add(u)
        for v in edge_generator(u):
            if v in visited:
                continue
            alt = distances[u] + 1
            if alt < distances[v]:
                distances[v] = alt
                prev[v] = u
                heapq.heappush(priority_queue, (int(alt), v))
    return distances, prev


def solve(start_state: State):
    wanted_state = 4, (
        tuple(),
        tuple(),
        tuple(),
        tuple(sorted(sum(start_state[1], tuple()))),
    )
    distances, _ = shortest_path(next_states, start_state, wanted_state)
    return distances[wanted_state]


print("ANSWER PART 1:", solve(part1_state()))
print("Might take around 5 minutes...")
print("ANSWER PART 2:", solve(part2_state()))
