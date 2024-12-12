from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]

grid = defaultdict(lambda: ".")

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[x + y * 1j] = c

W = len(lines[0])
H = len(lines)

visited = set()


def find_region(p, fences):
    if p in visited:
        return 0
    visited.add(p)
    c = grid[p]
    if c == ".":
        return 0
    res = 1
    for d in (1, -1, 1j, -1j):
        np = p + d
        n = grid[np]
        if n != c:
            if d == 1:
                fences.add((p + 1, "V"))
            elif d == -1:
                fences.add((p, "V"))
            elif d == 1j:
                fences.add((p + 1j, "H"))
            elif d == -1j:
                fences.add((p, "H"))
            else:
                assert False
    for d in (1, -1, 1j, -1j):
        np = p + d
        n = grid[np]
        if n == c:
            res += find_region(np, fences)
    return res


def trace_fence(fence, fences, visited_fences, direction=None):
    if fence in visited_fences:
        return 0
    visited_fences.add(fence)
    pos, d = fence
    if direction == None:
        if d == "H":
            direction = "R"
        elif d == "V":
            direction = "D"
        else:
            assert False
    if direction == "R":
        FORWARD = (pos + 1, "H")
        RIGHT = (pos + 1, "V")
        LEFT = (pos + 1 - 1j, "V")
        if FORWARD in fences:
            extra = 0
            if LEFT in fences:
                assert RIGHT in fences
                extra = 1
            return extra + trace_fence(FORWARD, fences, visited_fences, "R")
        elif RIGHT in fences:
            return 1 + trace_fence(RIGHT, fences, visited_fences, "D")
        elif LEFT in fences:
            return 1 + trace_fence(LEFT, fences, visited_fences, "U")
        else:
            assert False
    elif direction == "L":
        FORWARD = (pos - 1, "H")
        LEFT = (pos, "V")
        RIGHT = (pos - 1j, "V")
        if FORWARD in fences:
            extra = 0
            if LEFT in fences:
                assert RIGHT in fences
                extra = 1
            return extra + trace_fence(FORWARD, fences, visited_fences, "L")
        elif LEFT in fences:
            return 1 + trace_fence(LEFT, fences, visited_fences, "D")
        elif RIGHT in fences:
            return 1 + trace_fence(RIGHT, fences, visited_fences, "U")
        else:
            assert False
    elif direction == "D":
        FORWARD = (pos + 1j, "V")
        RIGHT = (pos - 1 + 1j, "H")
        LEFT = (pos + 1j, "H")
        if FORWARD in fences:
            extra = 0
            if LEFT in fences:
                assert RIGHT in fences
                extra = 1
            return extra + trace_fence(FORWARD, fences, visited_fences, "D")
        elif RIGHT in fences:
            return 1 + trace_fence(RIGHT, fences, visited_fences, "L")
        elif LEFT in fences:
            return 1 + trace_fence(LEFT, fences, visited_fences, "R")
        else:
            assert False
    elif direction == "U":
        FORWARD = (pos - 1j, "V")
        RIGHT = (pos, "H")
        LEFT = (pos - 1, "H")
        if FORWARD in fences:
            extra = 0
            if LEFT in fences:
                assert RIGHT in fences
                extra = 1
            return extra + trace_fence(FORWARD, fences, visited_fences, "U")
        elif RIGHT in fences:
            return 1 + trace_fence(RIGHT, fences, visited_fences, "R")
        elif LEFT in fences:
            return 1 + trace_fence(LEFT, fences, visited_fences, "L")
        else:
            assert False
    else:
        assert False


def count_fences(fences, visited_fences):
    cnt = 0
    for fence in fences:
        if fence in visited_fences:
            continue
        cnt += trace_fence(fence, fences, visited_fences)
    return cnt


regions = []
for x in range(W):
    for y in range(H):
        fences = set()
        L = find_region(x + y * 1j, fences)
        if L > 0:
            regions.append((L, fences))

s = 0
for region in regions:
    L, fences = region
    s += count_fences(fences, set()) * L

print("ANSWER", s)
