import math

from collections import defaultdict
from sys import setrecursionlimit

from vector2d import *

setrecursionlimit(1_000_000)


def parse():
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines() if line.strip() != ""]

    grid = defaultdict(lambda: "#")
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            p = Vector2D(x, y)
            if c == "S":
                start = p
            if c == "E":
                end = p
            grid[p] = c

    assert start is not None
    assert end is not None
    return grid, start, end


def find_distances_and_path(grid, start, end):
    distances = dict()
    path = []
    visited = set()

    def trace(p):
        if grid[p] not in ".SE":
            return
        if p in visited:
            return
        visited.add(p)
        path.append(p)
        distances[p] = len(visited)
        for d in (LEFT, RIGHT, UP, DOWN):
            trace(p + d)

    trace(start)

    # Invert distances
    totaldist = distances[end]
    for k in distances.keys():
        distances[k] = totaldist - distances[k]
    return distances, path


grid, start, end = parse()
distances, path = find_distances_and_path(grid, start, end)


def find_answer(distances, path, max_cheat_distance):
    answer = 0
    for v in path:
        for radius in range(2, max_cheat_distance + 1):

            def check(cheat_to):
                distance_after_cheating = distances.get(cheat_to, math.inf)
                if distance_after_cheating < distances[v] - radius:
                    saved = distances[v] - distance_after_cheating - radius
                    if saved >= 100:
                        return 1
                return 0

            for i in range(0, radius):
                answer += check(v + Vector2D(i - radius, i))
                answer += check(v + Vector2D(radius - i, -i))
                answer += check(v + Vector2D(i, radius - i))
                answer += check(v + Vector2D(-i, i - radius))
    return answer


print("ANSWER PART1", find_answer(distances, path, 2))
print("ANSWER PART2", find_answer(distances, path, 20))
