from collections import deque

N = 1362
TARGET = 31, 39
START = 1, 1
DELTAS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_wall(p):
    x, y = p
    v: int = N + x * x + 3 * x + 2 * x * y + y + y * y
    return v.bit_count() % 2 == 1


def part1():
    visited = set()
    q = deque()
    q.append((0, START))
    while q:
        distance, location = q.popleft()
        if location == TARGET:
            return distance
        if location in visited:
            continue
        if not is_wall(location):
            x, y = location
            for dx, dy in DELTAS:
                q.append((distance + 1, (x + dx, y + dy)))
        visited.add(location)
    assert 0


def part2():
    visited = set()
    reached = 0
    q = deque()
    q.append((0, START))
    while q:
        distance, location = q.popleft()
        if location in visited:
            continue
        x, y = location
        if not is_wall(location) and distance <= 50 and x >= 0 and y >= 0:
            reached += 1
            for dx, dy in DELTAS:
                q.append((distance + 1, (x + dx, y + dy)))
        visited.add(location)
    return reached


print("ANSWER PART 1:", part1())
print("ANSWER PART 2:", part2())
