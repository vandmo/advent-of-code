from algorithms import dijkstra_shortest_path
from vector2d import *
import math

START = ORIGIN
END = Vector2D(70, 70)
bounds = InclusiveBounds2D(START, END)

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines() if line.strip() != ""]


def can_reach(imax):
    corrupted = set(
        Vector2D(*(int(n) for n in lines[i].split(","))) for i in range(imax)
    )
    edges = set()
    for v in bounds.discrete_points():
        if v in corrupted:
            continue
        for direction in (UP, DOWN, LEFT, RIGHT):
            neigbour = v + direction
            if neigbour in bounds and neigbour not in corrupted:
                edges.add((v, neigbour, 1))
    distances, _ = dijkstra_shortest_path(edges, START, END)
    return distances[END] < math.inf


def solve():
    L = len(lines)
    reachable = -1
    unreachable = L
    i = L // 2
    while True:
        result = can_reach(i)
        if result:
            if unreachable == i + 1:
                return i
            else:
                reachable = i
                i = (reachable + unreachable) // 2
        else:
            if reachable == i - 1:
                return i - 1
            else:
                unreachable = i
                i = (reachable + unreachable) // 2


print("ANSWER", lines[solve()])
