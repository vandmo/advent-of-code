from hashlib import md5
from collections import deque

INPUT = "ulqzkmiv"


def candidates(passcode, location, path):
    doors = md5(f"{passcode}{path}".encode()).hexdigest()
    x, y = location
    result = []
    if y > 0 and doors[0] in "bcdef":
        result.append(((x, y - 1), f"{path}U"))
    if y < 3 and doors[1] in "bcdef":
        result.append(((x, y + 1), f"{path}D"))
    if x > 0 and doors[2] in "bcdef":
        result.append(((x - 1, y), f"{path}L"))
    if x < 3 and doors[3] in "bcdef":
        result.append(((x + 1, y), f"{path}R"))
    return result


def solve_p1(passcode):
    visited = set()
    q = deque()
    q.append(((0, 0), ""))
    while q:
        node = q.popleft()
        location, path = node
        if location == (3, 3):
            return path
        if node in visited:
            continue
        q.extend(candidates(passcode, location, path))
        visited.add(node)
    return None


def solve_p2(passcode):
    visited = set()
    q = deque()
    q.append(((0, 0), ""))
    longest = 0
    while q:
        node = q.popleft()
        location, path = node
        if location == (3, 3):
            longest = max(len(path), longest)
            continue
        if node in visited:
            continue
        q.extend(candidates(passcode, location, path))
        visited.add(node)
    return longest


print("ANSWER PART 1:", solve_p1(INPUT))
print("ANSWER PART 2:", solve_p2(INPUT))
